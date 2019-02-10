## FILE INPUT/OUTPUT
### See It to Believe It
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Until now, the Python code you've been writing comes from one source and only goes to one place: you type it in at the keyboard and its results are displayed in the console. But what if you want to read information from a file on your computer, and/or write that information to another file?</p>
<p>This process is called <em>file I/O</em> (the "I/O" stands for "input/output"), and Python has a number of built-in functions that handle this for you.</p>
<p>Check out the code in the editor to the right.</p>
</div>

###### TASK
<p>Click Run! You just wrote all the contents of <code>my_list</code> to a text file called <code>output.txt</code>.</p>

```python
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

```

### The open() Function
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Let's walk through the process of writing to a file one step at a time.</p>
<p>The first code that you saw executed in the previous exercise was this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">f</span> <span class="cm-operator">=</span> <span class="cm-builtin">open</span>(<span class="cm-string">"output.txt"</span>,<!-- --> <span class="cm-string">"w"</span>)</div></span>
</code></pre>
<p>This told Python to open <code>output.txt</code> in <code>"w"</code> mode ("w" stands for "write"). We stored the result of this operation in a file object, <code>f</code>.</p>
<p>Doing this opens the file in write-mode and prepares Python to send data into the file.</p>
</div>

###### TASK
<p>Create a variable, <code>my_file</code>, and set it equal to calling the <code>open()</code> function on <code>output.txt</code>. In this case, pass <code>"r+"</code> as a second argument to the function so the file will allow you to read <em>and</em> write to it! (See the Hint for details.)</p>

```python
my_file = open("output.txt", "r+")
```

### Writing
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Good work! Now it's time to write some data to a new <code>.txt</code> file.</p>
<p>We added the list comprehension from the first exercise to the code in the editor. Our goal in this exercise will be to write each element of that list to a file called <code>output.txt</code>. The <code>output.txt</code> file that you write to will be created in your current folder - for simplicity, the folder has been hidden. <code>output.txt</code> will list each number on its own line.</p>
<p>We can write to a Python file like so:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">my_file</span>.<span class="cm-property">write</span>(<span class="cm-string">"Data to be written"</span>)</div></span>
</code></pre>
<p>The <code>.write()</code> method takes a string argument, so we'll need to do a few things here:</p>
<p>You must close the file. You do this simply by calling <code>my_file.close()</code> (we did this for you in the last exercise). If you don't close your file, Python <em>won't</em> write to it properly. From here on out, you gotta close your files!</p>
</div>

<div class="theme__22QeW-d-YRjfwg7z9oiZH_ hintBody__Xlfb7YxNNyRdyb2SB9sb1"><p>You can open files in any of the following modes:</p>
<ul>
<li>write-only mode (<code>"w"</code>)</li>
<li>read-only mode (<code>"r"</code>)</li>
<li>read and write mode (<code>"r+"</code>)</li>
<li>append mode (<code>"a"</code>), which adds any new data you write to the file to the end of the file.</li>
</ul>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Iterate over <code>my_list</code> to get each value.</p>
<p>Use <code>my_file.write()</code> to write each value to a text file called, <code>output.txt</code>.</p>
<p>Make sure to call <code>str()</code> on the iterating data so <code>.write()</code> will accept it.</p>
<p>Make sure to add a newline (<code>+ "\n"</code>) after each element to ensure each will appear on its own line.</p>
<p>Use <code>my_file.close()</code> to close the file when you're done.</p>
<p>Passing the exercise means that you successfully wrote <code>my_list</code> to <code>output.txt</code>!</p>
</div>

```python
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!

for item in my_list:
  my_file.write(str(item) + "\n")
my_file.close()
```

### Reading
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Excellent! You're a pro.</p>
<p>Finally, we want to know how to read from our <code>output.txt</code> file. As you might expect, we do this with the <code>read()</code> function, like so:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-builtin">print</span> <span class="cm-variable">my_file</span>.<span class="cm-property">read</span>(<!-- -->)</div></span>
</code></pre>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Declare a variable, <code>my_file</code>, and set it equal to the file object returned by calling <code>open()</code> with both <code>"output.txt"</code> and <code>"r"</code>.</p>
<p>Next, <code>print</code> the result of using <code>.read()</code> on <code>my_file</code>, like the example above.</p>
<p>Make sure to <code>.close()</code> your file when you're done with it! All kinds of doom will happen if you don't.</p>
</div>

```python
my_file = open("output.txt", "r")

print(my_file.read())

my_file.close()
```

