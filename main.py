# Christian Woolard
# My Integration Project
# Maze Game

# Below is a print statement that uses 'end'
print("Hello and welcome to my Game! Before we get started" , end = '.')
print("Please accept or terms and conditions:\n"
      "By agreeing to these conditions you agree to the collection\n"
      "and storge of the data you enter!")
terms_Conditions = input("Do you agree to the Terms and Conditions Yes or No:\n").lower()
# countdown variable is used to close the infinite loop
countdown = 1
# Below is an infinite loop with variable countdown assigned not equal to 0
while countdown != 0:
    # If statement below creates a boolean of
    # terms_conditions is equal to 'yes' then executes the rest of the code
    # Below is boolean operator ==
    if terms_Conditions == "yes":
        print("Thank you! Now lets create your profile!")
        # shortcut operator subtract 1 from countdown
        # and executes the rest of the code
        countdown -= 1
    # elif statement below
    elif terms_Conditions == "no":
        print("Sorry! Goodbye!")
    # exit function ends the program because user did not agree to terms
        exit()
    # Else tests the user response for terms_conditions
    # if it is not yes or no the program will continue
    # to ask for the right response
    else:
        terms_Conditions = input("Invalid entry please try again!")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
email = input("Enter your email: ")
username = input("Enter your username: ")
age = input("Enter your age")
# Print statement below is connecting the '!' by using a concatenate
# Also used 'sep' at the end of a print statement to add a ':'
print("Hello" , firstName, lastName + "!")
print("Your username is" , username)
print("Now lets explain how the game works" , sep = ":")
# \n is used to move my code to the next line down
# Created multiple functions for three different difficulty levels
def easy_Choice(easy):
    print("You have chosen easy difficulty begin!")
    # Below is a nested for loop with outer and inner loops
    # 'in' and 'range' used in both loops
    for x in range(10):
        for x in range(10):
            print("*" + " ", end=" ")
        print()
def normal_Choice(normal):
    print("You have chosen normal difficulty begin!")
    for x in range(20):
        for x in range(20):
            print("*" + " ", end=" ")
        print()
def hard_Choice(hard):
    print("You have chosen hard difficulty begin!")
    for x in range(50):
        for x in range(50):
            print("*" + " ", end=" ")
        print()
def difficulty_Choice(Choice):
    print("Choose your difficulty: \nEasy\nNormal\nHard\n")
# The code below is calling def difficulty_Choice function
difficulty_Choice('Choice')
# .lower helps with validating the entry the user entered is valid
difficulty = input("Enter your difficulty: ").lower()
loop_done = 0
while loop_done == 0:
    if difficulty == "easy":
        easy_Choice("easy")
        # += is a shortcut operator to add 1 to variable loop_done
        loop_done += 1
    elif difficulty == "normal":
        normal_Choice("normal")
        loop_done += 1
    elif difficulty == "hard":
        hard_Choice("hard")
        loop_done += 1
        # If difficulty is not 'easy', 'normal', 'hard' the code below, 'else',
        # will continue to as user for valid entry.
    else:
        difficulty = input("Invalid entry try again: ").lower()
# def EnterNumber(num1):
# def Direction(choice):
#     direction == input(" Direction to move:\nLeft\nRight\nUp\nDown\n")
# below I will do logical operators
num1 = 1
num2 = 2
num3 = 3
# even though num1 is not greater than num2 the code
# still executes because num3 is greater than num2
if (num1 > num2) or (num3 > num2):
    print(num3)
# The code does not execute because both booleans must be true
if (num1 > num2) and (num3 > num2):
    print("done")
# The code below does execute because 'not' inverts num1==num2 so it is true
if not(num1 == num2):
    print("Success")

