## LOOPS

### While you're here
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The <code>while</code> loop is similar to an <code>if</code> statement: it executes the code inside of it if some condition is true.  The difference is that the <code>while</code> loop will continue to execute as long as the condition is true.  In other words, instead of executing if something is true, it executes while that thing is true.</p>
<p>Line 6 decides when the loop will be executed. So, "as long as <code>count</code> is less than <code>5</code>," the loop will continue to execute. Line 8 increases <code>count</code> by 1.  This happens over and over until <code>count</code> equals <code>5</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Change the loop so that it counts from <code>0</code> up to <code>9</code> (inclusive).</p>
<p>Be careful not to alter or remove the <code>count += 1</code> statement. If your program has no way to increase <code>count</code>, your loop could go on forever and become an <em>infinite loop</em> which could crash your computer/browser!</p>
</div>

```python
count = 0

if count < 5:
  print "Hello, I am an if statement and count is", count

while count < 10:
  print "Hello, I am a while and count is", count
  count += 1
```

### Condition

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The <em>condition</em> is the expression that decides whether the loop is going to continue being executed or not.  There are 5 steps to this program:</p>
<ol>
<li><p>The <code>loop_condition</code> variable is set to <code>True</code></p>
</li>
<li><p>The <code>while</code> loop checks to see if <code>loop_condition</code> is <code>True</code>.  It is, so the loop is entered.</p>
</li>
<li><p>The <code>print</code> statement is executed.</p>
</li>
<li><p>The variable <code>loop_condition</code> is set to <code>False</code>.</p>
</li>
<li><p>The <code>while</code> loop again checks to see if <code>loop_condition</code> is <code>True</code>.  It is not, so the loop is not executed a second time.</p>
</li>
</ol>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>See how the loop checks its condition, and when it stops executing? When you think you've got the hang of it, click Run to continue.<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The <em>condition</em> is the expression that decides whether the loop is going to continue being executed or not.  There are 5 steps to this program:</p>
<ol>
<li><p>The <code>loop_condition</code> variable is set to <code>True</code></p>
</li>
<li><p>The <code>while</code> loop checks to see if <code>loop_condition</code> is <code>True</code>.  It is, so the loop is entered.</p>
</li>
<li><p>The <code>print</code> statement is executed.</p>
</li>
<li><p>The variable <code>loop_condition</code> is set to <code>False</code>.</p>
</li>
<li><p>The <code>while</code> loop again checks to see if <code>loop_condition</code> is <code>True</code>.  It is not, so the loop is not executed a second time.</p>
</li>
</ol>
</div></p>
</div>

```python
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False
```

### While you're at it
<p>Inside a <code>while</code> loop, you can do anything you could do elsewhere, including arithmetic operations.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a <code>while</code> loop that prints out all the numbers from 1 to 10 squared (1, 4, 9, 16, ... , 100), each on their own line.  </p>
<ul>
<li>Fill in the blank space so that our <code>while</code> loop goes from <code>1</code> to <code>10</code> inclusive.</li>
<li>Inside the loop, print the value of <code>num</code> squared. The syntax for squaring a number is <code>num ** 2</code>.</li>
<li>Increment <code>num</code>.</li>
</ul>
</div>

```python
num = 1

# Fill in the condition
while num <= 10:
  # Print num squared
  print(num ** 2)	  
  # Increment num (make sure to do this!)
  num += 1
```

### Simple errors
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>A common application of a <code>while</code> loop is to check user input to see if it is valid.  For example, if you ask the user to enter <code>y</code> or <code>n</code> and they instead enter <code>7</code>, then you should re-prompt them for input.</p>
</div>

###### TASK
<p>Fill in the loop condition so the user will be prompted for a choice over and over while <code>choice</code> does not equal <code>'y'</code> and <code>choice</code> does not equal <code>'n'</code>.</p>

```python
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")
```

### Infinite loops
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>An <em>infinite loop</em> is a loop that never exits.  This can happen for a few reasons:</p>
<ol>
<li><p>The loop condition cannot possibly be false (<em>e.g.</em> <code>while 1 != 2</code>)</p>
</li>
<li><p>The logic of the loop prevents the loop condition from becoming false.</p>
</li>
</ol>
<p>Example:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">count</span> <span class="cm-operator">=</span> <span class="cm-number">10</span>
<span class="cm-keyword">while</span> <span class="cm-variable">count</span> <span class="cm-operator">&gt;</span> <span class="cm-number">0</span>:<!-- -->
<!-- -->  <span class="cm-variable">count</span> <span class="cm-operator">+=</span> <span class="cm-number">1</span> <span class="cm-comment"># Instead of count -= 1</span></div></span>
</code></pre>
</div>

