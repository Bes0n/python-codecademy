### Number Guess

""" Wanna play a game? In this project, we'll build a program that rolls a pair of dice and asks the user to guess the sum. 
If the user's guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.
The program should do the following:
    Roll a pair of dice.
    Add the values of the roll.
    Ask the user to guess a number.
    Compare the user's guess to the total value.
    Determine the winner (user or computer).
Let's begin! """

#To make sure that the rolls are random, we will need some Python code that isn't built-in  we need to import the randint function,
#from the random module.
from random import randint 

#You'll also need to import more code that will be used to simulate dice rolls.
from time import sleep

#By default, using raw_input alone will store the user's input as a string. Since the user is guessing a whole number, 
#we will need an integer, not a string. 
def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess 
#The roll_dice function will be used to simulate the rolling of a pair of dice. 
def roll_dice(number_of_sides):
  #Use the randint function that you imported earlier to generate a random integer between 1 and number_of_sides. 
  #The syntax for the function looks 
  first_roll = randint(1, int(number_of_sides))
  second_roll = randint(1, int(number_of_sides))
  #On the next line, create a variable called max_val and set it equal to number_of_sides times 2 (since there are two dice).
  max_val = number_of_sides * 2
  print("Max possible value: %s" % (max_val))
  #On the next line, call the get_user_guess() function. Remember that the function will return the user's guess 
  #after prompting the user.
  #Store the returned value into a variable called guess.
  guess = get_user_guess()
  if guess > max_val:
    print("Your guess is greater that the maximum value.")
  else:
    print("Rolling...")
    sleep(2)
    #Print roll numbers 
    print("First roll gave number: %d" % (first_roll))
    sleep(1)
    print("Second roll gave number: %d" % (second_roll))
    sleep(1)
    #get total of first and second roll 
    total_roll = first_roll + second_roll
    print("Total roll is %d" % (total_roll))
    print("Result...")
    sleep(1)
    #if you guessed number right - you won, else you lost
    if guess == total_roll:
      print("You won!")
    else:
      print("You lost")

#calling function, where number in function is a number of sides of one dice. 
roll_dice(4)
