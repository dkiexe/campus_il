# Exercise: Basic command server (running the client against the server on a local computer)
# In the previous chapter we learned how to write a simple protocol for sending messages between a server and a client,
# but the communication between them does not produce a successful relationship - the server always returns the information sent by the client as it is. 
# Let's spice things up.

# You must write a client-server system, where the server executes commands that the client sends to it and returns an answer to the client accordingly. 
# Below is the list of requests that must be supported:

# NAME – server name request. The server must respond with a string representing its name. The name can be any string you choose.
# TIME – current time request. The server must respond with a string that includes the current time. Use the time library built into Python.
# RAND – random number request. The server must respond with a random number ranging from 1 to 10. Use the random library built into Python.

# The length of the response can be different depending on the request.

# As we have seen, the communication between the server and the client should continue as long as the user has not entered a "Quit" message which causes a disconnection.

# Instructions for the exercise
# Before you start writing the code, do a preliminary planning: think about exactly what you will implement on the client side and what on the server side, 
# and try to anticipate problems you will encounter.

# On the client side - first, you must ask the user to choose one of the commands specified in the chapter (hint: use the input function). 
# Then, send the request to the server, receive the response and display it to the user.

# On the server side - you must receive a connection from the client, understand his request and respond to it accordingly.

# My solution(server)
import time 
import random
import os
import socket as socket_module

SERVER_NAME = "DAVID's Cool server ;)"

server_socket = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8850))
server_socket.listen()
print('> Server created! listning....')
(client_socket, client_adress) = server_socket.accept()

data_from_client = ''

while data_from_client != 'shut_down':
    # Checking if client connected
    if client_socket.fileno() == -1:
        # Awaiting new client
        (client_socket, client_adress) = server_socket.accept()
    data_from_client = client_socket.recv(100).decode()
    if data_from_client == 'name_plz':
        client_socket.send(SERVER_NAME.encode())
    elif data_from_client == 'time_plz':
        raw_time_obj = time.localtime()
        time_representation = time.strftime("%D %H:%M:%S", raw_time_obj)
        client_socket.send(time_representation.encode())
    elif data_from_client == 'random_num':
        client_socket.send(str(random.choice(range(10))).encode())
    elif data_from_client == 'quit':
        client_socket.send(b"goodbye!")
        client_socket.close()
    else:
        client_socket.send('ERR'.encode())

print('Server shuting down....')
client_socket.close()
server_socket.close()