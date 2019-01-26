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
