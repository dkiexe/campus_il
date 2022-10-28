# Server I wrote for the 2.6.2 client assignment
import chatlib
import socket

# Vital setup
print('Welcome to Trivia Server!')
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5678))
server_socket.listen()
print('starting up on port 5678')
(client_socket, client_adress) = server_socket.accept()

# Helper variables
white_list_users = ['david', 'ella']
high_score_table = {
    "dave": "15",
    "jones": "14",
    "camron": "13"
}

# Helper functions
def print_action(action_maker, adress_tuple, type_of_cmd):
    print(f'\n[{action_maker.upper()}] {"SENT MESSAGE" if action_maker == "client" else "RESPONSE TO [CLIENT]"} (IP: {adress_tuple[0]}, PORT:{adress_tuple[1]}, TYPE:{chatlib.parse_message(type_of_cmd)[0]})')

def strigfy_high_score_table(var_storing_table):
    lst = []
    for key,val in zip(var_storing_table.keys(), var_storing_table.values()):
        lst.append(f'{key}: {val}')
    return "\n".join(lst)

# Main server function
def main():
    client_score = 0
    logged_in = False
    # user login attempt
    while logged_in == False:
        client_sent_data = client_socket.recv(100).decode()
        print_action('client', client_adress, client_sent_data)
        print(client_sent_data)
        print_action('server', client_adress, client_sent_data)
        if chatlib.parse_message(client_sent_data)[1].split(chatlib.DATA_DELIMITER)[0] in white_list_users:
            server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER['login_ok_msg'], "").encode()
            print(server_sent_data.decode())
            client_socket.send(server_sent_data)
            logged_in = True
            break
        else:
            server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER['login_failed_msg'], "User not allowed!").encode()
            print(server_sent_data.decode())
            client_socket.send(server_sent_data)
            continue
    # user option select after login
    while logged_in == True:
        client_sent_data = client_socket.recv(100).decode()
        print_action('client', client_adress, client_sent_data)
        if chatlib.parse_message(client_sent_data)[0] not in chatlib.PROTOCOL_CLIENT.values():
            print_action('server', client_adress, client_sent_data)
            server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER['choice_err'], "Choice not recognized!").encode()
            print(server_sent_data.decode())
            client_socket.send(server_sent_data)
            continue
        match chatlib.parse_message(client_sent_data)[0]:
            case "SCORE":
                print_action('server', client_adress, client_sent_data)
                server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER['score_res'], f"{str(client_score)}").encode()
                print(server_sent_data.decode())
                client_socket.send(server_sent_data)
                continue
            case "HIGHSCORE":
                print_action('server', client_adress, client_sent_data)
                str_rep_of_highscore_table = strigfy_high_score_table(high_score_table)
                server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER['highscore_res'], fr"{str_rep_of_highscore_table}").encode()
                print(server_sent_data.decode())
                client_socket.send(server_sent_data)
                continue
            case "LOGOUT":
                print_action('server', client_adress, client_sent_data)
                print('Connection closed....')
                client_socket.close()
                server_socket.close()
                break
main()