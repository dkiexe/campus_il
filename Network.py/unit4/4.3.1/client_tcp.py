import socket 

SERVER_IP = "127.0.0.1"
PORT = 5555
MAX_MSG_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, PORT))
while True:
    user_inp = input('Type here> ')
    client_socket.send(user_inp.encode())
    data_from_server = client_socket.recv(MAX_MSG_SIZE).decode()
    print(data_from_server)