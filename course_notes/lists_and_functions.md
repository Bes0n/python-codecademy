## Lists and Functions

### List accessing
This exercise goes over just pulling information from a list, which we've covered in a previous section!

###### TASK
Please add the code to print out the second element in the list.

```python 
n = [1, 3, 5]

# Add your code below
print(n[1])
```

### List element modification
You've already learned how to modify elements of a list in a previous section. This exercise is just a recap of that!

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>On line 3, multiply the second element of the <code>n</code> list by 5</p>
<p>Overwrite the second element with that result.</p>
<p>Make sure to print the list when you are done!</p>
</div>

```python 
n = [1, 3, 5]
# Do your multiplication here
n[1] = n[1] * 5
print n
```

### Appending to a list
<p>Here, we'll quickly recap how to <code>.append()</code> elements to the end of a list.</p>

###### TASK 
<p>Append the number 4 to the end of the list <code>n</code>.</p>

```python
n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n
```

### Removing elements from lists
<p>This exercise will expand on ways to remove items from a list. You actually have a few options. For a list called <code>n</code>:</p>

1. <p><code>n.pop(index)</code> will remove the item at <code>index</code> from the list and return it to you:</p>

```python
n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]
```

2. <p><code>n.remove(item)</code> will remove the actual <code>item</code> if it finds it:</p>

```python
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]
```

3. <p><code>del(n[1])</code> is like <code>.pop</code> in that it will remove the item at the given index, but it won't return it:</p>

```python
del(n[1])
# Doesn't return anything
print n
# prints [1, 5]
```

###### TASK
<p>Remove the first item from the list <code>n</code> using either <code>.pop()</code>, <code>.remove()</code>, or <code>del</code>.</p>

```python 
n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0) 
#or n.del(0)
#or n.remove(1)
print n
```

### Changing the functionality of a function
In this exercise, you will just be making a minor change to a function to change what that function does.

###### TASK
<p>Change the function so the given argument is multiplied by 3 and returned.</p>

```python 
number = 5

def my_function(x):
    return x * 3

print my_function(number)
```

### More than one argument
This exercise will recap how to use more than one argument in a function.

###### TASK 
<p>Define a function called <code>add_function</code> that has 2 parameters <code>x</code> and <code>y</code> and adds them together.</p>

```python 
m = 5
n = 13
# Add add_function here!
def add_function(x,y):
  return x+y

print add_function(m, n)
```

### Strings in functions
This is a basic recap on using strings in functions.

###### TASK 
<p>Write a function called <code>string_function</code> that takes in a string argument (<code>s</code>) and then <code>return</code>s that argument concatenated with the word <code>'world'</code>. Don't add a space before <code>world</code>!</p>

```python
n = "Hello"
# Your function here!
def string_function(s):
  return s + ' world'

print string_function(n)
```

### Passing a list to a function
You pass a list to a function the same way you pass any other argument to a function.

###### TASK 
Click Run to see that using a list as an argument in a function is essentially the same as using just a number or string!

```python
def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)
```

### Using an element from a list in a function
Passing a list to a function will store it in the argument (just like with a string or a number!)

```python
def first_item(items):
  print items[0]

numbers = [2, 7, 9]
first_item(numbers)
```

<ol>
<li>In the example above, we define a function called <code>first_item</code>. It has one argument called <code>items</code>.</li>
<li>Inside the function, we <code>print</code> out the item stored at index zero of <code>items</code>.</li>
<li>After the function, we create a new list called <code>numbers</code>.</li>
<li>Finally, we call the <code>first_item</code> function with <code>numbers</code> as its argument, which prints out <code>2</code>.</li>
</ol>

###### TASK
<p>Change line 2 so that <code>list_function</code> returns only the item stored in index one of <code>x</code>, rather than the entire <code>x</code> list.</p>

```python
def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)
```

### Modifying an element of a list in a function
Modifying an element in a list in a function is the same as if you were just modifying an element of a list outside a function.

```python 
def double_first(n):
  n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print numbers
```

<ol>
<li>We create a list called <code>numbers</code>.</li>
<li>We use the <code>double_first</code> function to modify that list.</li>
<li>Finally, we print out <code>[2, 2, 3, 4]</code></li>
</ol>
<p>When we pass a list to a function and modify that list, like in the <code>double_first</code> function above, we end up modifying the original list.</p>

###### TASK

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Change <code>list_function</code> to:</p>
<ul>
<li>Add 3 to the item at index <code>1</code> of the list.</li>
<li>Store the result back into index <code>1</code>.</li>
<li>Return the list. </li>
</ul>
</div>

```python
def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print list_function(n)
```

### List manipulation in functions
You can also append or delete items of a list inside a function just as if you were manipulating the list outside a function.

```python
my_list = [1, 2, 3]
my_list.append(4)
print my_list
# prints [1, 2, 3, 4]
```
The example above is just a reminder of how to append items to a list.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>list_extender</code> that has one parameter <code>lst</code>.</p>
<p>Inside the function, append the number <code>9</code> to  <code>lst</code>. </p>
<p>Then return the modified list.</p>
</div>

```python 
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst

print list_extender(n)
```

### Printing out a list item by item in a function
<p>This exercise will go over how to utilize every element in a list in a function. You can use the existing code to complete the exercise and see how running this operation inside a function isn't much different from running this operation outside a function.</p>

