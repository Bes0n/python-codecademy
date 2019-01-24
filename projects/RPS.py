"""
In this project, we'll build Rock-Paper-Scissors!

The program should do the following:

1. Prompt the user to select either Rock, Paper, or Scissors.
2. Instruct the computer to randomly select either Rock, Paper, or Scissors.
3. Compare the user's choice and the computer's choice.
4. Determine a winner (the user or the computer).
5. Inform the user who the winner is.

Happy coding!

if you get stuck:
https://youtu.be/jxyrSodMJ0A
"""


"""
What is program doing?

1. Prompt the user to select either Rock, Paper, or Scissors.
2. Instruct the computer to randomly select either Rock, Paper, or Scissors.
3. Compare the user's choice and the computer's choice.
4. Determine a winner (the user or the computer).
5. Inform the user who the winner is.

"""

#Since the computer will select Rock, Paper, or Scissors randomly, we will need the randint function – which is not built-in.
from random import randint

options = ['ROCK', 'PAPER', 'SCISSORS']

message = {"tie": "Yawn it's a tie!", 
           "won" : "Yay you won!", 
           "lost" : "Aww you lost!"}

def decide_winner(user_choice, computer_choice):
  """
  How do we determine the result?
	
  Start by adding an if statement that checks if the user_choice is equal to the computer_choice. 	This means it's a tie!

	Inside the if statement, print the message to the user informing them of the tie. The message is
  stored under the "tie" key in message dictionary.
  """
  print("User choice: %s" % user_choice)
  print("Computer choice: %s" % computer_choice)
  
  """
		Now it's time to think of the scenarios in which the user wins:
    
		User: Rock, Computer: Scissors
		User: Paper, Computer: Rock
		User: Scissors, Computer: Paper
  """
  if user_choice == computer_choice:
    print(message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print(message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print(message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print(message["won"])
  else:  
    print(message["lost"])

    
"""
Great! We have the function that will decide who the winner is between the user and the computer, but we haven't written a function that actually starts the game. Let's do that now.
"""    
def play_RPS():
  user_input = raw_input("Enter Rock, Paper, or Scissors: ")
  """  
  Convert the user's choice to uppercase in case they type in lowercase rock, paper, or scissors.
  """
  user_choice = user_input.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice,computer_choice)
  
play_RPS()
