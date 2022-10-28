# So we said we were building an online trivia game, didn't we? Yes! So here we start, and with one of the most important things in the game - the score!
# You already know it - if you answer correctly you get 5 points. If the answer is incorrect then... we will not deduct a score, 
# but make sure that the user does not receive a score for an answer he made a mistake.

# In this exercise you must add additional commands in the protocol to the client code. 
# From now on, each of the functions we implement on the client side will use the helper functions we implemented in the previous exercise build_and_send_message, 
# and recv_message_and_parse to send the messages to the server and receive information back from it.

# And back to the score. The new functions we have to implement are:
# Write a tiny helper function called build_send_recv_parse which will shorten our processes - it will accept a socket, command, and data, 
# and use the send and receive functions that we implemented in the previous section one after the other. 
# The function will return the answer from the server in two strings, msg_code and data.
# Write a function called get_score which accepts a socket and prints the user's current score. 
# Remember that this function should not only send a message to the server but also receive a response. 
# Remember to use the auxiliary function build_send_recv_parse if a bad answer is returned (incorrect msg_code), an error must be printed.
# Write a function called get_highscore which accepts a socket and prints the Highscores table as it comes from the server. 
# Use the helper function build_send_recv_parse.
# Extend main to show the user a choice of what action they want to take - exit, or see what their current score is. 
# As long as the user has not exited, prompt them to perform an action. If the user has selected a particular action, call the appropriate function.

# My solution 
import socket
import chatlib  

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678
logged_in = False

# HELPER SOCKET METHODS

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
1) score        Get your score
2) highscore    Get the highest score
3) quit         Quit
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
				print(
f"""High score tabe: 
{msg}
				""".replace('#', ' '))
	logout(client_socket_object)
	print('Goodbye')
	client_socket_object.close()

if __name__ == '__main__':
	main()