###### TASK
<p>The loop in the editor has two problems: it's missing a colon (a syntax error) and <code>count</code> is never incremented (logical error).  The latter will result in an infinite loop, so be sure to fix both before running!</p>

```python
count = 0

while count < 10:
  print count
  # Increment count
  count += 1
```

### Break
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The <code>break</code> is a one-line statement that means "exit the current loop."  An alternate way to make our counting loop exit and stop executing is with the <code>break</code> statement.  </p>
<ul>
<li><p>First, create a <code>while</code> with a condition that is always true. The simplest way is shown.</p>
</li>
<li><p>Using an <code>if</code> statement, you define the <em>stopping condition</em>.  Inside the <code>if</code>, you write <code>break</code>, meaning "exit the loop."</p>
</li>
</ul>
<p>The difference here is that this loop is guaranteed to run at least once.</p>
</div>

###### TASK
<p>See what the <code>break</code> does? Feel free to mess around with it (but make sure you don't cause an infinite loop)! Click Run when you're ready to continue.</p>

```python
count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break
```

### While / else
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Something completely different about Python is the <code>while</code>/<code>else</code> construction. <code>while</code>/<code>else</code> is similar to <code>if</code>/<code>else</code>, but there is a difference: the <code>else</code> block will execute <strong>anytime</strong> the loop condition is evaluated to <code>False</code>.  This means that it will execute if the loop is never entered or if the loop exits normally.  If the loop exits as the result of a <code>break</code>, the <code>else</code> will not be executed.</p>
<p>In this example, the loop will <code>break</code> if a 5 is generated, and the <code>else</code> will not execute.  Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.</p>
</div>

###### TASK
<p>Click Run to see <code>while</code>/<code>else</code> in action!</p>

```python
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"

#Output: 
"""
Lucky Numbers! 3 numbers will be generated.
If one of them is a '5', you lose!
1
5
Sorry, you lose!

Or

Lucky Numbers! 3 numbers will be generated.
If one of them is a '5', you lose!
4
2
3
You win!
"""
```

### Your own while / else
Now you should be able to make a game similar to the one in the last exercise. The code from the last exercise is below:

```python 
count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
```

<p>In this exercise, allow the user to guess what the number is <code>3</code> times. </p>

```python
guess = int(raw_input("Your guess: "))
```

<p>Remember, <code>raw_input</code> turns user input into a string, so we use <code>int()</code> to make it a number again.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Use a <code>while</code> loop to let the user keep guessing so long as <code>guesses_left</code> is greater than zero.</p>
<p>Ask the user for their <code>guess</code>, just like the second example above.</p>
<p>If they guess correctly, <code>print "You win!"</code> and <code>break</code>.</p>
<p>Decrement <code>guesses_left</code> by one.</p>
<p>Use an <code>else:</code> case after your <code>while</code> loop to print <code>"You lose."</code>.</p>
</div>

```python 
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")
```

### For your health
<p>An alternative way to loop is the <code>for</code> loop.  The syntax is as shown in the code editor. This example means "for each number <code>i</code> in the range 0 - 9,  print <code>i</code>".</p>

###### TASK
Make the loop print the numbers from 0 to 19 instead of 0 to 9.

```python
print "Counting..."

for i in range(20):
  print i
```

### For your hobbies
This kind of loop is useful when you want to do something a certain number of times, such as append something to the end of a list.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a <code>for</code> loop that prompts the user for a hobby 3 times.</p>
<p>Save the result of each prompt in a <code>hobby</code> variable</p>
<p><code>append</code> each one to <code>hobbies</code>.</p>
<p>print <code>hobbies</code> after your <code>for</code> loop</p>
<p>Make sure to answer the prompts in the terminal when testing your code!</p>
</div>

```python
hobbies = []

# Add your code below!
for i in range(3):
  hobby = raw_input("Enter your hobby: ")
  hobbies.append(hobby)
```

### For your strings
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Using a <code>for</code> loop, you can print out each individual character in a string.  </p>
<p>The example in the editor is almost plain English: "for each character <code>c</code> in <code>thing</code>, print <code>c</code>".</p>
</div>

###### TASK 
<p>Add a second <code>for</code> loop so that each character in <code>word</code> is printed one at a time.</p>

```python 
thing = "spam!"

for c in thing:
  print c

word = "eggs!"

# Your code here!
for c in word:
  print(c)
```

### For your A
<p>String manipulation is useful in <code>for</code> loops if you want to modify some content in a string. </p>

```python
word = "Marble"
for char in word:
  print char,
```
<p>The example above iterates through each character in <code>word</code> and, in the end, prints out <code>M a r b l e</code>.</p>
<p>The <code>,</code> character after our <code>print</code> statement means that our next <code>print</code> statement keeps printing on the same line.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Let's filter out the letter <code>"A"</code> from our string.</p>
<ul>
<li>Do the following <code>for</code> each <code>char</code>acter in the <code>phrase</code>.</li>
<li>If <code>char</code> is an <code>"A"</code> or <code>char</code> is an <code>"a"</code>, <code>print "X",</code> instead of <code>char</code>. Make sure to include the trailing comma.</li>
<li>Otherwise (<code>else:</code>), please <code>print char,</code> with the trailing comma.</li>
</ul>
</div>

```python 
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print "X",
  else:
    print char,

#Don't delete this print statement!
print

#Output
"""
X   b i r d   i n   t h e   h X n d . . .
"""
```

### For your lists
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Perhaps the most useful (and most common) use of <code>for</code> loops is to go through a list.</p>
<p>On each iteration, the variable <code>num</code> will be the next value in the list.  So, the first time through, it will be <code>7</code>, the second time it will be <code>9</code>, then <code>12</code>, <code>54</code>, <code>99</code>, and then the loop will exit when there are no more values in the list.</p>
</div>

###### TASK
<p>Write a second <code>for</code> loop that goes through the <code>numbers</code> list and prints each element <em>squared</em>, each on its own line.</p>

```python
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

# Add your loop below!
for num in numbers:
  print num ** 2 
```

### Looping over a dictionary
You may be wondering how looping over a dictionary would work. Would you get the key or the value?

The short answer is: you get the key which you can use to get the value.

```python 
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print "This dictionary has the value 10!"
```

<ol>
<li>First, we create a dictionary with strings as the keys and numbers as the values.</li>
<li>Then, we iterate through the dictionary, each time storing the key in <code>key</code>.</li>
<li>Next, we check if that key's value is equal to 10. </li>
<li>If so, we print <code>"This dictionary has the value 10!"</code></li>
</ol>

###### TASK
<p>On line 5, print the key, followed by a space, followed by the value associated with that key.</p>

```python
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key, d[key]

#Output:
"""
a apple
c cherry
b berry
"""
```

### Counting as you go
<p>A weakness of using this for-each style of iteration is that you don't know the index of the thing you're looking at.  Generally this isn't an issue, but at times it is useful to know how far into the list you are.  Thankfully the built-in <code>enumerate</code> function helps with this.</p>
<p><code>enumerate</code> works by supplying a corresponding index to each element in the list that you pass it.  Each time you go through the loop, <code>index</code> will be one greater, and <code>item</code> will be the next item in the sequence.  It's very similar to using a normal <code>for</code> loop with a list, except this gives us an easy way to count how many items we've seen so far.</p>

###### TASK 
<p>We don't want the user to see things listed from index 0, since this looks unnatural. Instead, the items should appear to start at index 1.  Modify the print statement to reflect this behavior. See the Hint for help.</p>

```python
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1, item
  
#Output
"""
Your choices are:
1 pizza
2 pasta
3 salad
4 nachos
"""
```

### Multiple lists

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>It's also common to need to iterate over two lists at once.  This is where the built-in <code>zip</code> function comes in handy.</p>
<p><code>zip</code> will create pairs of elements when passed two lists, and will stop at the end of the shorter list.</p>
<p><code>zip</code> can handle three or more lists as well!</p>
</div>

###### TASK
Compare each pair of elements and print the larger of the two.

```python
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  print(max(a,b))
  
#Output
"""
3
9
17
15
30
"""
```

### For / else
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Just like with <code>while</code>, <code>for</code> loops may have an <code>else</code> associated with them.</p>
<p>In this case, the <code>else</code> statement is executed after the <code>for</code>, but only if the <code>for</code> ends normally—that is, not with a <code>break</code>. This code will <code>break</code> when it hits <code>'tomato'</code>, so the <code>else</code> block won't be executed.</p>
</div>

###### TASK
<p>Click Run to see how <code>for</code> and <code>else</code> work together.</p>

```python
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'
  
#Output
"""
You have...
A banana
A apple
A orange
A tomato is not a fruit!

Or if we will remove tomato from the list:

You have...
A banana
A apple
A orange
A pear
A grape
A fine selection of fruits!
"""
```

### Create your own
<p>To wrap up this lesson, let's create our own <code>for</code>/<code>else</code> statement from scratch.</p>

###### TASK 
<p>Build your <code>for</code>/<code>else</code> statement in the editor. Execution of the <code>else</code> branch is optional, but your code should print a string of your choice to the editor regardless.</p>

```python
microsoft_products = ['skype', 'windows', 'command center', 'exchange', 'scom', 'centos', 'sccm', 'dpm', 'orchestrator']

for product in microsoft_products:
  if product == 'centos':
    print('%s is not microsoft product' % 'centos')
    break
  print(product)
else:
  print("Yes, all listed products from Microsoft") 
```
