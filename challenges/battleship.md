## Welcome to Battleship!
In this project you will build a simplified, one-player version of the classic board game Battleship! In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.

To build this game we will use our knowledge of lists, conditionals and functions in Python. When you're ready to get started, click Next to continue.

### Getting Our Feet Wet
<p>Create a variable <code>board</code> and set it equal to an empty list.</p>

```
board = []
```

### Make a List
<p>Good! Now we'll use a built-in Python function to generate our board, which we'll make into a 5 x 5 grid of all <code>"O"</code>s, for "ocean."</p>

```
print ["O"] * 5
```

<p>will print out <code>['O', 'O', 'O', 'O', 'O']</code>, which is the basis for a row of our board.</p>
<p>We'll do this five times to make five rows. (Since we have to do this five times, it sounds like a loop might be in order.)</p>

###### TASK
<p>Create a 5 x 5 grid initialized to all 'O's and store it in <code>board</code>.</p>

<ul>
<li>Use <code>range()</code> to loop <code>5</code> times.</li>
<li>Inside the loop, <code>.append()</code> a list containing 5 <code>"O"</code>s to <code>board</code>, just like in the example above.</li>
</ul>

<p>Note that these are capital letter "O" and not zeros.</p>

### Check it Twice
Great job! Now that we've built our board, let's show it off.

Throughout our game, we'll want to print the game board so that the player can see which locations they have already guessed. Regularly printing the board will also help us debug our program.

The easiest way to print the board would be to have Python display it for us using the print command. Let's give that a try and see what the results look like—is this a useful way to print our board for Battleship?

###### TASK
<p>Use the <code>print</code> command to display the contents of the <code>board</code> list.</p>

```python
board = []

for i in range(5):
  board.append(["O"] * 5)

#Output 
"""
[
['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']
]
"""

### Custom Print

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Now we can see the contents of our list, but clearly it would be easier to play the game if we could print the board out like a grid with each row on its own line.  </p>
<p>We can use the fact that our board is a list of lists to help us do this.  Let's set up a <code>for</code> loop to go through each of the elements in the outer list (each of which is a row of our board) and print them.</p>
</div>

###### TASK

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>First, delete your existing <code>print</code> statement.</p>
<p>Then, define a function named <code>print_board</code> with a single argument, <code>board_in</code>.</p>
<p>Inside the function, write a <code>for</code> loop to iterates through each <code>row</code> in <code>board</code> and <code>print</code> it to the screen.</p>
<p>Call your function with <code>board</code> to make sure it works.</p>
</div>
```

```python
board = []

for i in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print(row)
    
print_board(board)

#Output

['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']

```

### Printing Pretty
<p>We're getting pretty close to a playable board, but wouldn't it be nice to get rid of those quote marks and commas?  We're storing our data as a list, but the player doesn't need to know that!</p>

```python
letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)
```

<ol>
<li>In the example above, we create a list called <code>letters</code>.</li>
<li>Then, we print <code>a b c d</code>. The <code>.join</code> method uses the string to combine the items in the list.</li>
<li>Finally, we print <code>a---b---c---d</code>. We are calling the <code>.join</code> function on the <code>"---"</code> string.</li>
</ol>

<p>We want to turn each row into <code>"O O O O O"</code>.</p>

###### TASK
<p>Inside your function, inside your <code>for</code> loop, use <code>" "</code> as the separator to <code>.join</code> the elements of each <code>row</code>.</p>

```python 
board = []

for i in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print " ".join(row)
    
print_board(board)
```

### Hide...

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Excellent!  Now, let's hide our battleship in a random location on the board.</p>
<p>Since we have a 2-dimensional list, we'll use  two variables to store the ship's location, <code>ship_row</code> and <code>ship_col</code>.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">from</span> <span class="cm-variable">random</span> <span class="cm-keyword">import</span> <span class="cm-variable">randint</span>
<span class="cm-variable">coin</span> <span class="cm-operator">=</span> <span class="cm-variable">randint</span>(<span class="cm-number">0</span>,<!-- --> <span class="cm-number">1</span>)<!-- -->
<span class="cm-variable">dice</span> <span class="cm-operator">=</span> <span class="cm-variable">randint</span>(<span class="cm-number">1</span>,<!-- --> <span class="cm-number">6</span>)</div></span>
</code></pre>
<ol>
<li>In the above example, we first import the <code>randint(low, high)</code> function from the <code>random</code> module.</li>
<li>Then, we generate either zero or one and store it in <code>coin</code>.</li>
<li>Finally, we generate a number from one to six inclusive.</li>
</ol>
<p>Let's generate a <code>random_row</code> and <code>random_col</code> from zero to four!</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define two new functions, <code>random_row</code> and <code>random_col</code>, that each take <code>board_in</code> as input.</p>
<p>These functions should <code>return</code> a random row index and a random column index from your board, respectively. Use <code>randint(0, len(board_in) - 1)</code>.</p>
<p>Call each function on <code>board</code>.</p>
</div>

