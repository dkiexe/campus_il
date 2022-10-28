# In Chapter 2 of the rolling exercise we will write the client for our online trivia game.
# Now that we have a code called chatlib.py, we can use the functions we wrote in our client code, 
# and implement the client side of the online trivia game.

# For testing purposes, you will receive a ready server (server.pyc) which you can run.

# How do you play trivia? Wait... before we run into the game itself - we need to connect to the system first. 
# That is, that our system will know how to identify different users, keep a score for them, know how to name them in the score table, 
# and much more. In this part of the exercise we will do everything related to connecting and identifying with the server.


# Create a new file named client.py.

# You must define the following functions:
# The function [connect] which performs a connection to the IP and port which are kept as constants at the beginning of the file, 
# and returns a socket which is connected to the server. This function is responsible for establishing the connection between 
# the server and the client according to the steps taught in the study unit. 
# The socket returned from this function will be used by us later - through it we will send and receive all the messages in the protocol.
# 
# The [error_and_exit] function which accepts a string to print, and uses Python's built-in exit command to exit*. 
# This function is convenient to end the running of the program in case of problems. 
# For example, we will call this function if we received an unknown error from the server.
# 
# The function [recv_message_and_parse] which receives an open socket (the same socket returned from the connect function), 
# requests information from it with the help of the recv function, 
# and returns a pair of strings: - msg_code - the command received from the server, 
# msg - the message received from the server**. As part of this function, 
# we will call the parse_message helper function that we wrote in the chatlib library.
# 
# The function [build_and_send_message] which receives an open socket, 
# a string with the name of the command and a string with data, 
# creates a ready protocol message with the help of the functions we implemented in chatlib, 
# and then sends it to the server through the socket. Here too, a debug print must be made with the details of the information sent.
# So far we have implemented auxiliary functions that will help in managing the communication with the server. 
# The following functions we will write will already be part of the protocol we chose, 
# it's time to remember the documentation file of the protocol. 
# 
# After that, implement the following functions:
# The [login] function, which receives a socket, and connects to the server.
#  Not to be confused with the connect function, which only establishes a physical communication pipe. 
# The login function, on the other hand, allows the user to log into his account using a username and password.
#  To connect to the server, the function must run in a loop that repeats as long as the login is unsuccessful. 
# The function will work according to the following steps:
# The function will request a username and password from the program operator
# The function creates and sends a login command according to the protocol using the build_and_send_message function. 
# Note that to create the protocol messages you must use the constants that define the protocol messages in chatlib.
# The function will receive a response from the server by the [recv_message_and_parse] function, 
# and will check whether the login was successful or failed according to the type of message returned (command). 
# The program will print to the user whether the login was successful or failed. 
# If the login was successful, you can execute a return to end the loop and the function.
# The function does not return a value, but it does not end until a successful login has taken place.
# 
# The [logout] function, which accepts a socket. 
# The function sends a logout command according to the protocol using the build_and_send_message function.
# The main function - the main function from which we will manage the game and call the other functions in the correct order. 
# First, we'll want the function to establish a physical connection to the server. After that, send a login command, 
# and finally a logout command. In the end, the socket object will be closed.
# Please note - right now our server does nothing but connect and disconnect. 
# After we make sure that these actions occur properly, we will continue to add commands that our client will support.
# The function is a substitute for the use of exception mechanisms in Python which are not required in this course.

# My solution
import socket
import chatlib  

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678

# HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
	"""
	Builds a new message using chatlib, wanted code and message. 
	Prints debug info, then sends it to the given socket.
	Paramaters: conn (socket object), code (str), data (str)
	Returns: Nothing
	"""
	try:
		built_message = chatlib.build_message(code, data)
		conn.send(built_message.encode())
	except Exception as e:
		print(f'{e} was was raised!')
		quit()

def recv_message_and_parse(conn):
	"""
	Recieves a new message from given socket,
	then parses the message using chatlib.
	Paramaters: conn (socket object)
	Returns: cmd (str) and data (str) of the received message. 
	If error occured, will return None, None
	"""
	full_msg = conn.recv(100).decode()	
	cmd, data = chatlib.parse_message(full_msg)
	return cmd, data


def connect():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((SERVER_IP, SERVER_PORT))
	return client_socket


def error_and_exit(error_msg):
	print(f'Server Responded with: {error_msg}')
	quit()


def login(conn):
	while True:
		username = input("Please enter username: \n")
		password = input("Please enter password: \n")
		build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"],f"{username} {password}")
		(command, msg) = recv_message_and_parse(conn)
		if command == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
			print('Logged in!')
			break
		else:
			print(f'Login unsucssesful. Server response: {command} => {msg}')
	return

def logout(conn):
	build_and_send_message(conn, chatlib.PROTOCOL_CLIENT['logout_msg'],"")
	return 

def main():
	client_socket_object = connect()
	login(client_socket_object)
	logout(client_socket_object)
	print('Goodbye')
	client_socket_object.close()

if __name__ == '__main__':
	main()
