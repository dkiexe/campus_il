import socket 
import select

SERVER_IP = "0.0.0.0"
PORT = 5555
MAX_MSG_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, PORT))
server_socket.listen()
print('server running')

client_list = []

while True:
    ready_to_read, ready_to_write, in_err = select.select([server_socket] + client_list, [], [])
    for current_socket in ready_to_read:
        if current_socket == server_socket:
            (client_socket, client_address) = server_socket.accept()
            print(f'New clitent connected {client_address}')
            client_list.append(client_socket)
        else:
            print('New data from client')
            data = current_socket.recv(MAX_MSG_SIZE).decode()
            if data == '':
                print('Disconnecting client')
                client_list.remove(current_socket)
                current_socket.close()
            else:
                print(current_socket.getpeername())
                current_socket.send(f'your data is: {data}'.encode())