```python
from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)
    
# Add your code below!
def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

random_row(board)
random_col(board)
```

### ...and Seek!
<p>Good job! For now, let's store coordinates for the ship in the variables <code>ship_row</code> and <code>ship_col</code>.  Now you have a hidden battleship in your ocean!  Let's write the code to allow the player to guess where it is.  </p>

```python 
number = raw_input("Enter a number: ")
if int(number) == 0:
  print "You entered 0"
```

<p><code>raw_input</code> asks the user for input and returns it as a string. But we're going to want to use integers for our guesses! To do this, we'll wrap the <code>raw_input</code>s with <code>int()</code> to convert the string to an integer.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a new variable called <code>guess_row</code> and set it to <code>int(raw_input("Guess Row: "))</code>.</p>
<p>Create a new variable called <code>guess_col</code> and set it to <code>int(raw_input("Guess Col: "))</code>.</p>
<p>Click <strong>Run</strong> and then answer the prompts by typing in a number and pressing Enter (or Return on some computers).</p>
</div>

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))
```

### It's Not Cheating—It's Debugging!

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Awesome!  Now we have a hidden battleship and a guess from our player.  In the next few steps, we'll check the user's guess to see if they are correct.  </p>
<p>While we're writing and debugging this part of the program, it will be helpful to know where that battleship is hidden.  Let's add a <code>print</code> statement that displays the location of the hidden ship.</p>
<p>Of course, we'll remove this output when we're finished debugging since if we left it in, our game wouldn't be very challenging. :)  </p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Before the lines prompting the user for input:</p>
<p>Print the value of <code>ship_row</code>.</p>
<p>Print the value of <code>ship_col</code>.</p>
</div>

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Add your code below!
print(ship_row)
print(ship_col)

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

```

### You win!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Okay—now for the fun!  We have the actual location of the ship and the player's guess so we can check to see if the player guessed right.</p>
<p>For a guess to be right, <code>guess_col</code> should be equal to <code>ship_col</code> and <code>guess_row</code> should be equal to <code>ship_row</code>.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">if</span> <span class="cm-variable">guess_col</span> <span class="cm-operator">==</span> <span class="cm-number">0</span> <span class="cm-keyword">and</span> <span class="cm-variable">guess_row</span> <span class="cm-operator">==</span> <span class="cm-number">0</span>:<!-- -->
<!-- -->  <span class="cm-builtin">print</span> <span class="cm-string">"Top-left corner."</span></div></span>
</code></pre>
<p>The example above is just a reminder about <code>if</code> statements.</p>
</div>

### Danger, Will Robinson!!
Great! Of course, the player isn't going to guess right all the time, so we also need to handle the case where the guess is wrong.

```python
print board[2][3]
```

<p>The example above prints out <code>"O"</code>, the element in the 3rd row and 4th column.</p>

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Add an <code>else</code> under the <code>if</code> we wrote in the previous step.</p>
<p>Print out <code>"You missed my battleship!"</code></p>
<p>Set the list element at <code>guess_row</code>, <code>guess_col</code> to <code>"X"</code>.</p>
<p>As the last line in your <code>else</code> statement, call <code>print_board(board)</code> again so you can see the <code>"X"</code>.Make sure to enter a col and row that is on the board!</p>
</div>

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else:
  print("You missed my battleship!")
  board[guess_row][guess_col] = "X"
  print_board(board)
```

### Bad Aim
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Great job!  Now we can handle both correct and incorrect guesses from the user.  But now let’s think a little bit more about the "miss" condition.</p>
<ol>
<li>They can enter a guess that's off the board.</li>
<li>They can guess a spot they’ve already guessed.</li>
<li>They can just miss the ship.</li>
</ol>
<p>We'll add these tests inside our <code>else</code> condition. Let's build the first case now!</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">if</span> <span class="cm-variable">x</span> <span class="cm-keyword">not</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">8</span>)<!-- --> <span class="cm-keyword">or</span> <!-- -->\<!-- -->
<!-- -->   <span class="cm-variable">y</span> <span class="cm-keyword">not</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">3</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-builtin">print</span> <span class="cm-string">"Outside the range"</span></div></span>
</code></pre>
<p>The example above checks if either <code>x</code> or <code>y</code> are outside those ranges. The <code>\</code> character just continues the <code>if</code> statement onto the next line.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Add a new <code>if</code> statement that is nested under the <code>else</code>.</p>
<p>Like the example above, it should check if <code>guess_row</code> is not in <code>range(5)</code> or  <code>guess_col</code> is not in <code>range(5)</code>.</p>
<p>If that is the case, print out <code>"Oops, that's not even in the ocean."</code></p>
<p>After your new <code>if</code> statement, add an <code>else</code> that contains your existing handler for an incorrect guess. Don't forget to indent the code!</p>
</div>

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else:
  if guess_row not in range(5) or \
  guess_col not in range(5):
    print("Oops, that's not even in the ocean.")
  else:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    print_board(board)
```

