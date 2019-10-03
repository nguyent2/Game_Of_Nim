######################################################################
# Author: Thy H. Nguyen
# Username: nguyent2

# Assignment: A05: The Game of Nim
# Purpose: Make the Game of Nim _ Thinking about Algorithm
#Practice breaking a larger problem down into smaller "mental chunks" using functions.
#Gain practice using loops and modulus (%).

# ######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by Raffi: https://www.youtube.com/watch?v=sOOZQZlxxC4
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random

def check_integer(initial_number_of_balls):
    """
    This function checks if the user's initial input is an integer or not.
    If not: return False
    If it is: return True
    :param initial_number_of_balls: this is the variable saving the user's input
    :return: True if the user puts in an integer
    False if the user did not put in an integer
    """
    try:
        change_into_integer = int(initial_number_of_balls)
    # The function try to convert any input (type is string) into integer
        return True
    #When the input is not an integer, the function will have a value error in converting the type from a string to an integer.
    #The function will then return False. Otherwise, the function returns True.
    except ValueError:
        return False
    #Return False when it has Value error in converting

def check_integer_greater_than_or_equal_to_15(number_of_balls_starting_with):
    """
    The function checks to see if the user puts in an integer which is greater or equal to 15
    (As the game requires starting with choosing at least 15 balls.)
    :param number_of_balls_starting_with: the variable saves the number of the balls the user chooses to start the game with.
    :return: the number of the balls (if the number is any integer greater than or equal to 15)
    """
    while check_integer(number_of_balls_starting_with) == False or int(number_of_balls_starting_with) < 15:
        number_of_balls_starting_with = input("Please enter a number of balls greater than or equal to 15: ")
    #As long as the user does not put in a valid integer to start the game with (which is an integer greater or equal to 15),
    #the function will infinitely and continuously asks the user to enter a valid integer.
    print ("Let's play the Game of Nim with ", number_of_balls_starting_with, " balls.")
    #If the integer is valid, print, the number of balls starting the game with
    return number_of_balls_starting_with
    #return the number of the balls starting with

def pick_a_number(number):
    """
    The function asks the user to remove any number of balls (from 1 to 4)
    :param number: The variable saves the number of balls the users want to remove each turn
    :return: the number of balls removing
    """
    while check_integer(number) == False or int(number) > 4 or int(number) < 1 :
        number = input("Please pick a number of balls you want to remove [from 1 to 4]: ")
    #As long as the user does not enter a valid number of balls to remove from the stack
    # (1<= number of balls removing <=4), the function continuously asks the user to enter a valid number
    return number
    #return the number of balls removing

def game_of_nim(number):
    """
    The function start the Game of Nim each round by asking the user to enter a valid number of balls removing
    :param number: This is the initial number of balls the user wants to start the game with
    :return: the number of balls left after each time the user replaces 1-4 balls
    """
    global number_of_balls_left
    #Make the number of balls left on the global scope, so it can be used outside of the function
    number_of_balls = input("Please pick a number of balls you want to remove [from 1 to 4]: ")
    #Ask the user to enter a valid number of balls removing (from 1 to 4)
    number_of_balls_left = int(number) - int(pick_a_number(number_of_balls))
    #number of balls left equals the initial number of balls put in minus the number of balls removing each turn.
    print("There are ", number_of_balls_left, " balls left after your turn.")
    #print the number of balls left after each time the user removes the ball out.

def computer_turn():
    """
    This function is the computer's turn to randomly removes the number of balls.
    :return: the number of balls left after the computer's turn.
    """
    global balls_left
    #Assign the variable to the balls the computer randomly removes
    choose_from_list = random.choice(["1","2","3","4"])
    # the list of number of balls the computer can choose to remove randomly (from 1 to 4)
    print("The computer chooses to remove ",choose_from_list, "balls.")
    # Computer chooses a random number from 1 to 4 balls to remove
    balls_left = int(number_of_balls_left) - int(choose_from_list)
    #the number of balls left after the computer's turn.
    print("There are ",balls_left, " balls left after the computer's turn.")
    #print the number of balls left

def looping_to_get_the_final_result():
    """
    This function creates a loop between user's turn and computer's turn.
    :return: The result whether user wins or the computer wins
    """
    while balls_left >1 and number_of_balls_left >1:
        #This loop has some funny part that whenever the number of ball left is -1, I assume that the current player (either the user or the computer) have already taken all of the remaining balls out.
        game_of_nim(balls_left)
        #As the computer randomly chooses to remove the number of balls without any strategy, any number of balls greater than 1 is not really important to be considered who is the winner.
        if number_of_balls_left >1:
            #If the number of the balls remaining after the user's turn is greater than 1, let the computer to take its turn.
            computer_turn()
    if number_of_balls_left == 1:
        #when it is only 1 ball after the user's turn, it is definitely the computer who wins.
        print("Computer wins since there is no other way for the computer not to win!")
    if balls_left == 1:
        # when it is only 1 ball after the computer's turn, it is definitely the user who wins.
        print("The user wins since there is no other way for you not to win!")
    if balls_left < 0:
        # when the ball left is negative (if and only if there are fewer than 4 balls left in the turn of any player), so I assume that the player takes the remaining of the balls out.
        #The reason is that realistically, no player needs to think about how many balls they need to take out in order to win, when they just need to take out all of the remaining balls. (If they are willing to win the game.).
        print("Well, the computer is just kidding with you! What the computer doing is taking the rest of the balls, which are , ", abs(balls_left)," balls, and wins! ")
    if number_of_balls_left <0:
        # This is the same case for the user.
        print("Hey! You are definitely just kidding with the computer and you have taken all of the rest of the balls out, which are, ", abs(number_of_balls_left), " balls, and win!")
    if balls_left == 0:
        #If there are no balls left after the computer turn, it means that the computer already took the last ball out.
        print("Computer wins!")
    if number_of_balls_left == 0:
        # If there are no balls left after the user turn, it means that the user already took the last ball out.
        print("You win")

def main():
    """
    This function is used to call all of the previous functions
    :return: The result who will win the Game of Nim
    """
    game_of_nim(check_integer_greater_than_or_equal_to_15(number_of_balls_starting_with= input("Please enter a number greater than or equal to 15: ")))
    # The variable number of balls starting with is taking the value the user puts in
    # Then, it checks through the check_integer_greater_than_or_equal_to_15 to determine if the input is valid for the game
    # Then the number will be put into the Game of Nim and start the game.
    #This will be the user's first turn to take out the balls.
    computer_turn()
    #This is the computer's first turn to take out the balls.
    looping_to_get_the_final_result()
    #run the looping_to_get_the_final_result function to print out who wins

if __name__ == "__main__":
    main()
    # Calling and executing the main function