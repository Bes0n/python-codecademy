## Python Lists and Dictionaries

### Introduction to Lists
Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name. (Datatypes you've already learned about include strings, numbers, and booleans.)

You can assign items to a list with an expression of the form
```python
list_name = [item_1, item_2]
```
with the items in between brackets. A list can also be empty: ```empty_list = [].```

Lists are very similar to strings, but there are a few key differences. 

1. The list zoo_animals has three items (check them out on line 1). Go ahead and add a fourth! Just enter the name of your favorite animal (as a "string") on line 1, after the final comma but before the closing ].

```python
zoo_animals = ["pangolin", "cassowary", "sloth", "wolf"];

# One animal is missing!
if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]
```

### Access by Index
You can access an individual item on the list by its index. An index is like an address that identifies the item's place in the list. The index appears directly after the list name, in between brackets, like this: ```list_name[index].```

List indices begin with 0, not 1! You access the first item in a list like this: ```list_name[0]```. The second item in a list is at index 1: ```list_name[1]```. Computer scientists love to start counting from zero.

1. Write a statement that prints the result of adding the second and fourth items of the list. Make sure to access the list by index!
```python
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]
```

### New Neighbors
A list index behaves like any other variable name! It can be used to access as well as assign values.

You saw how to access a list index like this:
```python
zoo_animals[0]
# Gets the value "pangolin"
```
You can see how assignment works on line 5:
```python
zoo_animals[2] = "hyena"
# Changes "sloth" to "hyena"
```

1. Write an assignment statement that will replace the item that currently holds the value "tiger" with another animal (as a string). It can be any animal you like.

```python
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "wolf"
```

### Late Arrivals & List Length
A list doesn't have to have a fixed length. You can add items to the end of a list any time you like!

```python
letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters
```
<li>In the above example, we first create a list called <code>letters</code>.</li>
<li>Then, we add the string <code>'d'</code> to the end of the <code>letters</code> list.</li>
<li>Next, we print out <code>4</code>, the length of the <code>letters</code> list.</li>
<li>Finally, we print out <code>['a', 'b', 'c', 'd']</code>.</li>

1. <p>On lines 5, 6, and 7, append three <em>more</em> items to the <code>suitcase</code> list, just like the second line of the example above. (Maybe bring a bathing suit?) </p>
   <p>Then, set <code>list_length</code> equal to the length of the <code>suitcase</code> list.</p>

```python
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("weed")
suitcase.append("ak-47")
suitcase.append("vodka")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase
```

### List Slicing

Sometimes, you only want to access a portion of a list. Consider the following code:
```python
letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice
print letters
```
What is this code doing?
<p>First, we create a list called <code>letters</code>.</p>
<p>Then, we take a subsection of the list and store it in the <code>slice</code> list. We do this by defining the indices we want to include after the name of the list: <code>letters[1:3]</code>.  In Python, when we specify a portion of a list in this manner, we <strong>include</strong> the element with the first index, <code>1</code>, but we <strong>exclude</strong> the element with the second index, <code>3</code>.</p>
<p>Next, we print out <code>slice</code>, which will print <code>['b','c']</code>. Remember, in Python indices always start at <code>0</code>, so the <code>1</code> element is actually <code>b</code>.</p>
<p>Finally, we print out <code>['a', 'b', 'c', 'd', 'e']</code>, notice that we did not modify the original <code>letters</code> list.</p>

1. <p>On line 7, create a list called <code>middle</code> containing only the two middle items from <code>suitcase</code>.</p>
   <p>On line 10, create a list called <code>last</code> made up only of the last two items from <code>suitcase</code>.</p>
   
```python
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first = suitcase[0:2]
print(first)

middle = suitcase[2:4]
print(middle)

last = suitcase[4:6]
print(last)

#Output
['sunglasses', 'hat']
['passport', 'laptop']
['suit', 'shoes']
```

### Slicing Lists and Strings

<p>You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index 0.</p>

```python
my_list[:2]
# Grabs the first two items
my_list[3:]
# Grabs the fourth through last items
```
If your list slice includes the very first or last item in a list (or a string), the index for that item doesn't have to be included.

1. <p>Assign to <code>dog</code> a slice of <code>animals</code> from index 3 up until <em>but not including</em> index 6.</p>
   <p>Assign to <code>frog</code> a slice of <code>animals</code> from index 6 until the end of the string.</p>
   
```python 
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]
print(cat)
# The fourth through sixth characters
dog = animals[3:6]
print(dog)
# From the seventh character to the end
frog = animals[6:]
print(frog)
```