### Not Again!
Great! Now let's handle the second type of incorrect guess: the player guesses a location that was already guessed. How will we know that a location was previously guessed?

```python
print board[guess_row][guess_col]
```

<p>The example above will print an <code>'X'</code> if already guessed or an <code>'O'</code> otherwise.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Add an <code>elif</code> to see if the guessed location already has an 'X' in it.</p>
<p>If it has, <code>print "You guessed that one already."</code></p>
</div>

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print("Congratulations! You sank my battleship!")
else:
  if guess_row not in range(5) or \
  guess_col not in range(5):
    print("Oops, that's not even in the ocean.")
  elif board[guess_row][guess_col] == "X":
    print("You guessed that one already.")
  else:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    print_board(board)
```

### Test Run
Congratulations! Now you should have a game of Battleship! that is fully functional for one guess.

Make sure you play it a couple of times and try different kinds of incorrect guesses. This is a great time to stop and do some serious debugging.

In the next step, we'll move on and look at how to give the user 4 guesses to find the battleship.

###### TASK
Thoroughly test your game. Make sure you try a variety of different guesses and look for any errors in the syntax or logic of your program.

### Play It, Sam
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>You can successfully make one guess in Battleship! But we’d like our game to allow the player to make up to 4 guesses before they lose.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">for</span> <span class="cm-variable">turn</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">4</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-comment"># Make a guess</span>
<!-- -->  <span class="cm-comment"># Test that guess</span></div></span>
</code></pre>
<p>We can use a <code>for</code> loop to iterate through a range. Each iteration will be a turn.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Add a <code>for</code> loop that repeats the guessing and checking part of your game for 4 turns, like the example above.</p>
<p>At the beginning of each iteration, <code>print "Turn", turn + 1</code> to let the player know what <code>turn</code> they are on.</p>
<p>Indent everything that should be repeated.</p>
</div>

```python
from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
  print "Turn", turn + 1
  #for Python 3 print("Turn", turn + 1)
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print_board(board)
```

### Game Over
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>If someone runs out of guesses without winning right now, the game just exits. It would be nice to let them know why.</p>
<p>Since we only want this message to display if the user guesses wrong on their last turn, we need to think carefully about where to put it.</p>
<ol>
<li>We’ll want to put it under the <code>else</code> that accounts for misses</li>
<li>We’ll want to print the message no matter what the cause of the miss</li>
<li>Since our <code>turn</code> variable starts at 0 and goes to 3, we will want to end the game when <code>turn</code> equals <code>3</code>.</li>
</ol>
</div>

###### TASK

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Add an <code>if</code> statement that checks to see if the user is out of guesses.</p>
<ul>
<li>Put it under the <code>else</code> that accounts for misses.</li>
<li>Put it after the <code>if/elif/else</code> statements that check for the reason the player missed. We want <code>"Game Over"</code> to print regardless of the reason.</li>
</ul>
<p>If <code>turn</code> equals <code>3</code>, <code>print "Game Over"</code>.</p>
</div>

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  if turn < 3:
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sank my battleship!"   
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
      print_board(board)
  else:
    print("Game Over")
```

### A Real Win
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Almost there! We can play Battleship!, but you’ll notice that when you win, if you haven’t already guessed 4 times, the program asks you to enter another guess. What we’d rather have happen is for the program to end—it’s no fun guessing if you know you’ve already sunk the Battleship!</p>
<p>We can use the <code>break</code> command to get out of a <code>for</code> loop.</p>
</div>

###### TASK
<p>Add a <code>break</code> under the win condition to end the loop after a win.</p>

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  if turn < 3:
    print ("Turn %d" % (turn + 1))
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    
    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sank my battleship!"
      break
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
      print_board(board)
  else:
    print("Game Over")
```

### To Your Battle Stations!
Congratulations! You have a fully functional Battleship game! Play it a couple of times and get your friends to try it out, too. (Don’t forget to go back and remove the debugging output that gives away the location of the battleship!)

You may want to take some time to clean up and document your code as well.

###### TASK
When you are done playing Battleship! and are ready to move on, click Run.

```python
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

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
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sank my battleship!"
      break
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
      print_board(board)
  else:
    print("Game Over")
```

### Extra Credit
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!</p>
<ol>
<li><p>Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.</p>
</li>
<li><p>Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.</p>
</li>
<li><p>Make your game a two-player game.</p>
</li>
<li><p>Use functions to allow your game to have more features like rematches, statistics and more!</p>
</li>
</ol>
<p>Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!</p>
</div>

