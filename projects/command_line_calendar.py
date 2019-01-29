#Step 1. describe program - done above 
"""
Command Line Calendar

So far, you've used Python to build a variety of things, including calculators and games. In this project, we'll build a basic calendar that 
the user will be able to interact with from the command line. The user should be able to choose to:

    * View the calendar
    * Add an event to the calendar
    * Update an existing event
    * Delete an existing event

The program should behave in the following way:

    1. Print a welcome message to the user
    2. Prompt the user to view, add, update, or delete an event on the calendar
    3. Depending on the user's input: view, add, update, or delete an event on the calendar
    4. The program should never terminate unless the user decides to exit
"""

"""
Step 2. On the next line, use a function import to import sleep from the time module.
"""
from time import sleep

"""
Step 3. Since this is a calendar program, we'll need to access date and time quite often. We've been using the familiar datetime function, 
but sometimes it's necessary to use other functions. Let's try a new function out.

On the next line, use a function import to import strftime from the time module.
"""
from time import strftime

"""
Step 4. Actually, it's repetitive to import two different functions from the same module on two different lines. Let's fix that.

Go ahead and delete that last two lines of code you wrote (the function imports). Whenever possible, it's better to not repeat yourself when 
coding.

Use a function import to import both sleep and strftime from the time module, all in one line of code.
"""
from time import sleep, strftime

"""
Step 5. Great, our program is a little more concise now.

The instructions ask to build a calendar that starts with a welcome message for the user. It'd be nice for the calendar to know who the user 
is.

On the next line, add a constant variable that stores the user's first name as a string. Set it equal to your name (or another name).
"""
name = 'Ilgar'

"""
Step 6. What data structure can we use to store calendar events? You learned about lists and dictionaries in the Python course, so we'll 
have to choose one of those two.

To decide, let's think about what a calendar requires. Ideally, a calendar allows users to at least associate an event with a date, as a 
pair.

That sounds a lot like the functionality that a dictionary provides, so we'll use a dictionary to build the calendar. Our calendar will 
store the dates as keys and the events as values.
"""

"""
Step 7. On the next line, create an empty dictionary called calendar.
"""
calendar = {}

"""
Step 8. Great! We have the structures in place that we'll use to build the rest of the program. Let's start by adding the welcome message.

On the next line, create a function called welcome().

"""
def welcome()

"""
Step 9. On the next line, inside of the function, print a welcome message to the user. Use concatenation to include the message and the 
user's first name.
"""
def welcome(username):
  print("Welcome Mr. %s, AI Calendar 2029 on your duty" % username)

"""
Step 10. Next, print a message to let the user know the calendar is opening. On the next line, sleep the program for 1 second
"""
def welcome(username):
  print("Welcome Mr. %s, AI Calendar 2029 on your duty" % username)
  print("Loading AI modules...")
  sleep(1)

"""
Step 11. It's time to use the new strftime function we imported. The cool thing about the strftime function is that printing different units 
of time (months, days, years, hours, etc.) is simpler than having to call separate functions for each aspect (the way datetime works).

Look at the strftime documentation to understand how to use it (the "Directive" table is especially useful). Reviewing documentation is a 
common practice among professional software engineers.

On the next line, print the current date in the following format: Full weekday name Month Day, Year. Use concatenation and strftime to help 
you.
"""
print(strftime("%A %d, %Y"))



