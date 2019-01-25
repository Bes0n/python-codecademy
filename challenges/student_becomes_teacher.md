## STUDENT BECOMES THE TEACHER

### Lesson Number One
<p>Welcome to this "Challenge Course". Until now we've been leading you by the hand and working on some short and relatively easy projects. This is a <strong>challenge</strong> so be ready. We have faith in you!</p>
<p>We’re going to switch it up a bit and allow you to be the teacher of your own class. Make a gradebook for all of your students.</p>

```python
animal = {
  "name": "Mr. Fluffles",
  "sounds": ["meow", "purr"]
}
print animal["name"]
```

<p>The example above is just to remind you how to create a dictionary and then to access the item stored by the <code>"name"</code> key.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create three dictionaries: <code>lloyd</code>, <code>alice</code>, and <code>tyler</code>.  </p>
<p>Give each dictionary the keys <code>"name"</code>, <code>"homework"</code>, <code>"quizzes"</code>, and <code>"tests"</code>.  </p>
<p>Have the "name" key be the name of the student (that is, <code>lloyd</code>'s name should be <code>"Lloyd"</code>) and the other keys should be an empty list (We'll fill in these lists soon!)</p>
</div>

```python
lloyd = {"name": "Lloyd", "homework": [], "quizzes": [], "tests": []}
alice = {"name": "Alice", "homework": [], "quizzes": [], "tests": []}
tyler = {"name": "Tyler", "homework": [], "quizzes": [], "tests": []}
```

### What's the Score?

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Now fill out your <code>lloyd</code> dictionary with the appropriate scores. To save you some time, we've filled out the rest for you.</p>
<p>Homework: 90.0, 97.0, 75.0, 92.0</p>
<p>Quizzes: 88.0, 40.0, 94.0</p>
<p>Test Scores: 75.0, 90.0</p>
<p><strong>Make sure to include the decimal points so your grades are stored as floats!</strong> This will be important later.</p>
</div>

```python
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
```

### Put It Together
<p>Now lets put the three dictionaries in a list together.</p>

```python 
my_list = [1, 2, 3]
```

<p>The above example is just a reminder on how to create a list. Afterwards, <code>my_list</code> contains <code>1</code>, <code>2</code>, and <code>3</code>.</p>

###### TASK

<p>Below your code, create a list called <code>students</code> that contains <code>lloyd</code>, <code>alice</code>, and <code>tyler</code>.</p>

```python 
students = [lloyd, alice, tyler]
```

### For the Record
Excellent. Now you need a hard copy document with all of your students' grades.

```python 
animal_sounds = {
  "cat": ["meow", "purr"],
  "dog": ["woof", "bark"],
  "fox": [],
}
print animal_sounds["cat"]
```

<p>The example above is just to remind you how to create a dictionary and then to access the item stored by the <code>"cat"</code> key.</p>

###### TASK

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p><code>for</code> each <code>student</code> in your <code>students</code> list, print out that <code>student</code>'s data, as follows:</p>
<ul>
<li><code>print</code> the <code>student</code>'s <code>name</code></li>
<li><code>print</code> the <code>student</code>'s <code>homework</code></li>
<li><code>print</code> the <code>student</code>'s <code>quizzes</code></li>
<li><code>print</code> the <code>student</code>'s <code>tests</code></li>
</ul>
</div>

```python
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student in students:
  print(student['name'])
  print(student['homework'])
  print(student['quizzes'])
  print(student['tests'])
  
"""
#Output 
Lloyd
[90.0, 97.0, 75.0, 92.0]
[88.0, 40.0, 94.0]
[75.0, 90.0]
Alice
[100.0, 92.0, 98.0, 100.0]
[82.0, 83.0, 91.0]
[89.0, 97.0]
Tyler
[0.0, 87.0, 75.0, 22.0]
[0.0, 75.0, 78.0]
[100.0, 100.0]
"""
```

### It's Okay to be Average
When teaching a class, it's important to take the students' averages in order to assign grades.

```python
5 / 2
# 2

5.0 / 2
# 2.5

float(5) / 2
# 2.5
```

The above example is a reminder of how division works in Python.
<ul>
<li>When you divide an integer by another integer, the result is always an integer (rounded down, if needed).</li>
<li>When you divide a float by an integer, the result is always a float.</li>
<li>To divide two integers and end up with a float, you must first use <code>float()</code> to convert one of the integers to a float.</li>
</ul>

###### TASK
<p>Write a function <code>average</code> that takes a list of numbers and returns the average.</p>
<ul>
<li>Define a function called <code>average</code> that has one argument, <code>numbers</code>.</li>
<li>Inside that function, call the built-in <code>sum()</code> function with the <code>numbers</code> list as a parameter. Store the result in a variable called <code>total</code>.</li>
<li>Like the example above, use <code>float()</code> to convert <code>total</code> and store the result in <code>total</code>.</li>
<li>Divide <code>total</code> by the length of the <code>numbers</code> list. Use the built-in <code>len()</code> function to calculate that.</li>
<li>Return that result.</li>
</ul>

```python
def average(numbers):
  total = sum(numbers)
  total = float(total) / len(numbers)
  return total
```

### Just Weight and See
Great! Now we need to compute a student’s average using weighted averages.

```python
cost = {
    "apples": [3.5, 2.4, 2.3],
    "bananas": [1.2, 1.8],
}

return 0.9 * average(cost["apples"]) + \
0.1 * average(cost["bananas"])
```

<ol>
<li>In the above example, we create a dictionary called <code>cost</code> that contains the costs of some fruit.</li>
<li>Then, we calculate the average cost of apples and the average cost of bananas. Since we like apples much more than we like bananas, we weight the average cost of apples by 90% and the average cost of bananas by 10%.</li>
</ol>

<p>The <code>\</code> character is a <em>continuation character</em>. The following line is considered a <em>continuation</em> of the current line.</p>

