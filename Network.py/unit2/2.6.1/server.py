# Server I wrote for the 2.6.1 client assignment
import chatlib
import socket

print('Welcome to Trivia Server!')
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5678))
server_socket.listen()
print('starting up on port 5678')
(client_socket, client_adress) = server_socket.accept()
white_list_users = ['david', 'ella']

def main():
    # printing client info
    print(f'\n[CLIENT] SENT MESSAGE (IP: {client_adress[0]}, PORT: {client_adress[1]})')
    client_sent_data = client_socket.recv(100).decode()
    print(client_sent_data)
    print(f'\n[SERVER] RESPONSE TO [CLIENT] (IP: {client_adress[0]}, PORT: {client_adress[1]})')
    if chatlib.parse_message(client_sent_data)[1].split(chatlib.DATA_DELIMITER)[0] not in white_list_users:
        server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER['login_failed_msg'], "User not allowed!").encode()
        print(server_sent_data.decode())
        client_socket.send(server_sent_data)
        main()
    else:
        server_sent_data = chatlib.build_message(chatlib.PROTOCOL_SERVER['login_ok_msg'], "").encode()
        print(server_sent_data.decode())
        client_socket.send(server_sent_data)

    print(f'\n[CLIENT] SENT MESSAGE (IP: {client_adress[0]}, PORT: {client_adress[1]})')
    client_sent_data = client_socket.recv(100).decode()
    print(client_sent_data)

    print(f'\n[SERVER] RESPONSE TO [CLIENT] (IP: {client_adress[0]}, PORT: {client_adress[1]})')
    print('Connection closed....')
    client_socket.close()
    server_socket.close()
    quit()

main()