### Maintaining Order
Sometimes you need to search for an item in a list.
```python 
animals = ["ant", "bat", "cat"]
print animals.index("bat")
```
<ol>
<li>First, we create a list called <code>animals</code> with three strings.</li>
<li>Then, we print the first index that contains the string <code>"bat"</code>, which will print <code>1</code>.</li>
</ol>
<p>We can also <code>insert</code> items into a list.</p>

```python
animals.insert(1, "dog")
print animals
```

<ol>
<li>We insert <code>"dog"</code> at index 1, which moves everything down by 1.</li>
<li>We print out <code>["ant", "dog", "bat", "cat"]</code></li>
</ol>

1. <p>Use the <code>.index(item)</code> function to find the index of  <code>"duck"</code>. Assign that result to a variable called <code>duck_index</code>.</p>
   <p>Then <code>.insert(index, item)</code> the string <code>"cobra"</code> at that index.</p>
   
```python 
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
print(duck_index)

# Your code here!
animals.insert(duck_index,"cobra")
print animals # Observe what prints after the insert operation
```

### For One and All
<p>If you want to do something with every item in the list, you can use a <code>for</code> loop. If you've learned about <code>for</code> loops in JavaScript, pay close attention! They're different in Python.</p>

```python
for variable in list_name:
  # Do stuff!
```
<p>A variable name follows the <code>for</code> keyword; it will be assigned the value of each list item in turn.</p>
<p>Then <code>in list_name</code> designates <code>list_name</code> as the list the loop will work on. The line ends with a colon (<code>:</code>) and the indented code that follows it will be executed once per item in the list.</p>

1. <p>Write a statement in the indented part of the <code>for</code>-loop that prints a number equal to <code>2 * number</code> for every list item.</p>

```python 
my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print number * 2 
```

### More with 'for'

<p>If your list is a jumbled mess, you may need to <code>sort()</code> it.</p>

```python
animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
  print animal
```

<ol>
<li>First, we create a list called <code>animals</code> with three strings. The strings are not in alphabetical order.</li>
<li>Then, we sort <code>animals</code> into alphabetical order. Note that <code>.sort()</code> modifies the list rather than returning a new list.</li>
<li>Then, for each item in <code>animals</code>, we print that item out as <code>"ant", "bat", "cat"</code> on their own line each.</li>
</ol>

1. <p>Write a <code>for</code>-loop that iterates over <code>start_list</code> and <code>.append()</code>s each number squared (<code>x ** 2</code>) to <code>square_list</code>.</p>
   <p>Then sort <code>square_list</code>!</p>
   
```python
from math import pow
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for n in start_list:
  square_list.append(pow(n,2))
  square_list.sort()

print(square_list)

#output 
[1.0, 4.0, 9.0, 16.0, 25.0]
```

### This Next Part is Key
<p>A dictionary is similar to a list, but you access values by looking up a <em>key</em> instead of an index. A key can be any string or number.  Dictionaries are enclosed in curly braces, like so:</p>

```python
d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
```

<p>This is a dictionary called <code>d</code> with three <em>key-value pairs</em>. The key <code>'key1'</code> points to the value <code>1</code>, <code>'key2'</code> to <code>2</code>, and so on.</p>
<p>Dictionaries are great for things like phone books (pairing a name with a phone number), login pages (pairing an e-mail address with a  username), and more!</p>

1. <p>Print the values stored under the <code>'Sloth'</code> and <code>'Burmese Python'</code> <em>keys</em>. Accessing dictionary values by key is just like accessing list values by index:</p>

```python
residents['Puffin']# Gets the value 104
```

```python
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']
```

### New Entries
<p>Like Lists, Dictionaries are <em>mutable</em>. This means they can be changed after they are created. One advantage of this is that we can add new <em>key/value pairs</em> to the dictionary after it is created like so:</p>

```python
dict_name[new_key] = new_value
```

<p>An empty pair of curly braces <code>{}</code> is an empty dictionary, just like an empty pair of <code>[]</code> is an empty list.</p>

