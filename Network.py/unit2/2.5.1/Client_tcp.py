# Shout server drill
# You must implement the "Scream" server. 
# This is a server that receives a message and "shouts" it back, 
# that is, returns the message it received in capital letters and at the end 3 exclamation marks.

# Guidelines:
# Write the server so that it receives a message and returns it in capital letters with 3 exclamation points at the end. 
# For this purpose, be based on the echo server code that you implemented in the unit.
# Write a client that will contact the server and print the received answer (you can use the client you wrote in the unit without changes).
# Highlights:
# Run the server and the client you wrote locally on your computer, and check that the communication works properly. 
# Remember to run the server first and only then the client.

# My solution(client)
import socket as socket_module

server_adress = ("127.0.0.1", 8858)

client_socket = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_STREAM)

client_socket.connect(server_adress)

data_from_server = ''

while data_from_server != 'QUIT!!!':
    socket_input = input('> Type somthing: ').encode()
    if len(socket_input) > 0:
        client_socket.send(socket_input)
    else:
        continue
    data_from_server = client_socket.recv(100).decode()
    print(f'\n> Server screamed: {data_from_server}\n')

client_socket.close()