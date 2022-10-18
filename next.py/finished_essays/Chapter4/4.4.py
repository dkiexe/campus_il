# You must write a program that knows how to generate dates and times from a certain date to infinity. 
# You will write the plan step by step until you reach a complete plan. Follow the instructions in the following sections.

# Write a function called gen_secs that returns a generator that produces all possible seconds ranges (numbers between 0 and 59).

# def gen_secs():
# Write a function called gen_minutes that returns a generator that produces all possible minute ranges (numbers between 0 and 59).

# def gen_minutes():
# Write a function called gen_hours that returns a generator that produces all possible hour ranges (numbers between 0 and 23).

# def gen_hours():
# Realize a generator function called gen_time.
# The generator must generate all possible hours of the day starting at 00:00:00.
# The generator function must use the gen_secs, gen_minutes, and gen_hours generators to print the time in the following format: 01:23:45.

# Guidelines:

# You can use the following format for the printing operation - "%02d:%02d:%02d" (string format).
# Check that the generator function you wrote works using a for loop that will print the following time each time:

# To view an accessible code snippet
# for gt in gen_time():
#     print(gt)
# Note: The output is partial of course.

# Write a generator function named gen_years defined as follows:

# def gen_years(start=2019):
#     #<yield>
# The generator function receives as a parameter a number representing a year (with a default value of the current year), 
# and produces the year received as a parameter and all the years from it onwards.

# Write a function called gen_months defined as follows:

# def gen_months():
# The function returns a generator that produces all the numbers of the months of the year (numbers in the range 1 to 12).

# Write a function called gen_days defined as follows:

# def gen_days(month, leap_year=True):
# The function accepts as parameters an integer representing a month number and a Boolean variable representing whether it is a leap year or not.

# The function returns a generator that produces the number of days in that month (depending on the month and the data regarding a leap year or not).

# You can use the following sources, for the number of days in each month and leap years:

# https://www.mathsisfun.com/measure/months.html
# https://www.mathsisfun.com/leap-years.html
# It's time to combine all the code we've written so far!

# Write a generator function named gen_date defined as follows:

# def gen_date():
#     #<yield>
# The generator returned from the function must produce a complete date signature, in the following format:

# dd/mm/yyyy hh:mm:ss.

# For the purpose of the task, of course you must use the generators you have already created. Remember to check whether a year is a leap year or not.

# Below is an example of a partial run (which includes printing the values ​​extracted from the generator):

# 01/01/2019 00:00:00
# 01/01/2019 00:00:01
# 01/01/2019 00:00:02
# Note: The output is of course partial (this is just the beginning of it).

# Call the next function in a loop for the generator object that is returned from the gen_date generator function and print the value produced from the generator after every 1000000 iterations.

# Below is a sample run:

# 12/01/2019 13:46:40
# 24/01/2019 03:33:20
# 04/02/2019 17:20:00
# Note: The output is of course partial (this is just the beginning of it).


# My solution 
import os,time
clear= lambda: os.system('cls')
clear()


def gen_secs():
    pos_second= -1
    while True:
        switched= False
        pos_second +=1
        if pos_second > 59:
            pos_second= 0
            switched= True
        yield [pos_second,switched]
def gen_mins():
    pos_min= -1
    while True:
        switched= False
        pos_min +=1
        if pos_min > 59:
            pos_min= 0
            switched= True
        yield [pos_min,switched]
def gen_hours():
    pos_hour= -1
    is_looped= False
    while True:
        is_looped= False
        pos_hour +=1
        if pos_hour > 23:
            pos_hour= 0
            is_looped= True
        yield [pos_hour,is_looped]

def num_orgenizer(input_of_nums):
    return '0'+str(input_of_nums) if len(str(input_of_nums))<2 else input_of_nums

def gen_time():
    #time format: ([0, False], [0, False], [1, False])
    seconds= gen_secs()
    minutes= gen_mins()
    hours= gen_hours()
    min_update= next(minutes)
    hours_update= next(hours)
    yield [hours_update,min_update,next(seconds)]
    while True:
        seconds_update= next(seconds)
        if seconds_update[1] == True:
            min_update= next(minutes)
            seconds_update[1]= False
        if min_update[1] == True:
            hours_update= next(hours)
            min_update[1] = False
        yield [hours_update,min_update,seconds_update]

def gen_years(start=2022):
    leap_year_counter= 2
    yield [start,False]
    while True:
        leap_year_counter+=1
        if leap_year_counter==4:
            yield [start+1,True]
        yield [start+1, False]

def gen_months():
    pos_month= 1
    is_looped= False
    yield [pos_month,is_looped]
    while True:
        is_looped= False
        pos_month+=1
        if pos_month > 12:
            pos_month= 1
            is_looped= True
        yield [pos_month, is_looped]

def gen_days(month, leap_year=True):
    is_looped= False
    while True:
        is_looped= False
        if leap_year:
            if month in (1,3,5,7,8,10,12):
                for day in range(1,33):
                    if day > 31:
                        day= 1
                        is_looped= True
                    yield [day,is_looped]
            elif month in (4,6,9,11):
                for day in range(1,32):
                    if day > 30:
                        day= 1
                        is_looped= True
                    yield [day,is_looped]
            else:
                for day in range(1,31):
                    if day > 29:
                        day= 1
                        is_looped= True
                    yield [day,is_looped]
        else:
            if month in (1,3,5,7,8,10,12):
                for day in range(1,33):
                    if day > 31:
                        day= 1
                        is_looped= True
                    yield [day,is_looped]
            elif month in (4,6,9,11):
                for day in range(1,32):
                    if day > 30:
                        day= 1
                        is_looped= True
                    yield [day,is_looped]
            else:
                for day in range(1,30):
                    if day > 28:
                        day= 1
                        is_looped= True
                    yield [day,is_looped]

def gen_date():
    #time format: ([0, False], [0, False], [1, False])
    year_reciver= gen_years()
    month_reciver= gen_months()
    day_reciver= gen_days(1,False)
    time_reciver= gen_time()
    year_update= next(year_reciver)
    month_update= next(month_reciver)
    time_update= next(time_reciver)
    day_update= next(day_reciver)
    yield f"{num_orgenizer(day_update[0])}/{num_orgenizer(month_update[0])}/{num_orgenizer(year_update[0])} {num_orgenizer(time_update[0][0])}:{num_orgenizer(time_update[1][0])}:{num_orgenizer(time_update[2][0])}"
    while True:
        time_update= next(time_reciver)
        if time_update[0][1] == True:
            time_update[0][1]= False
            day_update= next(day_reciver)
        if day_update[1]== True:
            day_update[1]= False
            month_update= next(month_reciver)
        if month_update[1]== True:
            month_update[1]= False
            year_update= next(year_reciver)
        if year_update[1]== True:
            day_reciver= gen_days(month_update, year_update[1])
            year_update[1]= False
        yield f"{num_orgenizer(day_update[0])}/{num_orgenizer(month_update[0])}/{num_orgenizer(year_update[0])} {num_orgenizer(time_update[0][0])}:{num_orgenizer(time_update[1][0])}:{num_orgenizer(time_update[2][0])}"

for x in gen_date():
    time.sleep(1)
    print(x)