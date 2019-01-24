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

###### LESSON
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

###### LESSON

<p>Below your code, create a list called <code>students</code> that contains <code>lloyd</code>, <code>alice</code>, and <code>tyler</code>.</p>

```python 
students = [lloyd, alice, tyler]
```
