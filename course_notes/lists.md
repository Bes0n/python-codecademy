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
