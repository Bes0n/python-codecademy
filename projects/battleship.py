from random import randint

board = []

print("""
Game description:
Ship hidded in one cell. Area size is 5x5
Start your guess from 0 to 4 (row and column)
You have 3 tries to win. 
""")


for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)
print("")

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  if turn < 3:
    print ("Turn %d" % (turn + 1))
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      print("Congratulations! You sank my battleship!")
      break
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
      print_board(board)
  else:
    print("Game Over")
