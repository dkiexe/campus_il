##############################################################################
# server.py
##############################################################################

import socket
import chatlib
import select
import random
import requests

# GLOBALS
users = {}
questions = {}
logged_users = {} # a dictionary of client hostnames to usernames - will be used later

ERROR_MSG = "Error! "
SERVER_PORT = 5678
SERVER_IP = "127.0.0.1"

client_socket_list = []
messages_to_send = []

# HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
	global messages_to_send
	"""
	Builds a new message using chatlib, wanted code and message. 
	Prints debug info, then sends it to the given socket.
	Paramaters: conn (socket object), code (str), data (str)
	Returns: Nothing
	"""
	try:
		built_message = chatlib.build_message(code, data)
		messages_to_send.append((conn, built_message))
		print("[SERVER] ", built_message) # Debug print
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
	try:
		full_msg = conn.recv(1024).decode()
	except:
		return 'None', '#'
	cmd, data = chatlib.parse_message(full_msg)
	print("[CLIENT] ",full_msg)	  # Debug print
	return cmd, data


# Data Loaders #

def load_questions():
	"""
	Loads questions bank from https://opentdb.com/api.php?amount=50&type=multiple (50 at a time.)
	Recieves: -
	Returns: questions dictionary
	"""
	url = 'https://opentdb.com/api.php?amount=50&type=multiple'
	r = requests.get(url)
	if r.status_code == 200: #status code 200 (hopefully)
		all_questions_dict = r.json()["results"]
		enumerated_questions_dict = {}
		for index, pair in enumerate(all_questions_dict):
			enumerated_questions_dict[index] = pair
		return enumerated_questions_dict
	else:
		print(f'[SERVER]!! Server couldnt start since no questions were able to be loaded HTTP ERR CODE {r.status_code}')
		quit()

def load_user_database():
	"""
	Loads users list from file	## FILE SUPPORT TO BE ADDED LATER
	Recieves: -
	Returns: user dictionary
	"""
	users = {
			"test"		:	{"password":"test","score":0,"questions_asked":[]},
			"yossi"		:	{"password":"123","score":50,"questions_asked":[]},
			"master"	:	{"password":"master","score":200,"questions_asked":[]}
			}
	return users

# SOCKET CREATOR

def setup_socket():
	"""
	Creates new listening socket and returns it
	Recieves: -
	Returns: the socket object
	"""
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((SERVER_IP, SERVER_PORT))
	sock.listen()
	return sock


def send_error(conn, error_msg):
	"""
	Send error message with given message
	Recieves: socket, message error string from called function
	Returns: None
	"""
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER['err_msg'], error_msg)

def create_random_question():
	select_question_number = random.choice(list(questions.keys()))
	all_answer_options = [questions[select_question_number]["correct_answer"]] + questions[select_question_number]['incorrect_answers']
	random.shuffle(all_answer_options)
	return str(select_question_number) + '#' + questions[select_question_number]["question"] + ('#'.join(all_answer_options).replace(' ', '_')).replace('&quot;', ' ')


##### MESSAGE HANDLING
def handle_question_message(conn):
	"""
	This function calls the 'create_random_question()' function to get a string of a random message and sends it to the client
	using the 'build_and_send_message()' function.
	Recives: socket object of a client
	Returns: None
	"""
	user_question = create_random_question()
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER["question_res"], user_question)

def handle_answer_message(conn, user_msg):
	question_id, user_answer = user_msg.split('/')
	question_id = int(question_id)
	if questions[question_id]["correct_answer"].lower() == user_answer.lower().replace('#', ' '):
		username = logged_users[conn.getpeername()]
		users[username]['score'] += 5 # adding 5 points per right answer
		build_and_send_message(conn, chatlib.PROTOCOL_SERVER['answer_correct'], '') # sending the user that he is right on his answer
	else:
		build_and_send_message(conn, chatlib.PROTOCOL_SERVER["answer_wrong"], str(questions[question_id]["correct_answer"])) # sending incorrect answer for wrong answer

def handle_logged_message(conn):
	logged_users_msg = "#".join([user for user in logged_users.values()])
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER["logged_list"], logged_users_msg)

