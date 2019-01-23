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