<p>Don't worry about the <code>range</code> function quite yet—we'll explain it later in this section.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>print_list</code> that has one argument called <code>x</code>.</p>
<p>Inside that function, print out each element one by one. Use the existing code as a scaffold.</p>
<p>Then call your function with the argument <code>n</code>. </p>
</div>

```python
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print x[i]

print_list(n)
```

### Modifying each element in a list in a function
<p>This exercise shows how to modify each element in a list. It is useful to do so in a function as you can easily put in a list of any length and get the same functionality. As you can see, <code>len(n)</code> is the length of the list.</p>

###### TASK
<p>Create a function called <code>double_list</code> that takes a single argument <code>x</code> (which will be a list) and multiplies each element by 2 and returns that list. Use the existing code as a scaffold.</p>

```python
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
# Don't forget to return your new list!

print double_list(n)
```

### Passing a range into a function
<p>Okay! Range time. The Python <code>range()</code> function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.</p>

```python 
range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]
```
<p>The <code>range</code> function has three different versions:</p>
<ol>
<li><code>range(stop)</code></li>
<li><code>range(start, stop)</code></li>
<li><code>range(start, stop, step)</code></li>
</ol>

<p>In all cases, the <code>range()</code> function returns a list of numbers from <code>start</code> up to (but not including) <code>stop</code>. Each item increases by <code>step</code>.</p>

<p>If omitted, <code>start</code> defaults to <code>0</code> and <code>step</code> defaults to <code>1</code>.</p>

###### TASK 
<p>On line 6, replace the <code>____</code> with a <code>range()</code> that returns a list containing <code>[0, 1, 2]</code>.</p>

```python 
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print my_function(range(0,3)) # Add your range between the parentheses!
```

### Iterating over a list in a function
<p>Now that we've learned about <code>range</code>, we have two ways of iterating through a list.</p>

<p><strong>Method 1</strong> - <code>for item in list</code>:</p>

```
for item in list:
  print item
```

<p><strong>Method 2</strong> - iterate through indexes:</p>

```
for i in range(len(list)):
  print list[i]
```

Method 1 is useful to loop through the list, but it's not possible to modify the list this way.

Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed. Since we aren't modifying the list, feel free to use either one on this lesson! 


###### TASK 
<p>Create a function that returns the sum of a list of numbers.</p>

<ul>
<li>On line 3, define a function called <code>total</code> that accepts one argument called <code>numbers</code>. It will be a list.</li>
<li>Inside the function, create a variable called <code>result</code> and set it to zero.</li>
<li>Using one of the two methods above, iterate through the <code>numbers</code> list. For each number, add it to <code>result</code>.</li>
<li>Finally, <code>return result</code>.</li>
</ul>

```python 
n = [3, 5, 7]

def total(numbers):
  result = 0
  for num in numbers:
    result += num
  return result
```

### Using strings in lists in functions
Now let's try working with strings!

```
for item in list:
  print item

for i in range(len(list)):
  print list[i]
```

The example above is just a reminder of the two methods for iterating over a list.

###### TASK
Create a function that concatenates strings.

<ul>
<li>Define a function called <code>join_strings</code> accepts an argument called <code>words</code>. It will be a list.</li>
<li>Inside the function, create a variable called <code>result</code> and set it to <code>""</code>, an empty string.</li>
<li>Iterate through the <code>words</code> list and concatenate each word to <code>result</code>.</li>
<li>Finally, <code>return</code> the <code>result</code>.</li>
</ul>
Don't add spaces between the joined strings!

```python 
n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
  result = ''
  for word in words:
    result += word
  return result  

print join_strings(n)
```

### Using two lists as two arguments in a function
Using multiple lists in a function is no different from just using multiple arguments in a function!

```python 
a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# prints [1, 2, 3, 4, 5, 6]
``` 

The example above is just a reminder of how to concatenate two lists.

###### TASK 
<p>Create a function that joins two lists together.</p>

<ul>
<li>On line 5, define a function called <code>join_lists</code> that has two arguments, <code>x</code> and <code>y</code>. They will both be lists.</li>
<li>Inside that function, <code>return</code> the result of concatenating <code>x</code> and <code>y</code> together.</li>
</ul>

```python 
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  return x + y

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]
```

### Using a list of lists in a function
Finally, this exercise shows how to make use of a single list that contains multiple lists and how to use them in a function.

```python 
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print item
```

<ol>
<li>In the example above, we first create a list  containing two items, each of which is a list of numbers.</li>
<li>Then, we iterate through our outer list.</li>
<li>For each of the two inner lists (as <code>lst</code>), we iterate through the numbers (as <code>item</code>) and print them out.</li>
</ol>

We end up printing out:
```
1
2
3
4
5
6
```

###### TASK

<p>Create a function called <code>flatten</code> that takes a single list and concatenates all the sublists that are part of it into a single list.</p>

<ul>
<li>On line 3, define a function called <code>flatten</code> with one argument called <code>lists</code>.</li>
<li>Make a new, empty list called <code>results</code>.</li>
<li>Iterate through <code>lists</code>. Call the looping variable <code>numbers</code>.</li>
<li>Iterate through <code>numbers</code>.</li>
<li>For each number, <code>.append()</code> it to <code>results</code>.</li>
<li>Finally, <code>return results</code> from your function.</li>
</ul>

```python 
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results    

print flatten(n)
```
