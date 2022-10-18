# Write a program that accepts a date from the user in the format dd/mm/yyyy and prints the day of the week for the entered date.

#example:
# >>> Enter a date: 01/01/2000
# Saturday
# >>> Enter a date: 27/11/2051
# Monday

# Directions: Look for documentation about the calendar library and the weekday function.

#My solution
import calendar

user_input= input("Enter a date: ")
seperator_day= 2
seperator_month= 5
day_in_num= calendar.weekday(int(user_input[seperator_month+1:]),int(user_input[seperator_day+1:seperator_month]),int(user_input[0:seperator_day]))
if day_in_num==0:
    print('Monday')
elif day_in_num==1:
    print('Tuesday')
elif day_in_num==2:
    print('Wednesday')
elif day_in_num==3:
    print('Thursday')
elif day_in_num==4:
    print('Friday')
elif day_in_num==5:
    print('Saturday')
elif day_in_num==6:
    print('Sunday')