def handle_highscore_message(conn):
	high_score_msg = "#".join([f"{user}:" + str(users[user]["score"]) for user in users.keys()])
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER["highscore_res"], high_score_msg)



def handle_getscore_message(conn, username):
	global users
	score = str(users[username]["score"])
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER["score_res"], score)


def handle_logout_message(conn):
	"""
	Closes the given socket (in laster chapters, also remove user from logged_users dictioary)
	Recieves: socket
	Returns: None
	"""
	global logged_users
	global client_socket_list
	del logged_users[conn.getpeername()]
	client_socket_list.remove(conn)
	conn.close()


def handle_login_message(conn, data):
	"""
	Gets socket and message data of login message. Checks  user and pass exists and match.
	If not - sends error and finished. If all ok, sends OK message and adds user and address to logged_users
	Recieves: socket, message code and data
	Returns: None (sends answer to client)
	"""
	global users  # This is needed to access the same users dictionary from all functions
	global logged_users	 # To be used later
	username = data.split('#')[0]
	password = data.split('#')[1]
	if username in users.keys():
		if users[username]['password'] == password:
			users[username] = {'password': password, 'score': 0, 'questions_asked': []}
			logged_users[conn.getpeername()] = username
			build_and_send_message(conn, chatlib.PROTOCOL_SERVER["login_ok_msg"], "")
		else:
			send_error(conn, "Wrong password.")
	else:
		send_error(conn, "Unable to find username.")


def handle_client_message(conn, cmd, data):
	"""
	Gets message code and data and calls the right function to handle command
	Recieves: socket, message code and data
	Returns: None
	"""
	global logged_users	 # To be used later
	if cmd == chatlib.PROTOCOL_CLIENT['login_msg']:
		handle_login_message(conn, data)
	elif cmd == chatlib.PROTOCOL_CLIENT['logout_msg'] and conn.getpeername() in logged_users.keys():
		handle_logout_message(conn)
	elif cmd == chatlib.PROTOCOL_CLIENT['score'] and conn.getpeername() in logged_users.keys():
		handle_getscore_message(conn, data)
	elif cmd == chatlib.PROTOCOL_CLIENT['highscore'] and conn.getpeername() in logged_users.keys():
		handle_highscore_message(conn)
	elif cmd == chatlib.PROTOCOL_CLIENT['users'] and conn.getpeername() in logged_users.keys():
		handle_logged_message(conn)
	elif cmd == chatlib.PROTOCOL_CLIENT['play'] and conn.getpeername() in logged_users.keys():
		handle_question_message(conn)
	elif cmd == chatlib.PROTOCOL_CLIENT['user_answer'] and conn.getpeername() in logged_users.keys():
		handle_answer_message(conn, data)
	else:
		build_and_send_message(conn, chatlib.PROTOCOL_SERVER['err_msg'], 'Non valid choice.')


def main():
	# Initializes global users and questions dicionaries using load functions, will be used later
	global users
	global questions
	global messages_to_send
	users = load_user_database()
	questions = load_questions()
	print("Welcome to Trivia Server!")
	server_socket = setup_socket()
	while True:
		ready_to_read, ready_to_write, in_err = select.select(
			[server_socket] + client_socket_list,
			client_socket_list,
			[]
		)
		for current_socket in ready_to_read:
			if current_socket == server_socket:
				(client_socket, client_address) = server_socket.accept()
				print(f'[SERVER] New connection from: {client_address[0]}')
				client_socket_list.append(client_socket)
			else:
				cmd ,data = recv_message_and_parse(current_socket)
				if data == '#' or data == None:
					handle_client_message(current_socket, 'LOGOUT', '')
				else:
					handle_client_message(current_socket, cmd, data)
			for msg in messages_to_send:
				the_socket_obj, data_to_send = msg # connected_socket => client socket
				if the_socket_obj in ready_to_write:
					try:
						the_socket_obj.send(data_to_send.encode())
						messages_to_send.remove(msg)
					except Exception as err:
						print('[SERVER]!! SOMTHING WENT WRONG BUT SERVER IS STILL RUNNING...')



if __name__ == '__main__':
	main()
