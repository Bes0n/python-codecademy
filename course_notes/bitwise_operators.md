## INTRODUCTION TO BITWISE OPERATORS
### Just a Little BIT
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Welcome to an intro level explanation of bitwise operations in Python!</p>
<p>Bitwise operations might seem a little esoteric and tricky at first, but you'll get the hang of them pretty quickly.</p>
<p><em>Bitwise operations</em> are operations that directly manipulate <em>bits</em>. In all computers, numbers are represented with bits, a series of zeros and ones. In fact, pretty much everything in a computer is represented by bits. This course will introduce you to the basic bitwise operations and then show you what you can do with them.</p>
<p>Bitwise operators often tend to puzzle and mystify new programmers, so don't worry if you are a little bit confused at first. To be honest, you aren't really going to see bitwise operators in everyday programming. However, they do pop up from time to time, and when they do, you should have a general idea of what is going on.  </p>
</div>

###### TASK
In the editor are the 6 basic bitwise operations. Click Run and see what the console prints out. All of them will be explained in due time!

```python
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

#output 
0
10
0
13
38
-89
```

### Lesson I0: The Base 2 Number System
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>When we count, we usually do it in base 10. That means that each place in a number can hold one of ten values, 0-9. In binary we count in base two, where each place can hold one of two values: 0 or 1. The counting pattern is the same as in base 10 except when you carry over to a new column, you have to carry over every time a place goes higher than one (as opposed to higher than 9 in base 10).</p>
<p>For example, the numbers one and zero are the same in base 10 and base 2. But in base 2, once you get to the number 2 you have to carry over the one, resulting in the representation "10". Adding one again results in "11" (3) and adding one again results in "100" (4).</p>
<p>Contrary to counting in base 10, where each decimal place represents a power of 10, each place in a binary number represents a power of two (or a <strong>bit</strong>). The rightmost bit is the 1's bit (two to the zero power), the next bit is the 2's bit (two to the first), then 4, 8, 16, 32, and so on.</p>
<p>The binary number '1010' is 10 in base 2 because the 8's bit and the 2's bit are "on":</p>
<pre><code><span class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror">8's bit  4's bit  2's bit  1's bit<!-- -->
<!-- -->    1       0       1      0 <!-- -->
<!-- -->    8   +   0    +  2   +  0  = 10 </div></span>
</code></pre><p>In Python, you can write numbers in binary format by starting the number with <code>0b</code>. When doing so, the numbers can be operated on like any other number!</p>
</div>

```python
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

#output: 
1 2 3 4 5 6 7
******
4
9
```

### I Can Count to 1100!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>All right! Time to practice counting in binary.</p>
<p>To make sure you've got the hang of it, fill out the rest of the numbers all the way up to twelve. Please <strong>do not</strong> use the str() method or any other outside functions.</p>
<p>Here are a few numbers that will be good to know going forward - </p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">0</span> <span class="cm-operator">=</span> <span class="cm-number">1</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">1</span> <span class="cm-operator">=</span> <span class="cm-number">2</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">2</span> <span class="cm-operator">=</span> <span class="cm-number">4</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">3</span> <span class="cm-operator">=</span> <span class="cm-number">8</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">4</span> <span class="cm-operator">=</span> <span class="cm-number">16</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">5</span> <span class="cm-operator">=</span> <span class="cm-number">32</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">6</span> <span class="cm-operator">=</span> <span class="cm-number">64</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">7</span> <span class="cm-operator">=</span> <span class="cm-number">128</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">8</span> <span class="cm-operator">=</span> <span class="cm-number">256</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">9</span> <span class="cm-operator">=</span> <span class="cm-number">512</span>
<span class="cm-number">2</span> <span class="cm-operator">*</span><span class="cm-operator">*</span> <span class="cm-number">10</span> <span class="cm-operator">=</span> <span class="cm-number">1024</span></div></span>
</code></pre>
<p>You may recognize these numbers. Do you have a 32 or 64 bit system? Does your computer have a 256GB hard drive? Computers think in binary!</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Fill out the rest of the numbers with their corresponding binary values up to twelve in the editor to the right, using the <code>0bxxx</code> format.</p>
</div>

