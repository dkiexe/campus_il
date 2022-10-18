# Create a dictionary with a name of your choice and initialize it according to the following table:

# first_name| Mariah 
# last_name | Carey 
# birth_date| 27.03.1970 (string) 
# hobbies   | Sing, Compose, Act (list)

# Write a program that performs the following actions, depending on the digit that the user pressed:

# Print Maria's last name to the screen.
# Print to the screen the month in which Maria was born.
# Print to the screen the number of hobbies Maria has.
# Print to the screen the last hobby in Maria's list of hobbies.
# Add the hobby "Cooking" to the end of the list of hobbies.
# Turn the date of birth type into a tuple that includes 3 numbers (day, month and year - from left to right) and print it.
# Add a new key called age which includes Maria's age and present it.

# Guidelines
# Ask the user to enter an input (a number between 1 and 7) and assume that the input is correct.
def person_func(input):
    special_person={
        "first_name": "Mariah",
        "last_name": "Carey",
        "birth_date": "27.03.1970",
        "hobbies": ['Sing', 'Compose', 'Act']
    }
    if input == '1':
        print(special_person["last_name"])
    elif input == '2':
        print(special_person["birth_date"][3:5])
    elif input == '3':
        print(len(special_person["hobbies"]))
    elif input == '4':
        print(special_person["hobbies"][len(special_person["hobbies"])-1:])
    elif input == '5':
        special_person["hobbies"].append("cooking")
    elif input == '6':
        new_list_for_dates= special_person["birth_date"].split('.')
        new_list_for_dates_nums= [int(x) for x in new_list_for_dates]
        new_list_for_dates_nums= tuple(new_list_for_dates_nums)
        special_person["birth_date"]= new_list_for_dates_nums
        print(special_person["birth_date"])
    elif input == '7':
        current_year= 2022
        print(current_year-int(special_person["birth_date"][6:]))


inp= input('Your option (1-7)> ')
person_func(inp)