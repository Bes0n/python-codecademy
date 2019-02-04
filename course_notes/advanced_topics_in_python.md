## ADVANCED TOPICS IN PYTHON
### Iterators for Dictionaries
Let's start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.

```python
d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
```
<p>Note that the <code>.items()</code> method doesn't return key/value pairs in any specific order.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create your own Python dictionary, <code>my_dict</code>, in the editor to the right with two or three key/value pairs.</p>
<p>Then, <code>print</code> the result of calling the <code>my_dict.items()</code>.</p>
</div>

```python
my_dict = {
  "Name": "Ilgar",
  "Age": 27,
  "Surname": "Naghiyev"
}
print my_dict.items()
```

### keys() and values()
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>While <code>.items()</code> returns an array of <em>tuples</em> with each tuple consisting of a key/value pair from the dictionary:</p>
<ul>
<li>The <code>.keys()</code> method returns a list of the dictionary's keys, and</li>
<li>The <code>.values()</code> method returns a list of the dictionary's values.</li>
</ul>
<p>Again, these methods will not return the keys or values from the dictionary in any specific order.</p>
<p>You can think of a tuple as an immutable (that is, unchangeable) list. Tuples are surrounded by <code>()</code>s and can contain any data type.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Remove your call to <code>.items()</code> and replace it with a call to <code>.keys()</code> and a call to <code>.values()</code>, each on its own line. Make sure to <code>print</code> both!</p>
</div>

```python
my_dict = {
  "Name": "Ilgar",
  "Age": 27,
  "Surname": "Naghiyev"
}
print my_dict.items()
print my_dict.keys()
print my_dict.values()
```

### The 'in' Operator
<p>For iterating over lists, tuples, dictionaries, and strings, Python also includes a special keyword: <code>in</code>. You can use <code>in</code> very <code>in</code>tuitively, like so:</p>

```python
for number in range(5):
  print number,

d = { 
  "name": "Eric",
  "age": 26
}

for key in d:
  print key, d[key],

for letter in "Eric":
  print letter,  # note the comma!
```
<li>In the example above, first we create and iterate through a range, printing out <code>0 1 2 3 4</code>. Note that the trailing comma ensures that we keep printing on the same line.</li>
<li>Next, we create a dictionary and iterate through, printing out <code>age 26 name Eric</code>. Dictionaries have no specific order.</li>
<li>Finally, we iterate through the letters of a string, printing out <code>E r i c</code>.</li>

###### TASK
<p>For each <code>key in my_dict:</code> <code>print</code> out the key , then a space, then the value stored by that key. (You should use <code>print a, b</code> rather than <code>print a + " " + b</code>.)</p>

```python
my_dict = {
  "Name": "Ilgar",
  "Age": 27,
  "Surname": "Naghiyev"
}
print my_dict.keys()
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]
```

### Building Lists
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Let's say you wanted to build a list of the numbers from 0 to 50 (inclusive). We could do this pretty easily:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">my_list</span> <span class="cm-operator">=</span> <span class="cm-builtin">range</span>(<span class="cm-number">51</span>)</div></span>
</code></pre>
<p>But what if we wanted to generate a list according to some logic—for example, a list of all the even numbers from 0 to 50?</p>
<p>Python's answer to this is the <strong>list comprehension</strong>. List comprehensions are a powerful way to generate lists using the <code>for</code>/<code>in</code> and <code>if</code> keywords we've learned.</p>
</div>

###### TASK
<p>Check out the list comprehension example in the editor. When you're pretty sure you know what it'll do, click Run to see it in action.</p>

```python
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#output:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
```

