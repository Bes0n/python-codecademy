## Exam Statistics
### Let's look at those grades!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Creating a program to compute statistics means that you won't have to whip out your calculator and manually crunch numbers. All you'll have to do is supply a new set of numbers and our program does all of the hard work. </p>
<p>This mini-project will give you some practice with functions, lists, and translating mathematical formulae into programming statements.</p>
<p>In order to use the scores in our program, we'll need them in a container, namely a list.</p>
<p>On the right, you'll see the grades <em>listed</em> (see what I did there). The data is anonymous to protect the privacy of the students. </p>
</div>

### Print those grades
As a refresher, let's start off by writing a function to print out the list of grades, one element at a time.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function on line 3 called <code>print_grades</code> with one argument, a list called <code>grades_input</code>.</p>
<p>Inside the function, iterate through <code>grades_input</code> and print each item on its own line.</p>
<p>After your function, call <code>print_grades</code> with the <code>grades</code> list as the parameter.</p>
</div>

```python
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for item in grades_input:
    print(item)
    
print(print_grades(grades))
```

### Review
So far, you've created a helper function that will be used in the next sections.

You also have a solid handle on the concepts that we'll need to continue.

The next step in the creation of our grade statistics program involves computing the mean (average) of the grades.

### The sum of scores
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Now that we have a function to print the grades, let's create another function to compute the sum of all of the test grades. </p>
<p>This will be super-helpful when we need to compute the average score.</p>
<p>I know what you're thinking, "let's just use the built-in <code>sum</code> function!" The built-in function would work beautifully, but it would be too easy. </p>
<p>Computing the sum manually involves computing a rolling sum. As you loop through the list, add the current grade to a variable that keeps track of the total, let's call that variable <code>total</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>On line 3, define a function, <code>grades_sum</code>, that does the following:</p>
<ul>
<li>Takes in a list of scores, <code>scores</code></li>
<li>Computes the sum of the scores</li>
<li>Returns the computed sum.</li>
</ul>
<p>Call the newly created <code>grades_sum</code> function with the list of <code>grades</code> and <code>print</code> the result.</p>
</div>

```python
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for item in scores:
    total += item
  return total

print(grades_sum(grades))
```

### Computing the Average
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>The average test grade can be found by dividing the sum of the grades by the total number of grades.</p>
<p>Luckily, we just created an awesome function, <code>grades_sum</code> to compute the sum.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function, <code>grades_average</code>, below the <code>grades_sum</code> function that does the following: </p>
<ul>
<li>Has one argument, <code>grades_input</code>, a list</li>
<li>Calls <code>grades_sum</code> with <code>grades_input</code></li>
<li>Computes the average of the grades by dividing that sum by <code>float(len(grades_input))</code>.</li>
<li>Returns the average.</li>
</ul>
<p>Call the newly created <code>grades_average</code> function with the list of <code>grades</code> and <strong>print the result</strong>.</p>
</div>

```python
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for item in scores:
    total += item
  return total

def grades_average(grades_input):
  average = grades_sum(grades_input) / float(len(grades_input))
  return average

print(grades_average(grades))
```

### The Variance
Let's see how the grades varied against the average. This is called computing the variance.

A very large variance means that the students' grades were all over the place, while a small variance (relatively close to the average) means that the majority of the students had similar grades.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>On line 18, define a new function called <code>grades_variance</code> that accepts one argument, <code>scores</code>, a list.</p>
<p>First, create a variable <code>average</code> and store the result of calling <code>grades_average(scores)</code>.</p>
<p>Next, create another variable <code>variance</code> and set it to zero. We will use this as a rolling sum.</p>
<p><code>for</code> each <code>score in scores:</code> Compute its squared difference: <code>(average - score) ** 2</code> and add that to <code>variance</code>.</p>
<p>Divide the total <code>variance</code> by the number of <code>scores</code>.</p>
<p>Then, return that result.</p>
<p>Finally, after your function code, <code>print grades_variance(grades)</code>.</p>
</div>

```python
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  variance = 0
  average = grades_average(scores)
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)

print(grades_variance(grades))
```

### Standard Deviation
Great job computing the variance! The last statistic will be much simpler: standard deviation.

The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.
###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function, <code>grades_std_deviation</code>, that takes one argument called <code>variance</code>.</p>
<p><code>return</code> the result of <code>variance ** 0.5</code></p>
<p>After the function, create a new variable called <code>variance</code> and store the result of calling <code>grades_variance(grades)</code>.</p>
<p>Finally <code>print</code> the result of calling <code>grades_std_deviation(variance)</code>.</p>
</div>

```python
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  variance = 0
  average = grades_average(scores)
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)

def grades_std_deviation(variance):
  return variance ** 0.5 

variance = grades_variance(grades)

print(grades_std_deviation(variance))
```

### Review
You've done a great job completing this program.

We've created quite a few meaningful functions. Namely, we've created helper functions to print a list of grades, compute the sum, average, variance, and standard deviation about a set of grades.

Let's wrap up by printing out all of the statistics.

Who needs to pay for grade calculation software when you can write your own? :)

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Print out the following: </p>
<ul>
<li>all of the grades</li>
<li>sum of grades</li>
<li>average grade</li>
<li>variance</li>
<li>standard deviation  </li>
</ul>
</div>

```python
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  variance = 0
  average = grades_average(scores)
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)

def grades_std_deviation(variance):
  return variance ** 0.5 

variance = grades_variance(grades)

print(print_grades(grades))
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
```

