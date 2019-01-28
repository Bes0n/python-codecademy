## Practice Makes Perfect

### is_even
All right! Let's get started.

Remember how an even number is a number that is divisible by 2?

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function <code>is_even</code> that will take a number <code>x</code> as input.</p>
<p>If <code>x</code> is even, then <code>return True</code>.</p>
<p>Otherwise, <code>return False</code>.</p>
</div>

```python
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
```

### is_int
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>An integer is just a number without a decimal part (for instance, <code>-17</code>, <code>0</code>, and <code>42</code> are all integers, but <code>98.6</code> is not).</p>
<p>For the purpose of this lesson, we'll also say that <strong>a number with a decimal part that is all 0s is also an integer</strong>, such as <code>7.0</code>.</p>
<p>This means that, for this lesson, you can't just test the input to see if it's of type <code>int</code>.</p>
<p>If the difference between a number and that same number rounded is greater than zero, what does that say about that particular number?</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function <code>is_int</code> that takes a number <code>x</code> as an input.</p>
<p>Have it <code>return True</code> if the number is an integer (as defined above) and <code>False</code> otherwise.</p>
<p>For example:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">is_int</span>(<span class="cm-number">7.0</span>)<!-- -->   <span class="cm-comment"># True    </span>
<span class="cm-variable">is_int</span>(<span class="cm-number">7.5</span>)<!-- -->   <span class="cm-comment"># False    </span>
<span class="cm-variable">is_int</span>(<span class="cm-operator">-</span><span class="cm-number">1</span>)<!-- -->    <span class="cm-comment"># True</span></div></span>
</code></pre>
</div>

```python
def is_int(x):
  if x // 1 == x:
    return True
  else:
    return False
    
or codecademy solution:

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)
```

### digit_sum
Awesome! Now let's try something a little trickier. Try summing the digits of a number.

###### TASK 
<p>Write a function called <code>digit_sum</code> that takes a positive integer <code>n</code> as input and returns the sum of all that number's digits. For example: <code>digit_sum(1234)</code> should return <code>10</code> which is <code>1 + 2 + 3 + 4</code>. (Assume that the number you are given will always be positive.)</p>

```python
def digit_sum(n):
  n = str(n)
  dsum = 0
  for i in n:
    dsum += int(i)
  return dsum

#Alternate Solution:

#def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total
```

### factorial

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>All right! Now we're cooking. Let's try a factorial problem.</p>
<p>To calculate the factorial of a non-negative integer <code>x</code>, just multiply all the integers from 1 through <code>x</code>. For example:</p>
<ul>
<li><code>factorial(4)</code> would equal <code>4 * 3 * 2 * 1</code>, which is 24.</li>
<li><code>factorial(1)</code> would equal <code>1</code>.</li>
<li><code>factorial(3)</code> would equal <code>3 * 2 * 1</code>, which is 6.</li>
</ul>
</div>

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function <code>factorial</code> that takes an integer <code>x</code> as input.</p>
<p>Calculate and return the factorial of that number.</p>
</div>

```python
def factorial(x):
  multiplier = 1
  while x > 1:
    multiplier *= x
    x -= 1
  return multiplier

print(factorial(4))
```

### is_prime
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>A <em>prime number</em> is a positive integer greater than 1 that has no positive divisors other than 1 and itself. (That's a mouthful!)</p>
<p>In other words, if you want to test if a number in a variable <code>x</code> is prime, then no other number should go into <code>x</code> evenly besides 1 and <code>x</code>. So <code>2</code> and <code>5</code> and <code>11</code> are all prime, but <code>4</code> and <code>18</code> and <code>21</code> are not.</p>
<p>If there is a number between 1 and <code>x</code> that goes in evenly, then <code>x</code> is not prime.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>is_prime</code> that takes a number <code>x</code> as input.</p>
<p>For each number <code>n</code> from 2 to <code>x - 1</code>, test if <code>x</code> is evenly divisible by <code>n</code>.</p>
<p>If it is, <code>return False</code>.</p>
<p>If none of them are, then <code>return True</code>.</p>
</div>
