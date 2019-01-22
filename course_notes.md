
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

###### Parameters and Arguments

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