### List Comprehension Syntax
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Here's a simple example of list comprehension syntax:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">new_list</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-variable">x</span> <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">1</span>,<!-- --> <span class="cm-number">6</span>)<!-- -->]<!-- -->
<span class="cm-comment"># =&gt; [1, 2, 3, 4, 5]</span></div></span>
</code></pre>
<p>This will create a <code>new_list</code> populated by the numbers one to five. If you want those numbers doubled, you could use:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">doubles</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-variable">x</span> <span class="cm-operator">*</span> <span class="cm-number">2</span> <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">1</span>,<!-- --> <span class="cm-number">6</span>)<!-- -->]<!-- -->
<span class="cm-comment"># =&gt; [2, 4, 6, 8, 10]</span></div></span>
</code></pre>
<p>And if you only wanted the doubled numbers that are evenly divisible by three:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">doubles_by_3</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-variable">x</span> <span class="cm-operator">*</span> <span class="cm-number">2</span> <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">1</span>,<!-- --> <span class="cm-number">6</span>)<!-- --> <span class="cm-keyword">if</span> <!-- -->(<span class="cm-variable">x</span> <span class="cm-operator">*</span> <span class="cm-number">2</span>)<!-- --> <span class="cm-operator">%</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0</span>]<!-- -->
<span class="cm-comment"># =&gt; [6]</span></div></span>
</code></pre>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Use a list comprehension to build a list called <code>even_squares</code> in the editor.</p>
<p>Your <code>even_squares</code> list should include the squares of the even numbers between 1 to 11. Your list should start <code>[4, 16, 36...]</code> and go from there.</p>
</div>


```python
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1,11) if x % 2 == 0]

print even_squares

```

### Now You Try!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Great work! Now it's time for you to create a list comprehension all on your own.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">c</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-string">'C'</span> <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">5</span>)<!-- --> <span class="cm-keyword">if</span> <span class="cm-variable">x</span> <span class="cm-operator">&lt;</span> <span class="cm-number">3</span>]<!-- -->
<span class="cm-builtin">print</span> <span class="cm-variable">c</span></div></span>
</code></pre>
<p>The example above creates and prints out a list containing <code>['C', 'C', 'C']</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Use a list comprehension to create a list, <code>cubes_by_four</code>.</p>
<p>The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.</p>
<p>Finally, <code>print</code> that list to the console.</p>
<p>Note that in this case, the cubed number should be evenly divisible by 4, not the original number.</p>
</div>

```python
cubes_by_four = [x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0]

print(cubes_by_four)

#output:
[8, 64, 216, 512, 1000]
```
### List Slicing Syntax
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Sometimes we only want part of a Python list. Maybe we only want the first few elements; maybe we only want the last few. Maybe we want every other element!</p>
<p>List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror">[<span class="cm-variable">start</span>:<span class="cm-variable">end</span>:<span class="cm-variable">stride</span>]</div></span>
</code></pre>
<p>Where <code>start</code> describes where the slice starts (inclusive), <code>end</code> is where it ends (exclusive), and <code>stride</code> describes the space between items in the sliced list. For example, a stride of <code>2</code> would select every other item from the original list to place in the sliced list.</p>
</div>

###### TASK
<p>We've generated a list with a list comprehension in the editor to the right, and we're about to print a selection from the list using list slicing. Can you guess what will be printed out? Click Run when you think you know!</p>

```python
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

#output: 
[9, 25, 49, 81]
```

### Omitting Indices

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>If you don't pass a particular index to the list slice, Python will pick a default. </p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">to_five</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-string">'A'</span>,<!-- --> <span class="cm-string">'B'</span>,<!-- --> <span class="cm-string">'C'</span>,<!-- --> <span class="cm-string">'D'</span>,<!-- --> <span class="cm-string">'E'</span>]<!-- -->
<!-- -->
<span class="cm-builtin">print</span> <span class="cm-variable">to_five</span>[<span class="cm-number">3</span>:<!-- -->]<!-- -->
<span class="cm-comment"># prints ['D', 'E'] </span>
<!-- -->
<span class="cm-builtin">print</span> <span class="cm-variable">to_five</span>[<!-- -->:<span class="cm-number">2</span>]<!-- -->
<span class="cm-comment"># prints ['A', 'B']</span>
<!-- -->
<span class="cm-builtin">print</span> <span class="cm-variable">to_five</span>[<!-- -->:<!-- -->:<span class="cm-number">2</span>]<!-- -->
<span class="cm-comment"># print ['A', 'C', 'E']</span></div></span>
</code></pre>
<ol>
<li>The default starting index is <code>0</code>.</li>
<li>The default ending index is the end of the list.</li>
<li>The default stride is <code>1</code>.</li>
</ol>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Use list slicing to <code>print</code> out every odd element of <code>my_list</code> from start to finish.</p>
<p>Omit the start and end index. You only need to specify a <code>stride</code>.</p>
<p>Check the Hint if you need help.</p>
</div>

