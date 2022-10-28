# Server I wrote for the 2.6.3 client assignment
import chatlib
import socket
import sqlite3
import random
import os

# Vital setup
clear = lambda: os.system('cls')
clear()
print('Welcome to Trivia Server!')
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5678))
server_socket.listen()
print('starting up on port 5678')

# database connection - questions.
db_connection = sqlite3.connect(r"C:\Users\david\OneDrive\Desktop\Network.py\unit2\2.6.3\user_questions.db")
db_cursor = db_connection.cursor()
db_cursor.execute("SELECT rowid,* FROM questions")
all_questions_global = db_cursor.fetchall()
db_connection.commit()
db_connection.close()
# closing db after single time use

# Helper variables
white_list_users = ['david', 'ella']
high_score_table = {
    "dave": "15",
    "jones": "14",
    "camron": "13"
}
all_logged_users = []

# Helper functions
def print_action(action_maker, adress_tuple, type_of_cmd):
    print(f'\n[{action_maker.upper()}] {"SENT MESSAGE" if action_maker == "client" else "RESPONSE TO [CLIENT]"} (IP: {adress_tuple[0]}, PORT:{adress_tuple[1]}, TYPE:{chatlib.parse_message(type_of_cmd)[0]})')

def strigfy_high_score_table(var_storing_table):
    lst = []
    for key,val in zip(var_storing_table.keys(), var_storing_table.values()):
        lst.append(f'{key}: {val}')
    return "\n".join(lst)

def await_client_connection():
    print('\n Awaiting New Connection....')
    (client_socket, client_adress) = server_socket.accept()
    print(f'\n Connection received from {client_adress[0]}')
    main(client_socket, client_adress)

def error_client_side(socket_obj_client, reason_for_err):
    print('\n AN ERROR ACCOURED AND CLIENT DISCONNECTED!')
    print(f'Reason: {reason_for_err}')
    socket_obj_client.close()
    await_client_connection()

def client_data_recv(socket_obj_client, client_adress):
    try:
        client_sent_data = socket_obj_client.recv(100).decode()
        print_action('client', client_adress, client_sent_data)
        print(client_sent_data)
        return client_sent_data
    except Exception as err:
        error_client_side(socket_obj_client, err)

def server_data_send(socket_obj_client, cmd, message):
    try:
        server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER[cmd], message).encode()
        print(server_sent_data.decode())
        socket_obj_client.send(server_sent_data)
        return
    except Exception as err:
        error_client_side(socket_obj_client, err)

# Main server function
def main(client_socket, client_adress):
    all_questions_local = all_questions_global
    client_score = 0
    logged_in = False
    selected_question = ''
    # user login attempt
    while logged_in == False:
        client_sent_data = client_data_recv(client_socket, client_adress)
        print_action('server', client_adress, client_sent_data)
        if chatlib.parse_message(client_sent_data)[1].split(chatlib.DATA_DELIMITER)[0] in white_list_users:
            server_data_send(client_socket, 'login_ok_msg', "")
            logged_in = True
            all_logged_users.append(chatlib.parse_message(client_sent_data)[1].split(chatlib.DATA_DELIMITER)[0])
            break
        else:
            server_data_send(client_socket, 'login_failed_msg', 'User not white listed!')
            continue
    # user option select after login
    while logged_in == True:
        client_sent_data = client_data_recv(client_socket, client_adress)
        if chatlib.parse_message(client_sent_data)[0] not in chatlib.PROTOCOL_CLIENT.values(): # CMD CHECKER
            print_action('server', client_adress, client_sent_data)
            server_data_send(client_socket, 'choice_err', 'CMD not recognized')
            continue
        match chatlib.parse_message(client_sent_data)[0]: # checking the CMD TYPE
            case "SCORE":
                print_action('server', client_adress, client_sent_data)
                server_data_send(client_socket, 'score_res', str(client_score))
                continue
            case "HIGHSCORE":
                print_action('server', client_adress, client_sent_data)
                str_rep_of_highscore_table = strigfy_high_score_table(high_score_table)
                server_data_send(client_socket, 'highscore_res', str_rep_of_highscore_table)
                continue
            case "LOGOUT":
                print_action('server', client_adress, client_sent_data)
                print('Connection closed....')
                break
            case "QUESTION_REQ":
                print_action('server', client_adress, client_sent_data)
                try:
                    selected_question = random.choice(all_questions_local)
                except:
                    print_action('server', client_adress, client_sent_data)
                    server_data_send(client_socket, 'out_of_quastions', "")
                    continue
                # Sending client the question
                server_data_send(client_socket, 'question_res', str(selected_question[1:len(selected_question)-1])) # this question is sent as a string
                # all_questions_local.remove(selected_question)
            case "ANSWER":
                print_action('server', client_adress, client_sent_data)
                if chatlib.parse_message(client_sent_data)[1].replace('#', ' '.lower()) == selected_question[3].lower():
                    server_data_send(client_socket, 'answer_correct', '')
                    client_score += 5
                else:
                    server_data_send(client_socket, 'answer_wrong', selected_question[3])
            case "GET_LOGGED_USERS":
                print_action('server', client_adress, client_sent_data)
                server_data_send(client_socket, "logged_list", str(all_logged_users))
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    await_client_connection()