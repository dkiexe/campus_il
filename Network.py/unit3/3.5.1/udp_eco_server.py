# Using a UDP client and server for multi-message communication.

# In this exercise we will upgrade the server and the client that we learned about in this chapter, 
# so that the communication will allow the client to send many messages to the server, and not just one message after which the socket is closed. To do this, 
# of course, we also need a condition that will stop the sending, so we will make the following changes:
# 1) We will ask the user to enter information, so that each time the client will send a different message to the server, depending on what the user entered.
# 2) The server will listen to the client's messages in an infinite loop.
# 3) When the user enters "EXIT" the client will forward the message to the server and close the socket.
# 4) Receiving the "EXIT" message on the server side will take it out of the infinite loop and it will also close the socket.

# My solution
import socket

SERVER_IP = "0.0.0.0"
PORT = 8828
MAX_MSG_SIZE = 1000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, PORT))
print('Server running')

while True:
    (client_msg, client_adress) = server_socket.recvfrom(MAX_MSG_SIZE)
    print(f'Client sent this {client_msg.decode()}')
    if client_msg.decode() == 'EXIT':
        print('Closing server...')
        break
    server_socket.sendto('Hello '.encode()+client_msg, client_adress)

server_socket.close()