```python
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print(my_list[::2])

#output:
[1, 3, 5, 7, 9]
```

### Reversing a List
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>We have seen that a positive stride progresses through the list from left to right.</p>
<p>A <em>negative</em> stride progresses through the list from right to left.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">letters</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-string">'A'</span>,<!-- --> <span class="cm-string">'B'</span>,<!-- --> <span class="cm-string">'C'</span>,<!-- --> <span class="cm-string">'D'</span>,<!-- --> <span class="cm-string">'E'</span>]<!-- -->
<span class="cm-builtin">print</span> <span class="cm-variable">letters</span>[<!-- -->:<!-- -->:<span class="cm-operator">-</span><span class="cm-number">1</span>]</div></span>
</code></pre>
<p>In the example above, we print out <code>['E', 'D', 'C', 'B', 'A']</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a variable called <code>backwards</code> and set it equal to the reversed version of <code>my_list</code>.</p>
<p>Make sure to reverse the list in the editor by passing your list slice a negative stride, like in the example above.</p>
</div>

```python
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]
```

### Stride Length
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left.</p>
<p>Further, a stride length of 1 traverses the list "by ones," a stride length of 2 traverses the list "by twos," and so on.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a variable, <code>backwards_by_tens</code>, and set it equal to the result of going backwards through <code>to_one_hundred</code> by tens. Go ahead and <code>print backwards_by_tens</code> to the console.</p>
</div>

```python
to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[::-10]

print(backwards_by_tens)

#Output
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
```

### Practice Makes Perfect
Great work! See? This list slicing business is pretty straightforward.

Let's do one more, just to prove you really know your stuff.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a list, <code>to_21</code>, that's just the numbers from 1 to 21, inclusive.</p>
<p>Create a second list, <code>odds</code>, that contains only the odd numbers in the <code>to_21</code> list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.</p>
<p>Finally, create a third list, <code>middle_third</code>, that's equal to the middle third of <code>to_21</code>, from 8 to 14, inclusive.</p>
</div>

```python
to_21 = [x for x in range(1,22)]
print(to_21)

odds = to_21[::2]
print(odds)

middle_third = to_21[7:14]
print(middle_third)

#output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

[8, 9, 10, 11, 12, 13, 14]
```

### Anonymous Functions
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>One of the more powerful aspects of Python is that it allows for a style of programming called <strong>functional programming</strong>, which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!</p>
<p>Check out the code at the right. See the <code>lambda</code> bit? Typing</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">lambda</span> <span class="cm-variable">x</span>:<!-- --> <span class="cm-variable">x</span> <span class="cm-operator">%</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0</span></div></span>
</code></pre>
<p>Is the same as</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">def</span> <span class="cm-def">by_three</span>(<span class="cm-variable">x</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-keyword">return</span> <span class="cm-variable">x</span> <span class="cm-operator">%</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0</span></div></span>
</code></pre>
<p>Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an <em>anonymous function</em>.</p>
<p>When we pass the lambda to <code>filter</code>, <code>filter</code> uses the lambda to determine what to filter, and the second argument (<code>my_list</code>, which is just the numbers 0 – 15) is the list it does the filtering on.</p>
</div>

###### TASK
<p>Can you guess what the this code will <code>print</code> to the console? Click Run to see.</p>

```python
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

#output 
[0, 3, 6, 9, 12, 15]
```

### Lambda Syntax

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Lambda functions are defined using the following syntax:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">my_list</span> <span class="cm-operator">=</span> <span class="cm-builtin">range</span>(<span class="cm-number">16</span>)<!-- -->
<span class="cm-builtin">filter</span>(<span class="cm-keyword">lambda</span> <span class="cm-variable">x</span>:<!-- --> <span class="cm-variable">x</span> <span class="cm-operator">%</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0</span>,<!-- --> <span class="cm-variable">my_list</span>)</div></span>
</code></pre>
<p>Lambdas are useful when you need a quick function to do some work for you.</p>
<p>If you plan on creating a function you'll use over and over, you're better off using <code>def</code> and giving that function a name.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Fill in the first part of the <code>filter</code> function with a <code>lambda</code>. The <code>lambda</code> should ensure that only <code>"Python"</code> is returned by the <code>filter</code>.</p>
<p>Fill in the second part of the <code>filter</code> function with <code>languages</code>, the list to filter.</p>
</div>

