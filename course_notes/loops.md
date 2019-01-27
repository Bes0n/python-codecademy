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
