# Your score is 100 / 100
# Examiner's comments Hi David, congratulations on completing the course and submitting the final assignment! From a functional point of view, the code you wrote maintains a proper hanging man game move and copes well with every guess of the player, both in winning games and in losing games. Good job! In terms of design and coding: the code is divided into the mandatory functions according to the exercise instructions. There is a logical division of the code into auxiliary functions. The code is designed in a clear and logical way. In terms of readability and style: you made sure to document all the functions according to the docstring guidelines that were learned in unit 5.4. Documentation is an integral part of quality and professional code. Well done! In terms of proper Python writing: an excellent understanding of the studied material is obtained. magnificent! :) The logic of checking whether it is an alphabetic character that you wrote in the correctness tests function, excellent! But it should be noted that Python has built-in functions for this, for example the isalpha function. In conclusion, there is no doubt that you acquired many tools in Python programming and managed to develop a great hanging man game! Good luck in the future! :)
import time
import os
HANGMAN_PHOTOS = {
    1: """
    x-------x
    """,
    2: """
    x-------x
    |
    |
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}
def welcome_text():
    """
    This function prints out the Welcome text art.
    Arguments: None
    Returns: None
    """
    WELCOME_TEXT_ART = """ 
<Welcome to the game Hangman>
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/  |                      
                   |___ /        
"""
    print(WELCOME_TEXT_ART)

def check_win(secret_word, old_letters_guessed):
    """
    This function checks if the user won the game, this is done by creating a new list named 'right_letters' and 
    appending to it the letters that are found both in 'secret_word' (parameter which represents the secret word the user needs
    to solve) and the 'old_letters_guessed' (parameter which represents the list of letters the user has tried to guess) after that
    the 'right_letters' list gets converted into a string and the length of this string is being compared to the leangth of the 
    'secret_word' parameter if the the leangths match Returns true indicating that the player won the game else Returns false.

    Parameters: 1) parameter which represents the secret word the user needs to solve 2) parameter which represents the 
    list of letters the user has tried to guess
    Parameter-Types: Str, List
    Returns: True/False
    Return-Types: bool
    """
    right_letters= []
    for letter in secret_word:
        if letter in old_letters_guessed:
            right_letters.append(letter)
        else:
            continue
    if len("".join(right_letters)) == len(secret_word):
        return True
    else:
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function checks the user's input to see if the user has already used that charcter before this
    is done by a checking if the 'letter_guessed' parameter is inside the 'old_letters_guessed' parameter.
    Parameters: 1) User's character input. 2) list of all the user's past gusses
    Calls: 'clear_screen'
    Parameter-Types: str, list
    Returns: True/False
    Return-Types: bool
    """
    if letter_guessed not in old_letters_guessed:
        return True
    else:
        clear_screen()
        old_letters_guessed.sort()
        print('X' + '\n' + " -> ".join(old_letters_guessed[:len(old_letters_guessed)]))
        return False

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function Checks the user's input to see if the user has inputted more than one character (if the user
    did use more then one character Returns False), then the function checks the character to see if its not a english character
    (if not Returns False again) if the user's input is one english character returns the value called from the 
    'try_update_letter_guessed' function.

    Calls: 'try_update_letter_guessed'
    Parameters: 1)user's guess input to check 2) A list of the user's old guesses
    Parameter-Types: Str, list
    Returns: True of False
    Return-Type: Bool  
    """
    #checking if user guessed more then one letter
    if len(letter_guessed)>=2:
        print('X')
        print('> Please provide ONE english letter.')
        time.sleep(2)
        clear_screen()
        return False
    # english_char_checker
    else:
        if letter_guessed.isidentifier():
            return try_update_letter_guessed(letter_guessed, old_letters_guessed)
        else:
            print('X')
            print('> Please provide a english letter.')
            time.sleep(2)
            clear_screen()
            return False

def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function returns the display string that represents the the progress of the player in finding the secret word.
    This is done by creating a new list('final_list') iterating over the 'secret_word' parameter and and checking if 
    'the old_letters_guessed' list contains letters from the secret word if a letter is found the function appends 
    it to the 'final_list' if not appends a blank ('_') instead, at the end the function returns a string 
    containing the users progress.

    Parameters: 1) secret word (string). 2) a list containing the letters a user already gussed
    Parameter-Types: str, list
    Returns: A string represanting The users Progress in finding the secret word
    Return-Type: str
    """
    final_list = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            final_list.append(letter)
        else:
            final_list.append("_")
    return " ".join(final_list)

