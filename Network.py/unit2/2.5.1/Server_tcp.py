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

# MY SOLUTION!!!(server)
import socket as socket_module

server_socket = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 8858))

server_socket.listen()
print('> Server Created awaiting connection')

(client_socket, client_adress) = server_socket.accept()

print(f'> New connection IP:{client_adress[0]}')

user_message = ''

while user_message != 'kill server':
    # checking if the client_socket is closed
    if client_socket.fileno() == -1:
        (client_socket, client_adress) = server_socket.accept()
        print(f'> New connection IP:{client_adress[0]}')
    user_message = client_socket.recv(100).decode()
    client_socket.send(f'{user_message.upper()}!!!'.encode())
    if user_message == 'quit':
        print(f'> Client of IP: {client_adress[0]} Disconnected!')
        client_socket.close()

print('> server closed by client')
client_socket.close()
server_socket.close()