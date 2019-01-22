
### What Good are Functions?

You might have considered the situation where you would like to reuse a piece of code, just with a few different values. Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.
```python
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
```

### Parameters and Arguments

1. When defining a function, placeholder variables are called parameters.
2. When using, or calling, a function, inputs into the function are called arguments.

* Check out the function in the editor, power. It should take two arguments, a base and an exponent, 
and raise the first to the power of the second. It's currently broken, however, because its parameters are missing.

* Replace the _s with the parameters base and exponent and then call the power function with a base of 37 and an exponent of 4.
```python 
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!
```

### Functions Calling Functions

* Let's look at the two functions in the editor: one_good_turn (which adds 1 to the number it takes in as an argument) and deserves_another (which adds 2).

* Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.
```python
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

print(one_good_turn(2)) #return 3
print(deserves_another(2)) #return 5
```

### Practice Makes Perfect

* First, def a function called cube that takes an argument called number. Don't forget the parentheses and the colon!

* Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).

* Define a second function called by_three that takes an argument called number.

* if that number is divisible by 3, by_three should call cube(number) and return its result. Otherwise, by_three should return False.

* Don't forget that if and else statements need a : at the end of that line!
```python
def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False
```

### Generic Imports

Did you see that? Python said: NameError: name 'sqrt' is not defined. Python doesn't know what square roots are—yet.

There is a Python module named math that includes a number of useful variables and functions, and sqrt() is one of those functions. In order to access math, all you need is the import keyword. When you simply import a module this way, it's called a generic import.

1. You'll need to do two things here:

* Type import math on line 2 in the editor.
* Insert math. before sqrt() so that it has the form math.sqrt(). This tells Python not only to import math, but to get the sqrt() function from within math. Then hit Run to see what Python now knows.
```python
# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)
```

### Function Imports

Nice work! Now Python knows how to take the square root of a number.

However, we only really needed the sqrt function, and it can be frustrating to have to keep typing math.sqrt().

It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it's done with the from keyword:
```python
from module import function
```
Now you can just type sqrt() to get the square root of a number—no more math.sqrt()!

1. Let's import only the sqrt function from math this time. (You don't need the () after sqrt in the from math import sqrt bit.)
```python
from math import sqrt

print sqrt(25)
```

### Universal Imports 

Great! We've found a way to handpick the variables and functions we want from modules.

What if we still want all of the variables and functions in a module but don't want to have to constantly type math.?

Universal import can handle this for you. The syntax for this is:
```python
from module import *
```

1. Use the power of from module import * to import everything from the math module on line 3 of the editor.
```python
from math import *
```

### Here Be Dragons

Universal imports may look great on the surface, but they're not a good idea for one very important reason: they fill your program with a ton of variable and function names without the safety of those names still being associated with the module(s) they came from.

If you have a function of your very own named sqrt and you import math, your function is safe: there is your sqrt and there is math.sqrt. If you do from math import *, however, you have a problem: namely, two different functions with the exact same name.

Even if your own definitions don't directly conflict with names from imported modules, if you import * from several modules at once, you won't be able to figure out which variable or function came from where.

For these reasons, it's best to stick with either import module and type module.name or just import specific variables and functions from various modules as needed.

1. The code in the editor will show you everything available in the math module.

Click Run to check it out (you'll see sqrt, along with some other useful things like pi, factorial, and trigonometric functions.
```python 
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!
```

### On Beyond Strings

Now that you understand what functions are and how to import modules, let's look at some of the functions that are built in to Python (no modules required!).

You already know about some of the built-in functions we've used with strings, such as .upper(), .lower(), str(), and len(). These are great for doing work with strings, but what about something a little more analytic?

1. What do you think the code in the editor will do? Click Run when you think you have an idea.
```python
def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
```

### max()

The max() function takes any number of arguments and returns the largest one. ("Largest" can have odd definitions here, so it's best to use max() on integers and floats, where the results are straightforward, and not on other objects, like strings.)

For example, max(1,2,3) will return 3 (the largest number in the set of arguments).

1. Try out the max() function on line 3 of the editor. You can provide any number of integer or float arguments to max().
```python
maximum = max(30,24,10)
print maximum #30
```

### min() 

min() then returns the smallest of a given series of arguments.

1. Go ahead and set minimum equal to the min() of any set of integers or floats you'd like.
```python
minimum = min(30,24,10)
print minimum #10
```

### abs() 

The abs() function returns the absolute value of the number it takes as an argument—that is, that number's distance from 0 on an imagined number line. For instance, 3 and -3 both have the same absolute value: 3. The abs() function always returns a positive value, and unlike max() and min(), it only takes a single number.

1. Set absolute equal to the absolute value of -42 on line 1.
```python
absolute = abs(-42)
print absolute #42
```

### type()
Finally, the type() function returns the type of the data it receives as an argument. If you ask Python to do the following:

```python
print type(42)
print type(4.2)
print type('spam')
```
Python will output: 
```python
<type 'int'>
<type 'float'>
<type 'str'>
```

1. Have Python print out the type of an int, a float, and a str string in the editor. You can pick any values on which to call type(), so long as they produce one of each.

### Review: Functions

Okay! Let's review functions.

```python
def speak(message):
  return message

if happy():
  speak("I'm happy!")
elif sad():
  speak("I'm sad.")
else:
  speak("I don't know what I'm feeling.")
```
Again, the example code above is just there for your reference!

1. First, def a function, shut_down, that takes one argument s. Don't forget the parentheses or the colon!

* Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down"

* Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted".

* Finally, if shut_down gets anything other than those inputs, the function should return "Sorry"

```python
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
```

### Review: Built-In Functions
Perfect! Last but not least, let's review the built-in functions you've learned about in this lesson.

```python
def is_numeric(num):
  return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2
```

1. First, def a function called distance_from_zero, with one argument (choose any argument name you like).

* If the type of the argument is either int or float, the function should return the absolute value of the function input.

* Otherwise, the function should return "Nope"

```python
def distance_from_zero(s):
  if type(s) == int or type(s) == float:
    return abs(s)
  else:
    return "Nope"
```
