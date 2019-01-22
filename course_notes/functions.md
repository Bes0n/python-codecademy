
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

* When defining a function, placeholder variables are called parameters.
* When using, or calling, a function, inputs into the function are called arguments.


Check out the function in the editor, power. It should take two arguments, a base and an exponent, 
and raise the first to the power of the second. It's currently broken, however, because its parameters are missing.

Replace the _s with the parameters base and exponent and then call the power function with a base of 37 and an exponent of 4.


```python 
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!
```

### Functions Calling Functions

Let's look at the two functions in the editor: one_good_turn (which adds 1 to the number it takes in as an argument) and deserves_another (which adds 2).

Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.

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
