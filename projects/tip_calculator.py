"""
Now that you have completed the lesson on Python syntax, it's time to practice your newfound skills. In this project, you will create a simple calculator that determines the price of a meal after tax and tip.

If you get stuck during this project, check out the project walkthrough video which can be found at the bottom of the page after the final step of the project.
"""

meal = 44.50
tax = .0675 #which equals to 6.75%
tip = .15 #which equals to 15% 

meal += meal * tax 
total = meal + meal * tip

print '%02d.02' % (total)
