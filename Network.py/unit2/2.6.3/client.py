# The users have logged into the system, we already have a score. what is missing? Need some questions. Trivia after all...
# There will still be time to get out of your head all the special details that only you know
#  (or use the questions that other learners will share), 
# but before that - you need to ask the server for information and present it: you need questions,
#  and also see which users are connected.


#  So let's start doing that by adding some new functions:
# Write a function called play_question which accepts a socket as a parameter. 
# The function must perform the actions in the following order:
# ask a question from the server (remember that the server can also tell you that the questions are over, 
# and you should prepare for such a situation)
# Print the question to the user
# Ask the user for the answer he thinks is correct
# Send the answer the user entered to the server
# Receive feedback from the server as to whether the answer the user chose is correct or incorrect, 
# and print the correct answer. Remember that in the case of a wrong answer, 
# the server announces (according to the protocol) what the correct answer is.
# The function should not return a return value. If there is any problem, 
# the function will simply print an error and stop with return. Use the helper function build_send_recv_parse.
# Write a function called get_logged_users which accepts a socket and prints the list of all users currently connected to the server.

# My solution 
import socket
import chatlib
import os  

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678
logged_in = False

# HELPER SOCKET METHODS
def clear():
	"""
	This function clears the screen using the os module
	Arguments: None
	Returns: None
	"""
	os.system('cls')

def build_send_recv_parse(conn, code, data):
	"""
	This function works in 2 ways:
	1)
		Builds a new message using chatlib, wanted code and message. 
		Prints debug info, then sends it to the given socket.
		Paramaters: conn (socket object), code (str), data (str)
		Returns: Nothing
	2)
		Recieves a new message from given socket,
		then parses the message using chatlib.
		Paramaters: conn (socket object)
		Returns: cmd (str) and data (str) of the received message. 
		If error occured, will return None, None
	"""
	try:
		built_message = chatlib.build_message(code, data)
		conn.send(built_message.encode())
	except Exception as e:
		print(f'{e} was was raised!')
		quit()
	full_msg = conn.recv(1000).decode()	
	cmd, data = chatlib.parse_message(full_msg)
	return cmd, data

def play_question(conn):
	# sending question request to server.
	(cmd, message) = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["play"], "")
	if cmd == 'ERROR_OUT_OF_QUASTIONS':
		print(f'Server responded with {cmd}=> {message} [ Please come back another time ;) ]')
		return 'ERR'
	filter_list = ['(',')',"'"]
	list_of_message = ("".join(list(filter(lambda char: True if char not in filter_list else False, message)))).replace('#', ' ')
	list_of_message = list_of_message.split(',')
	message_question, message_options = (list_of_message[0], list_of_message[1])
	print(f'(Q) Your question is: {message_question}')
	for num, elem in enumerate(message_options.split('/'), 1):
		if num == 1:
			print(f'is it:\n{num}) {elem}')
			continue
		print(f'{num}) {elem}')
	user_answer = input('Type answer here (txt only!):')
	# sending user answer to server.
	(cmd, message) = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["user_answer"], user_answer)
	if cmd == 'ANSWER_CORRECT':
		print('\n CORRECT!')
		return
	elif cmd == 'ANSWER_WRONG':
		print(f'\n You are wrong the right answer is: {message.replace("#", " ")}')
		print("")

def get_logged_users(conn):
	(cmd, message) = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["users"], "")
	if cmd == "ERROR":
		error_and_exit(message)
	print(f'here is a list of all logged users <{message.replace("#", " ")}>')

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
		(command, msg) = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["login_msg"],f"{username} {password}")
		if command == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
			print('Logged in!')
			break
		else:
			print(f'Login unsucssesful. Server response: {command} => {msg}')
	return

def logout(conn):
	build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT['logout_msg'],"")
	return

def main():
	global logged_in
	while True:
		if logged_in == False:
			client_socket_object = connect()
			login(client_socket_object)
			logged_in = True
		user_choice = input("""
	    |MENU|
1) play         Play a trivia question
2) score        Get your score
3) highscore    Get the highest score
4) users        Get all the users logged in
4) quit         Quit
Please enter your choice: 
		""")
		if user_choice == "quit":
			break
		if user_choice not in chatlib.PROTOCOL_CLIENT.keys():
			print(f'Choice ERROR.')
			continue
		match user_choice:
			case "score":
				(command, msg) = build_send_recv_parse(client_socket_object, chatlib.PROTOCOL_CLIENT[user_choice],"")
				if command == 'ERROR':
					print(f'Choice ERROR. Server response: {command} => {msg}')
					continue
				print(f'Your score is {msg}')
			case "highscore":
				(command, msg) = build_send_recv_parse(client_socket_object, chatlib.PROTOCOL_CLIENT[user_choice],"")
				print(f"High score tabe: \n{msg}".replace('#', ' '))
			case "play":
				play_question(client_socket_object)
			case "users":
				get_logged_users(client_socket_object)
	logout(client_socket_object)
	print('Goodbye')
	client_socket_object.close()

if __name__ == '__main__':
	clear()
	main()