def Choose_word(file_path, index):
    """
    This function reads the inputed file from the user creates a list of all words inside then selects a word from the file based
    on the users index inupt. The function returns the selected word as a string.
    Parameters: 1) file path from the user. 2) index from the user to select a word.

    Parameter-Types: str, int
    Returns: A selected word from the file the user inputed.
    Return-Type: str
    """
    with open(file_path, 'r') as file:
        words_list= file.read().strip().split(' ')
        Word_selected_from_list=  words_list[(index-1) % len(words_list)]
    return Word_selected_from_list

def running_game(max_player_tries):
    """
    This function is the main function that runs and manages the hangman game it recives only one parameter and its 
    the max tries a player can have the function is divided into 2 parts:

    1) The game setup where all the values needed for the game to run are getting created(i.e: file_input_from user which is a 
    variable that takes a path(str) that points to the file containing the words for the game), this part also prints the 
    welcome art.
    2) The game loop this is the game itself, its the main part that calls all the functions and passes them arguments from the 
    setup.

    Calls: 'Choose_word','clear_screen','welcome_text','show_hidden_word','check_win','check_valid_input'
    Parameter: A number which tells the game loop how much times a player is allowed to guess a wrong letter
    Parameter-Type: int
    Returns: None
    """
    welcome_text()
    # Game Setup
    file_input_from_user= input("Please provide a Path to the file containing words: ")
    index_input_from_user= int(input("Please provide a index to select a word: "))
    secret_word= Choose_word(file_input_from_user,index_input_from_user)
    num_of_tries= 0
    old_letters_guessed= []
    print('Loading...')
    time.sleep(2)
    clear_screen()

    # Game loop
    print('> The Game Has Started! Good luck!!')
    while num_of_tries < max_player_tries:
        print(HANGMAN_PHOTOS[num_of_tries+1])
        print(show_hidden_word(secret_word, old_letters_guessed))
        if len(old_letters_guessed)>0:
            print('\n-Letters you guessed-')
            print(' ' + ' -> '.join(old_letters_guessed))
        user_guess= input(f'\nGuess a Letter({max_player_tries-num_of_tries} Tries left!): ')
        # Converting the user's guess from uppercase to lower case to avoid bugs
        user_guess_to_lowercase= user_guess.casefold()
        if check_valid_input(user_guess_to_lowercase, old_letters_guessed):
            old_letters_guessed.append(user_guess_to_lowercase)
            if user_guess_to_lowercase not in secret_word:
                # user failed to guess a letter
                clear_screen()
                print(':(')
                num_of_tries+=1
                continue
            else:
                # user guessed right checking if he won
                if check_win(secret_word,old_letters_guessed):
                    clear_screen()
                    print(HANGMAN_PHOTOS[num_of_tries + 1])
                    print(show_hidden_word(secret_word, old_letters_guessed))
                    print('\n' + """
  _______
 |       |
(|  {#1} |)
 |       |
  \     /
   `---'
   _|_|_
                    """)
                    user_choice =input("\nYOU WIN!! To play agian type 'yes': ")
                    if user_choice == 'yes':
                        main()
                        break
                    else:
                        print('Thank you for playing :-) Closing this game in 3 seconds')
                        time.sleep(3)
                        quit()
                else:
                    # clears the screen after a user gussed right but didn't win.
                    clear_screen()
                    continue
    else:
        # Player lost by exceeding the guess limit
        clear_screen()
        print(HANGMAN_PHOTOS[num_of_tries + 1])
        print(show_hidden_word(secret_word, old_letters_guessed))
        if len(old_letters_guessed)>0:
            print('\n-Letters you guessed-')
            print(' ' + ' -> '.join(old_letters_guessed))
        user_choice =input("\nYOU LOSE... To play agian type 'yes': ")
        if user_choice == 'yes':
            main()
        else:
            print('Thank you for playing :-) Closing this game in 3 seconds')
            time.sleep(3)
            quit()



def clear_screen():
    """
    This funcion clears the screen for aesthetic purposes using the os module.
    Parameters: None
    Returns: None
    """
    os.system('cls')

def main():
    """
    This function does the following:
    1) Clears the screen by calling the 'clear_screen()' function
    2) Calls the function that runs and manages the game 'running_game()' and passes the
       'MAX_TRIES' variable that tells the 'running_game' function how many times the player can
       get eliminated for inputing a wrong letter.
    Calls: 'running_game'
    Parameters: None
    Returns: None
    """
    MAX_TRIES= 6
    clear_screen()
    running_game(MAX_TRIES)

if __name__ == '__main__':
    main()