<p>The length <code>len()</code> of a dictionary is the number of key-value pairs it has. Each pair counts only once, even if the value is a list. (That's right: you can put lists <em>inside</em> dictionaries!)</p>

1. <p>Add at least three more key-value pairs to the <code>menu</code> variable, with the dish name (as a <code>"string"</code>) for the key and the price (a float or integer) as the value. Here's an example:</p>

```python 
menu['Spam'] = 2.50
```

```python 
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Shaurma Mamed'] = 4.99
menu['Deve Kutabi'] = 9.59
menu['Kosicka cheese'] = 6.00

print "There are " + str(len(menu)) + " items on the menu."
print menu

#output
14.5
There are 4 items on the menu.
{'Chicken Alfredo': 14.5, 'Deve Kutabi': 9.59, 'Shaurma Mamed': 4.99, 'Kosicka cheese': 6.0}
```

### Changing Your Mind 
<p>Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the <code>del</code> command:</p>

```python
del dict_name[key_name]
``` 

<p>will remove the key <code>key_name</code> and its associated value from the dictionary.</p>
<p>A new value can be associated with a key by assigning a value to the key, like so:</p>

```python
dict_name[key] = new_value
```

1. <p>Delete the <code>'Sloth'</code> and <code>'Bengal Tiger'</code> items from <code>zoo_animals</code> using <code>del</code>.</p>
   <p>Set the value associated with <code>'Rockhopper Penguin'</code> to anything other than <code>'Arctic Exhibit'</code>.</p>
   
```python
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'North Face'

print zoo_animals

#output
""" {'Atlantic Puffin': 'Arctic Exhibit', 'Rockhopper Penguin': 'North Face'} """
```

### Remove a Few Things
Sometimes you need to remove something from a list.

```python 
beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles
```
This code will print:

```python
 ["john","paul","george","ringo"]
```

<ol>
<li>We create a list called <code>beatles</code> with 5 strings.</li>
<li>Then, we remove the first item from <code>beatles</code> that matches the string <code>"stuart"</code>. Note that <code>.remove(item)</code> does not return anything.</li>
<li>Finally, we print out that list just to see that <code>"stuart"</code> was actually removed.</li>
</ol>

1. <p>Remove <code>'dagger'</code> from the list of items stored in the <code>backpack</code> variable.</p>

```python 
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')
```

### It's Dangerous to Go Alone! Take This
<p>Let's go over a few last notes about <em>dictionaries</em></p>

```python
my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]
```

<ol>
<li>In the example above, we created a dictionary that holds many types of values.</li>
<li>The key <code>"fish"</code> has a <em>list</em>, the key <code>"cash"</code> has an <em>int</em>, and the key <code>"luck"</code> has a <em>string</em>.</li>
<li>Finally, we print the letter <code>"c"</code>. When we access a value in the dictionary like <code>my_dict["fish"]</code>, we have direct access to that value (which happens to be a list). We can access the item at index <code>0</code> in the list stored by the key <code>"fish"</code>.</li>
</ol>

1. <div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Add a key to <code>inventory</code> called <code>'pocket'</code></p>
<p>Set the value of <code>'pocket'</code> to be a list consisting of the strings <code>'seashell'</code>, <code>'strange berry'</code>, and <code>'lint'</code></p>
<p><code>.sort()</code> the items in the list stored under the <code>'backpack'</code> key</p>
<p>Then <code>.remove('dagger')</code> from the list of items stored under the <code>'backpack'</code> key</p>
<p>Add 50 to the number stored under the <code>'gold'</code> key</p>
</div>

```python 
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
```

### BeFOR We Begin

<p>Before we begin our exercise, we should go over the Python <code>for</code> loop one more time. For now, we are only going to go over the <code>for</code> loop in terms of how it relates to <em>lists</em> and <em>dictionaries</em>. We'll explain more cool <code>for</code> loop uses in later courses.</p>

<p><code>for</code> loops allow us to iterate through all of the elements in a list from the left-most (or zeroth element) to the right-most element. A sample loop would be structured as follows: </p>

```python
a = ["List", "of", "some", "sort"]
for x in a: 
  # Do something for every x
```

<p>This loop will run all of the code in the indented block under the <code>for x in a:</code> statement. The item in the list that is currently being evaluated will be <code>x</code>.  So running the following:</p>

```python
for item in [1, 3, 21]: 
  print item
```

<p>would print <code>1</code>, then <code>3</code>, and then <code>21</code>. The variable between <code>for</code> and <code>in</code> can be set to any variable name (currently <code>item</code>), but you should be careful to avoid using the word <code>list</code> as a variable, since that's a reserved word (that is, it means something special) in the Python language.</p>

1. <p>Use a <code>for</code> loop to print out all of the elements in the list <code>names</code>.</p>

```python 
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
  print(name)
  
#Output: 
"""
Adam
Alex
Mariah
Martine
Columbus
"""
``` 
