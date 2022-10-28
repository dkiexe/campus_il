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

# My solution(client)
import os
import time
import socket as socket_module

server = ("127.0.0.1", 8850)

def clear():
    os.system('cls')

client_socket = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_STREAM)
client_socket.connect(server)
server_response = ''
possible_commands= ['name_plz', 'time_plz', 'random_num', 'quit', 'shut_down']

while server_response != 'goodbye!':
    selected_command = input("""
Select command option:
1) name_plz
2) time_plz
3) random_nun
4) quit     
    """)
    if selected_command.casefold() not in possible_commands:
        continue
    client_socket.send(selected_command.encode())
    server_response = client_socket.recv(100).decode()
    if server_response == 'ERR':
        print('> Server errored from the request!')
        continue
    print(f'> Server response to {selected_command} is : {server_response}')
    time.sleep(2)
    clear()