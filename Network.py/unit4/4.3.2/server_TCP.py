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
msg_to_send = []

while True:
    ready_to_read, ready_to_write, in_err = select.select([server_socket] + client_list, client_list, [])
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
            msg_to_send.append((current_socket, data)) if data != '' else None
    for msg in msg_to_send:
        client_socket, data_on_hold = msg
        if client_socket in ready_to_write:
            try:
                client_socket.send(f'your data here {data_on_hold}'.encode())
                msg_to_send.remove(msg)
            except:
                print('somthing went wrong')