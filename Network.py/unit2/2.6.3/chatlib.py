# Protocol Constants
CMD_FIELD_LENGTH = 16	# Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4   # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH-1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
"login_msg" : "LOGIN",
"logout_msg" : "LOGOUT",
"score" : "SCORE",
"highscore" : "HIGHSCORE",
"play" : "QUESTION_REQ", # CLIENT inputs 'play' but the server will see a request for a message
"user_answer": "ANSWER",
"users": "GET_LOGGED_USERS"
} # .. Add more commands if needed


PROTOCOL_SERVER = {
"login_ok_msg" : "LOGIN_OK",
"login_failed_msg" : "ERROR",
"score_res" : "SCORE",
"highscore_res": "HIGHSCORE",
"choice_err": "ERROR",
"out_of_quastions": 'ERROR_OUT_OF_QUASTIONS',
"question_res": "QUESTION_RES",
"answer_correct": "ANSWER_CORRECT",
"answer_wrong": "ANSWER_WRONG",
"logged_list": "LOGGED_USERS"	
} # ..  Add more commands if needed


# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
	"""
	Gets command name (str) and data field (str) and creates a valid protocol message
	Returns: str, or None if error occured
	"""
	if cmd in PROTOCOL_CLIENT.values() or cmd in PROTOCOL_SERVER.values():
		while len(cmd) < CMD_FIELD_LENGTH:
			cmd += ' '
		sum_of_msg_chars_list= [char for char in str(len(data))]
		while len(sum_of_msg_chars_list) < LENGTH_FIELD_LENGTH:
			sum_of_msg_chars_list.insert(0, '0')
		return cmd + DELIMITER + "".join(sum_of_msg_chars_list) + DELIMITER + join_data(data.split(' '))
	else:
		return ERROR_RETURN 


def parse_message(input_to_parse):
	"""
	Parses protocol message and returns command name and data field
	Returns: cmd (str), data (str). If some error occured, returns None, None
	"""
	num_of_deli= input_to_parse.count(DELIMITER)
	if num_of_deli != 2:
		return None, None
	raw_input_list = input_to_parse.split(DELIMITER)
	if '\t' in raw_input_list[1] or '\n' in raw_input_list[1]:
		return None,None
	if len(raw_input_list[0]) > 16 or len(raw_input_list[1]) > LENGTH_FIELD_LENGTH or len(raw_input_list[2]) > MAX_DATA_LENGTH:
		return None,None
	if not raw_input_list[1].strip().isnumeric():
		return None, None
	cmd_from_input = "".join([char for char in raw_input_list[0] if char != ' '])
	msg_from_input = raw_input_list[2]
	return cmd_from_input, msg_from_input

	
def split_data(msg, expected_fields):
	"""
	Helper method. gets a string and number of expected fields in it. Splits the string 
	using protocol's data field delimiter (|#) and validates that there are correct number of fields.
	Returns: list of fields if all ok. If some error occured, returns None"""
	msg_list= msg.split('#' if '#' in msg else '|')
	if len(msg_list) > expected_fields or len(msg_list) < expected_fields:
		return None
	else:
		return msg_list


def join_data(msg_fields):
	"""
	Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter. 
	Returns: string that looks like cell1#cell2#cell3
	"""
	return DATA_DELIMITER.join(msg_fields)