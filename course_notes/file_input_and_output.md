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
