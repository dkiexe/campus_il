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

ADDRESS_SERVER = "127.0.0.1"
PORT = 8828
MAX_MSG_SIZE = 1000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

user_input = input('What would you like to say to the server? ')

client_socket.sendto(user_input.encode(),(ADDRESS_SERVER, PORT))

if user_input == 'EXIT':
    client_socket.close()
    quit()

(res_server, server_ip) = client_socket.recvfrom(MAX_MSG_SIZE)

print("Server sent: "+ res_server.decode())

client_socket.close()