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