### Reading Between the Lines
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>What if we want to read from a file line by line, rather than pulling the entire file in at once. Thankfully, Python includes a <code>.readline()</code> method that does exactly that.</p>
<p>If you open a file and call <code>.readline()</code> on the file object, you'll get the first line of the file; subsequent calls to <code>.readline()</code> will return successive lines.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Declare a new variable <code>my_file</code> and store the result of calling <code>open()</code> on the <code>"text.txt"</code> file in <code>"r"</code>ead-only mode.</p>
<p>On three separate lines, <code>print</code> out the result of calling <code>my_file.readline()</code>. See how it gets the next line each time?</p>
<p>Don't forget to <code>.close()</code> your file when you're done with it!</p>
</div>

```python
my_file = open("text.txt", "r")

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()

#output:
I'm the first line of the file!

I'm the second line.

Third line here, boss.
```

### PSA: Buffering Data
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>We keep telling you that you always need to close your files after you're done writing to them. Here's why!</p>
<p>During the I/O process, data is <em>buffered</em>: this means that it is held in a temporary location before being written to the file.</p>
<p>Python doesn't <em>flush the buffer</em>—that is, write data to the file—until it's sure you're done writing. One way to do this is to close the file. If you write to a file without closing, the data won't make it to the target file.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Check out our <em>extremely bad</em> code in the editor. Click Run—you'll note that our <code>read_file.read()</code> didn't read any data back! </p>
<ul>
<li>Add a <code>write_file.close()</code> call after writing to the file but before reading it.</li>
<li>Add a <code>read_file.close()</code> call after the <code>print read_file.read()</code> line</li>
<li>Run the code again.</li>
<li>This time, you'll see the data come through!</li>
</ul>
</div>

```python
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()

read_file.close()
```

### The 'with' and 'as' Keywords
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Programming is all about getting the computer to do the work. Is there a way to get Python to automatically close our files for us?</p>
<p>Of course there is. This is Python.</p>
<p>You may not know this, but file objects contain a special pair of built-in methods: <code>__enter__()</code> and <code>__exit__()</code>. The details aren't important, but what <em>is</em> important is that when a file object's <code>__exit__()</code> method is invoked, it automatically closes the file. How do we invoke this method? With <code>with</code> and <code>as</code>.</p>
<p>The syntax looks like this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">with</span> <span class="cm-builtin">open</span>(<span class="cm-string">"file"</span>,<!-- --> <span class="cm-string">"mode"</span>)<!-- --> <span class="cm-keyword">as</span> <span class="cm-variable">variable</span>:<!-- -->
<!-- -->  <span class="cm-comment"># Read or write to the file</span></div></span>
</code></pre>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Check out the example in the editor. Note that we don't explicitly <code>close()</code> our file, and remember that if we don't close a file, our data will get stuck in the buffer. Click Run! </p>
<p><code>Success!</code> is written to a file called <code>text.txt</code>.</p>
</div>

```python
with open("text.txt", "w") as textfile:
  textfile.write("Success!")
```

### Try It Yourself
<p>It worked! Our Python program successfully wrote to <code>text.txt</code>.</p>

###### TASK
<p>Now you try: write any data you like to a file called <code>text.txt</code> using <code>with</code>...<code>as</code>. Give your file object the usual name: <code>my_file</code>.</p>

```python
with open("text.txt", "w") as my_file:
  my_file.write("It works!")
```

### Case Closed?
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Finally, we'll want a way to test whether a file we've opened is closed. Sometimes we'll have a lot of file objects open, and if we're not careful, they won't all be closed. How can we test this?</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">f</span> <span class="cm-operator">=</span> <span class="cm-builtin">open</span>(<span class="cm-string">"bg.txt"</span>)<!-- -->
<span class="cm-variable">f</span>.<span class="cm-property">closed</span>
<span class="cm-comment"># False</span>
<span class="cm-variable">f</span>.<span class="cm-property">close</span>(<!-- -->)<!-- -->
<span class="cm-variable">f</span>.<span class="cm-property">closed</span>
<span class="cm-comment"># True</span></div></span>
</code></pre>
<p>Python file objects have a <code>closed</code> attribute which is <code>True</code> when the file is closed and <code>False</code> otherwise.</p>
<p>By checking <code>file_object.closed</code>, we'll know whether our file is closed and can call <code>close()</code> on it if it's still open.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Below your <code>with</code>...<code>as</code> code, do two things:</p>
<ul>
<li>Check <code>if</code> the file is not <code>closed</code>.</li>
<li>If that's the case, call <code>.close()</code> on it.</li>
<li>(You don't need an <code>else</code> here, since your <code>if</code> statement should do nothing if <code>closed</code> is <code>True</code>.)</li>
<li>After your <code>if</code> statement, <code>print</code> out the value of <code>my_file.closed</code> to make sure your file is really closed.</li>
</ul>
</div>

```python
with open("text.txt", "w") as my_file:
  my_file.write("It works!")
  
if my_file.closed == False:
  my_file.close()
  
print(my_file.closed)  

#output:
True
```
