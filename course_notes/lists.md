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

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Use the <code>.index(item)</code> function to find the index of  <code>"duck"</code>. Assign that result to a variable called <code>duck_index</code>.</p>
<p>Then <code>.insert(index, item)</code> the string <code>"cobra"</code> at that index.</p>
</div>
