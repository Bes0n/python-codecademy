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

```python
board = []

for i in range(5):
  board.append(["O"] * 5)

#Output 
"""
[

['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']

]
"""
```

### Check it Twice
Great job! Now that we've built our board, let's show it off.

Throughout our game, we'll want to print the game board so that the player can see which locations they have already guessed. Regularly printing the board will also help us debug our program.

The easiest way to print the board would be to have Python display it for us using the print command. Let's give that a try and see what the results look like—is this a useful way to print our board for Battleship?