```python
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
```

### The bin() Function
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Excellent! The biggest hurdle you have to jump over in order to understand bitwise operators is learning how to count in base 2. Hopefully the lesson should be easier for you from here on out. </p>
<p>There are Python functions that can aid you with bitwise operations. In order to print a number in its binary representation, you can use the <code>bin()</code> function. <code>bin()</code> takes an integer as input and returns the binary representation of that integer in a string. (Keep in mind that after using the <code>bin</code> function, you can no longer operate on the value like a number.) </p>
<p>You can also represent numbers in base 8 and base 16 using the <code>oct()</code> and <code>hex()</code> functions. (We won't be dealing with those here, however.)</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>We've provided an example of the <code>bin</code> function in the editor. Go ahead and use <code>print</code> and <code>bin()</code> to print out the binary representations of the numbers 2 through 5, each on its own line.</p>
</div>

```python
print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

#output
0b1
0b10
0b11
0b100
0b101
```

### int()'s Second Parameter
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Python has an <code>int()</code> function that you've seen a bit of already. It can turn non-integer input into an integer, like this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-builtin">int</span>(<span class="cm-string">"42"</span>)<!-- -->
<span class="cm-comment"># ==&gt; 42</span></div></span>
</code></pre>
<p>What you might not know is that the <code>int</code> function actually has an optional second parameter.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-builtin">int</span>(<span class="cm-string">"110"</span>,<!-- --> <span class="cm-number">2</span>)<!-- -->
<span class="cm-comment"># ==&gt; 6</span></div></span>
</code></pre>
<p>When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.</p>
</div>

###### TASK
<p>In the console are several different ways that you can use the <code>int</code> function's second parameter.On line 7, use <code>int</code> to <code>print</code> the base 10 equivalent of the binary number 11001001.</p>

```python
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)

#output: 
1
2
7
4
5
201
```

### Slide to the Left! Slide to the Right!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The next two operations we are going to talk about are the left and right shift bitwise operators. These operators work by shifting the bits of a number over by a designated number of slots.</p>
<p>The block below shows how these operators work on the bit level. Note that in the diagram, the shift is always a positive integer:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-comment"># Left Bit Shift (&lt;&lt;)  </span>
<span class="cm-number">0b000001</span> <span class="cm-operator">&lt;&lt;</span> <span class="cm-number">2</span> <span class="cm-operator">==</span> <span class="cm-number">0b000100</span> <!-- -->(<span class="cm-number">1</span> <span class="cm-operator">&lt;&lt;</span> <span class="cm-number">2</span> <span class="cm-operator">=</span> <span class="cm-number">4</span>)<!-- -->
<span class="cm-number">0b000101</span> <span class="cm-operator">&lt;&lt;</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0b101000</span> <!-- -->(<span class="cm-number">5</span> <span class="cm-operator">&lt;&lt;</span> <span class="cm-number">3</span> <span class="cm-operator">=</span> <span class="cm-number">40</span>)<!-- -->       <!-- -->
<!-- -->
<span class="cm-comment"># Right Bit Shift (&gt;&gt;)</span>
<span class="cm-number">0b0010100</span> <span class="cm-operator">&gt;&gt;</span> <span class="cm-number">3</span> <span class="cm-operator">==</span> <span class="cm-number">0b000010</span> <!-- -->(<span class="cm-number">20</span> <span class="cm-operator">&gt;&gt;</span> <span class="cm-number">3</span> <span class="cm-operator">=</span> <span class="cm-number">2</span>)<!-- -->
<span class="cm-number">0b0000010</span> <span class="cm-operator">&gt;&gt;</span> <span class="cm-number">2</span> <span class="cm-operator">==</span> <span class="cm-number">0b000000</span> <!-- -->(<span class="cm-number">2</span> <span class="cm-operator">&gt;&gt;</span> <span class="cm-number">2</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>)</div></span>
</code></pre>
<p>Shift operations are similar to rounding down after dividing and multiplying by 2 (respectively) for every time you shift, but it's often easier just to think of it as shifting all the 1s and 0s left or right by the specified number of slots.</p>
<p>Note that you can only do bitwise operations on an <strong>integer</strong>. Trying to do them on strings or floats will result in nonsensical output!</p>
</div>

###### TASK
<p>Shift the variable <code>shift_right</code> to the right twice (<code>&gt;&gt; 2</code>) and shift the variable <code>shift_left</code> to the left twice (<code>&lt;&lt; 2</code>). Try to guess what the <code>print</code>ed output will be!</p>

```python
shift_right = 0b1100 >> 2
shift_left = 0b1 << 2

# Your code here!
print bin(shift_right)
print bin(shift_left)

#output 
0b11
0b100
```

### A BIT of This AND That
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The bitwise AND (<code>&amp;</code>) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of <strong>both</strong> numbers are 1. For example: </p>
<pre><code><span class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror">     a:   00101010   42<!-- -->
<!-- -->     b:   00001111   15       <!-- -->
<!-- -->===================<!-- -->
<!-- --> a &amp; b:   00001010   10</div></span>
</code></pre><p>As you can see, the 2's bit and the 8's bit are the only bits that are on in both <code>a</code> and <code>b</code>, so <code>a &amp; b</code> only contains those bits. Note that using the <code>&amp;</code> operator can only result in a number that is less than or equal to the smaller of the two values.</p>
<p>So remember, for every given bit in <code>a</code> and <code>b</code>:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-number">0</span> <span class="cm-operator">&amp;</span> <span class="cm-number">0</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>
<span class="cm-number">0</span> <span class="cm-operator">&amp;</span> <span class="cm-number">1</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>
<span class="cm-number">1</span> <span class="cm-operator">&amp;</span> <span class="cm-number">0</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>
<span class="cm-number">1</span> <span class="cm-operator">&amp;</span> <span class="cm-number">1</span> <span class="cm-operator">=</span> <span class="cm-number">1</span></div></span>
</code></pre>
<p>Therefore,</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-number">0b111</span> <!-- -->(<span class="cm-number">7</span>)<!-- --> <span class="cm-operator">&amp;</span> <span class="cm-number">0b1010</span> <!-- -->(<span class="cm-number">10</span>)<!-- --> <span class="cm-operator">=</span> <span class="cm-number">0b10</span></div></span>
</code></pre>
<p>which equals two.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p><code>print</code> out the result of calling <code>bin()</code> on  <code>0b1110 &amp; 0b101</code>.</p>
<p>See if you can guess what the output will be!</p>
</div>

```python
print bin(0b1110 & 0b101)

#output
0b100
```

### A BIT of This OR That
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The bitwise OR (<code>|</code>) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if <strong>either</strong> of the corresponding bits of either number are 1. For example:</p>
<pre><code><span class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror">    a:  00101010  42<!-- -->
<!-- -->    b:  00001111  15       <!-- -->
<!-- -->================<!-- -->
<!-- -->a | b:  00101111  47</div></span>
</code></pre><p>Note that the bitwise <code>|</code> operator can only create results that are greater than or equal to the larger of the two integer inputs.</p>
<p>So remember, for every given bit in <code>a</code> and <code>b</code>:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-number">0</span> <span class="cm-operator">|</span> <span class="cm-number">0</span> <span class="cm-operator">=</span> <span class="cm-number">0</span>
<span class="cm-number">0</span> <span class="cm-operator">|</span> <span class="cm-number">1</span> <span class="cm-operator">=</span> <span class="cm-number">1</span> <!-- -->
<span class="cm-number">1</span> <span class="cm-operator">|</span> <span class="cm-number">0</span> <span class="cm-operator">=</span> <span class="cm-number">1</span>
<span class="cm-number">1</span> <span class="cm-operator">|</span> <span class="cm-number">1</span> <span class="cm-operator">=</span> <span class="cm-number">1</span></div></span>
</code></pre>
<p>Meaning</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-number">110</span> <!-- -->(<span class="cm-number">6</span>)<!-- --> <span class="cm-operator">|</span> <span class="cm-number">1010</span> <!-- -->(<span class="cm-number">10</span>)<!-- --> <span class="cm-operator">=</span> <span class="cm-number">1110</span> <!-- -->(<span class="cm-number">14</span>)</div></span>
</code></pre>
</div>

###### TASK
<p>For practice, <code>print</code> out the result of using <code>|</code> on <code>0b1110</code> and <code>0b101</code> as a binary string. Try to do it on your own without using the <code>|</code> operator if you can help it.</p>

```python
print( bin(0b1110 | \
           0b0101))
           
#output 
0b1111
```

### This XOR That?
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The XOR (<code>^</code>) or <em>exclusive or</em> operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if <strong>either</strong> of the corresponding bits of the two numbers are 1, <strong>but not both</strong>.</p>
<pre><code><span class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror">    a:  00101010   42<!-- -->
<!-- -->    b:  00001111   15       <!-- -->
<!-- -->================<!-- -->
<!-- -->a ^ b:  00100101   37</div></span>
</code></pre><p>Keep in mind that if a bit is off in both numbers, it stays off in the result. Note that XOR-ing a number with itself will always result in 0.</p>
<p>So remember, for every given bit in <code>a</code> and <code>b</code>:</p>
<pre><code><span class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror">0 ^ 0 = 0<!-- -->
<!-- -->0 ^ 1 = 1<!-- -->
<!-- -->1 ^ 0 = 1<!-- -->
<!-- -->1 ^ 1 = 0</div></span>
</code></pre><p>Therefore:</p>
<pre><code><span class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"> 111 (7) ^ 1010 (10) = 1101 (13)</div></span>
</code></pre></div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>For practice, <code>print</code> the result of using <code>^</code> on <code>0b1110</code> and <code>0b101</code> as a binary string. Try to do it on your own without using the <code>^</code> operator.</p>
</div>

```python
print(bin(0b1110 ^ \
          0b0101))

#output 0b1011
```

### See? This is NOT That Hard!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The bitwise NOT operator (<code>~</code>) just flips all of the bits in a single number. What this actually means to the computer is actually very complicated, so we're not going to get into it. Just know that mathematically, this is equivalent to adding one to the number and then making it negative. </p>
<p>And with that, you've seen all of the basic bitwise operators! We'll see what we can do with these in the next section. </p>
</div>

###### TASK
Click Run and observe what the console prints out.

```python
print ~1
print ~2
print ~3
print ~42
print ~123

#output
-2
-3
-4
-43
-124
```

### The Man Behind the Bit Mask
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>A <em>bit mask</em> is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">num</span>  <span class="cm-operator">=</span> <span class="cm-number">0b1100</span>
<span class="cm-variable">mask</span> <span class="cm-operator">=</span> <span class="cm-number">0b0100</span>
<span class="cm-variable">desired</span> <span class="cm-operator">=</span> <span class="cm-variable">num</span> <span class="cm-operator">&amp;</span> <span class="cm-variable">mask</span>
<span class="cm-keyword">if</span> <span class="cm-variable">desired</span> <span class="cm-operator">&gt;</span> <span class="cm-number">0</span>:<!-- -->
<!-- -->  <span class="cm-builtin">print</span> <span class="cm-string">"Bit was on"</span></div></span>
</code></pre>
<p>In the example above, we want to see if the third bit from the right is on.</p>
<ol>
<li>First, we first create a variable <code>num</code> containing the number 12, or <code>0b1100</code>.</li>
<li>Next, we create a <code>mask</code> with the third bit on.</li>
<li>Then, we use a bitwise-and operation to see if the third bit from the right of <code>num</code> is on.</li>
<li>If <code>desired</code> is greater than zero, then the third bit of <code>num</code> must have been one.</li>
</ol>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function, <code>check_bit4</code>, with one argument, <code>input</code>, an integer.</p>
<p>It should check to see if the fourth bit from the right is on.</p>
<p>If the bit is on, <code>return "on"</code> (not <code>print</code>!)</p>
<p>If the bit is off,  <code>return "off"</code>.</p>
<p>Check the Hint for some examples!</p>
</div>


```python
def check_bit4(inp):
  mask = 0b1000
  desired = inp & mask
  if desired > 0: 
    return "on"
  else:
    return "off"
    
```

### Turn It On
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>You can also use masks to turn a bit in a number on using <code>|</code>. For example, let's say I want to make sure the rightmost bit of number <code>a</code> is turned on. I could do this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">a</span> <span class="cm-operator">=</span> <span class="cm-number">0b110</span> <span class="cm-comment"># 6</span>
<span class="cm-variable">mask</span> <span class="cm-operator">=</span> <span class="cm-number">0b1</span> <span class="cm-comment"># 1</span>
<span class="cm-variable">desired</span> <span class="cm-operator">=</span>  <span class="cm-variable">a</span> <span class="cm-operator">|</span> <span class="cm-variable">mask</span> <span class="cm-comment"># 0b111, or 7</span></div></span>
</code></pre>
<p>Using the bitwise <code>|</code> operator will turn a corresponding bit on if it is off and leave it on if it is already on.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>In the editor is a variable, <code>a</code>. Use a bitmask and the value <code>a</code> in order to achieve a result where the third bit from the right of a is turned on. Be sure to <code>print</code> your answer as a <code>bin()</code> string!</p>
</div>

```python
a = 0b10111011
mask = 0b100
desired = a | mask

print(bin(desired))
```

### Just Flip Out
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Using the XOR (<code>^</code>) operator is very useful for flipping bits. Using <code>^</code> on a bit with the number one will return a result where that bit is flipped. </p>
<p>For example, let's say I want to flip all of the bits in <code>a</code>. I might do this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">a</span> <span class="cm-operator">=</span> <span class="cm-number">0b110</span> <span class="cm-comment"># 6</span>
<span class="cm-variable">mask</span> <span class="cm-operator">=</span> <span class="cm-number">0b111</span> <span class="cm-comment"># 7</span>
<span class="cm-variable">desired</span> <span class="cm-operator">=</span>  <span class="cm-variable">a</span> <span class="cm-operator">^</span> <span class="cm-variable">mask</span> <span class="cm-comment"># 0b1</span></div></span>
</code></pre>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>In the editor is the 8 bit variable <code>a</code>. Use a bitmask and the value <code>a</code> in order to achieve a result where all of the bits in <code>a</code> are flipped. Be sure to print your answer as a <code>bin()</code> string!</p>
</div>

```python
a = 0b11101110
mask = 0b11111111
desired = a ^ mask 

print(bin(desired))

#output 
0b10001
```

### Slip and Slide
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Finally, you can also use the left shift (<code>&lt;&lt;</code>) and right shift (<code>&gt;&gt;</code>) operators to slide masks into place.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">a</span> <span class="cm-operator">=</span> <span class="cm-number">0b101</span> <!-- -->
<span class="cm-comment"># Tenth bit mask</span>
<span class="cm-variable">mask</span> <span class="cm-operator">=</span> <!-- -->(<span class="cm-number">0b1</span> <span class="cm-operator">&lt;&lt;</span> <span class="cm-number">9</span>)<!-- -->  <span class="cm-comment"># One less than ten </span>
<span class="cm-variable">desired</span> <span class="cm-operator">=</span> <span class="cm-variable">a</span> <span class="cm-operator">^</span> <span class="cm-variable">mask</span></div></span>
</code></pre>
<p>Let's say that I want to turn on the 10th bit from the right of the integer <code>a</code>.</p>
<p>Instead of writing out the entire number, we  slide a bit over using the <code>&lt;&lt;</code> operator.</p>
<p>We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>flip_bit</code> that takes the inputs <code>(number, n)</code>.</p>
<p>Flip the nth bit (with the ones bit being the first bit) and store it in <code>result</code>.</p>
<p>Return the result of calling <code>bin(result)</code>.</p>
</div>

```python
def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)
```
