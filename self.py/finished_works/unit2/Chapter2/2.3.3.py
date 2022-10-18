# The legend "The Three Little Pigs" tells about three pigs who lived under the threat of a wolf. In order to provide themselves with shelter from him, they began to gather together building materials.
# Write a program that will display the total number of bricks collected by the pigs, and the number of bricks available to each pig, according to the following instructions.

# Guidelines:
# The program will receive as input a three-digit number (assume that the input is correct). Each digit in this number represents the number of bricks collected by another pig.
# The program will print the following output:
# The total number of bricks collected by the piggies (ie the sum of the three digits)
# The number of bricks that each pig will get if they divide the total number of bricks is equal among all
# The remainder of the distribution of bricks (as distributed in the previous section)
# True if the sum is divided between the three pigs without a remainder, and False otherwise. Note, do not use a conditional statement
# Do not use loops.

# My solution
user_input= input("Enter three digits (each digit for one pig): ")
sum= int(user_input[0])+int(user_input[1])+int(user_input[2])
division= int(sum / 3)
leftover= sum % 2
clean_division= not(sum % 2)
print(sum)
print(division)
print(leftover)
print(clean_division)