```python
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)

#output
['Python']
```

### Try It!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>All right! Time to test out <code>filter()</code> and <code>lambda</code> expressions.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">cubes</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-variable">x</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">3</span> <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">1</span>,<!-- --> <span class="cm-number">11</span>)<!-- -->]<!-- -->
<span class="cm-builtin">filter</span>(<span class="cm-keyword">lambda</span> <span class="cm-variable">x</span>:<!-- --> <span class="cm-variable">x</span> <span class="cm-operator">%</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0</span>,<!-- --> <span class="cm-variable">cubes</span>)</div></span>
</code></pre>
<p>The example above is just a reminder of the syntax.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a list, <code>squares</code>, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!</p>
<p>Use <code>filter()</code> and a <code>lambda</code> expression to <code>print</code> out only the squares that are between 30 and 70 (inclusive).</p>
</div>

```python
squares = [x ** 2 for x in range(1,11)]

print(filter(lambda x: x >= 30 and x <= 70, squares))

#output
[36, 49, 64]
```

### Iterating Over Dictionaries
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>First, let's review iterating over a <code>dict</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Call the appropriate method on <code>movies</code> such that it will <code>print</code> out all the <em>items</em> (hint, hint) in the dictionary—that is, each key and each value.</p>
</div>

```python
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print(movies.items())

#output 
[("Monty Python's Life of Brian", 'Good'), ("Monty Python's Meaning of Life", 'Okay'), ('Monty Python and the Holy Grail', 'Great')]
```

### Comprehending Comprehensions
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Good! Now let's take another look at list comprehensions.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">squares</span> <span class="cm-operator">=</span> <!-- -->[<span class="cm-variable">x</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">2</span> <span class="cm-keyword">for</span> <span class="cm-variable">x</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-number">5</span>)<!-- -->]</div></span>
</code></pre>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Use a list comprehension to create a list, <code>threes_and_fives</code>, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.</p>
</div>

```python
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
```

### List Slicing
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Great! Next up: list slicing.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-builtin">str</span> <span class="cm-operator">=</span> <span class="cm-string">"ABCDEFGHIJ"</span>
<span class="cm-variable">start</span>,<!-- --> <span class="cm-variable">end</span>,<!-- --> <span class="cm-variable">stride</span> <span class="cm-operator">=</span> <span class="cm-number">1</span>,<!-- --> <span class="cm-number">6</span>,<!-- --> <span class="cm-number">2</span>
<span class="cm-builtin">str</span>[<span class="cm-variable">start</span>:<span class="cm-variable">end</span>:<span class="cm-variable">stride</span>]</div></span>
</code></pre>
<p>You can think of a Python string as a list of characters.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The string in the editor is garbled in two ways:</p>
<ol>
<li>Our message is backwards.</li>
<li>The letter we want is every other letter.</li>
</ol>
<p>Use list slicing to extract the message and save it to a variable called <code>message</code>.</p>
</div>

```python
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message_r = garbled[::-1]
message = message_r[::2]

print(message)

#output:
I am the secret message!

Or codecademy way:

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
```

### Lambda Expressions
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Last but not least, let's look over some <code>lambda</code>s.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">my_list</span> <span class="cm-operator">=</span> <span class="cm-builtin">range</span>(<span class="cm-number">16</span>)<!-- -->
<span class="cm-builtin">filter</span>(<span class="cm-keyword">lambda</span> <span class="cm-variable">x</span>:<!-- --> <span class="cm-variable">x</span> <span class="cm-operator">%</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0</span>,<!-- --> <span class="cm-variable">my_list</span>)</div></span>
</code></pre>
<p>We've given you another (slightly different) <code>garbled</code>. Sort it out with a <code>filter()</code> and a <code>lambda</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a new variable called <code>message</code>.</p>
<p>Set it to the result of calling <code>filter()</code> with the appropriate <code>lambda</code> that will filter out the <code>"X"</code>s. The second argument will be <code>garbled</code>.</p>
<p>Finally, <code>print</code> your <code>message</code> to the console.</p>
</div>

```python
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"


message = (filter(lambda x: x != 'X', garbled))

print(message)

#output:
I am another secret message!
```
