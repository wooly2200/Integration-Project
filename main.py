"""
# Christian Woolard
# My Integration Project
# Maze Game
"""

# The function below will prompt the user for how far they want to move.


def amount_to_move():
    """

    :return:
    """
    move_amount = int(input("Enter the amount you wish to move: "))
    return move_amount

# This function below will prompt the
# user for what direction they want to move.


def direction_move():
    """

    :return:
    """
    direction = input(" Direction to move:\nLeft\nRight\nUp\nDown\n").lower()
    return direction


# This function is my maze game. It uses multiple while loops with the try/
# exception, inorder to make sure the user enters the correct answers
# and the game will not crash.


def my_maze():
    """
    :no param
    """
    print(".--.--.--. *.--.--.\n"
          "|     |        |  |\n"
          ":  :--:  :  :  :  :\n"
          "|  |     |  |     |\n"
          ":  :  :  :--:--:--:\n"
          "|  |  |           |\n"
          ":--:  :--:--:--:--:\n")
    # validate_tes and the while loop below are used multiple times
    # The purpose ist to repeat the questions for direction and movement,
    # to the new corresponding maze after a correct entry.
    validate_test = True
    while validate_test:
        try:
            user_amount_move = amount_to_move()
            choice_direction = direction_move()
        except ValueError:
            print("Error please try again: ")
        else:
            if (user_amount_move == 1) and (choice_direction == "down"):
                print(".--.--.--.  .--.--.\n"
                      "|     |    *   |  |\n"
                      ":  :--:  :  :  :  :\n"
                      "|  |     |  |     |\n"
                      ":  :  :  :--:--:--:\n"
                      "|  |  |           |\n"
                      ":--:  :--:--:--:--:\n")
                print("Next Move!")

                while validate_test:
                    try:
                        user_amount_move = amount_to_move()
                        choice_direction = direction_move()
                    except ValueError:
                        print("Error please try again: ")
                    else:
                        if (user_amount_move == 3) and (
                                choice_direction == "left"):
                            print(".--.--.--.  .--.--.\n"
                                  "|     | *      |  |\n"
                                  ":  :--:  :  :  :  :\n"
                                  "|  |     |  |     |\n"
                                  ":  :  :  :--:--:--:\n"
                                  "|  |  |           |\n"
                                  ":--:  :--:--:--:--:\n")
                            print("Next Move!")
                            while validate_test:
                                try:
                                    (user_amount_move) = (amount_to_move())
                                    (choice_direction) = (
                                        direction_move())
                                except ValueError:
                                    print("Error please try again: ")
                                else:
                                    if (user_amount_move == 2) and (
                                            choice_direction == "down"):
                                        print(".--.--.--.  .--.--.\n"
                                              "|     |        |  |\n"
                                              ":  :--:  :  :  :  :\n"
                                              "|  |    *|  |     |\n"
                                              ":  :  :  :--:--:--:\n"
                                              "|  |  |           |\n"
                                              ":--:  :--:--:--:--:\n")
                                        print("Next Move!")
                                        while validate_test:
                                            try:
                                                user_amount_move = (
                                                    amount_to_move())
                                                choice_direction = (
                                                    direction_move())
                                            except ValueError:
                                                print(
                                                    "Error please try again: ")
                                            else:
                                                if (user_amount_move == 3)\
                                                        and (
                                                        choice_direction
                                                        == "left"):
                                                    print(
                                                        ".--.--.--.  .--.--.\n"
                                                        "|     |        |  |\n"
                                                        ":  :--:  :  :  :  :\n"
                                                        "|  | *   |  |     |\n"
                                                        ":  :  :  :--:--:--:\n"
                                                        "|  |  |           |\n"
                                                        ":--:  :--:--:--:--:\n"
                                                    )
                                                    print("Next Move!")
                                                    while validate_test:
                                                        try:
                                                            (user_amount_move)\
                                                             = \
                                                             amount_to_move()
                                                            choice_direction =\
                                                                direction_move(

                                                                )
                                                        except ValueError:
                                                            print("Error "
                                                                  "please try "
                                                                  "again: ")
                                                        else:
                                                            if(
                                                               user_amount_move
                                                               == 3) and\
                                                             choice_direction\
                                                                    == "down":
                                                                print(
                                                                    ".--.--.-"
                                                                    "-.  .--."
                                                                    "--.\n"
                                                                    "|     | "
                                                                    "       | "
                                                                    " |\n"
                                                                    ":  :--: "
                                                                    " :  :  : "
                                                                    " :\n"
                                                                    "|  |     "
                                                                    "|  |     "
                                                                    "|\n"
                                                                    ":  :  : "
                                                                    " :--:--:"
                                                                    "--:\n"
                                                                    "|  |  |  "
                                                                    "         "
                                                                    "|\n"
                                                                    ":--: *:-"
                                                                    "-:--:--:"
                                                                    "--:\n")
                                                                print(
                                                                    "Congratul"
                                                                    "ations!"
                                                                    " You have"
                                                                    " beaten "
                                                                    "my Game!")

                                                                validate_test\
                                                                    = False
                                                            else:
                                                                print(
                                                                    "Incorrect"
                                                                    " try "
                                                                    " again: ")
                                                else:
                                                    print("Incorrect try "
                                                          "again: ")
                                    else:
                                        print("Incorrect try again: ")
                        else:
                            print("Incorrect try again: ")
            else:
                print("Incorrect try again: ")


# Below is the beginning of my game that will
# prompt the user for information about them.
print("Hello and welcome to my Game! Before we get started", end='.')
print(" Please accept our terms and conditions:\n"
      "By agreeing to these conditions you agree to the collection\n"
      "storage, and distribution of your data!")
# validation variable is used to close the infinite loop
validation_Test = True
# Below is an infinite loop with variable countdown assigned not equal to 0
while validation_Test:
    try:
        terms_Conditions = input("Do you agree to the Terms and Conditions "
                                 "Yes or No:\n").lower()
    except ValueError:
        print("Error code 1245. Please try again.")
    else:
        accepted_terms = terms_Conditions.lower()
        if accepted_terms == "yes":
            print("Great lets create your profile!")
            validation_Test = False
        elif accepted_terms == "no":
            print("Too bad. You may continue anyways.")
            validation_Test = False
        else:
            print("Error in reading answer, please enter 'Yes' or 'No' ")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
email = input("Enter your email: ")
username = input("Enter your username: ")
countdown = 0
while countdown == 0:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Error try again: ")
    else:
        if age > 3:
            print("You are old enough to play! Great!")
            countdown = 1
        else:
            print("You are not older than 3, you cannot play.")
# Print statement below is connecting the '!' by using concatenate
# Also used 'sep' at the end of a print statement to add a ':'
print("Hello", firstName, lastName + "!\nYour username is",
      username + ". Now lets explain how the game works")
print("Your objective is to move the star to the other end of the maze.\n"
      "You will be given a prompt to enter a number and direction,\n"
      "it must be the correct entry in order to make it to the end!\n"
      "Hint: Use your cursor to estimate how far you need to move.\n")
validation = True
while validation:
    try:
        start = input("Enter 'y' to continue to the game!").lower()
    except ValueError:
        print("Error try again! ")
    else:
        if start == 'y':
            print("Lets begin!")
            validation = False
        else:
            print("You did not press 'y' try again! ")
my_maze()
