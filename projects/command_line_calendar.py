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
Step 11. It's time to use the new strftime function we imported. The cool thing about the strftime function is that printing different 
units of time (months, days, years, hours, etc.) is simpler than having to call separate functions for each aspect 
the way datetime works).

Look at the strftime documentation to understand how to use it (the "Directive" table is especially useful). Reviewing documentation 
is a common practice among professional software engineers.

On the next line, print the current date in the following format: Full weekday name Month Day, Year. Use concatenation and strftime 
to help you.
"""
print(strftime("%A %d, %Y"))

"""
Step 12. 
On the next line, print the current time in the following format: H:M:S. Use concatenation and strftime to help you.

Next, sleep the program for 1 second.
"""
sleep(1)

"""
Step 13. You succesfully used a new function, congrats! On the next line, print "What would you like to do?" to the user.
"""
print("What would you like to do?")

"""
Step 14. Perfect! Our welcome message function is now complete. Let's start building the calendar's functionality.

Create a new function called start_calendar().
"""
def start_calendar():
   
"""
Step 15. When the calendar starts, the first thing we'd like to do is welcome the user. On the next line, inside of start_calendar(), 
call the welcome() function.
"""

def start_calendar():
  welcome()

"""
Step 16. The project instructions ask that the project terminate only when the user voluntarily exits the program. In this case, 
we can use a while loop, since while loops will continue running as long as a condition is true.

On the next line, create a variable called start and set it equal to True. Next, add a while loop that uses start as the Boolean 
condition.

Since start is True, we have ensured that this loop will continue to run, unless start changes value.
"""
def start_calendar():
  welcome()
  start = True
  while start == True:
   
"""
Step 17. 
Now we'll start building the most important part of this program, the actual calendar (along with its required behavior).

Inside of the while loop, prompt the user to enter A to Add, U to Update, V to View, D to Delete, X to Exit:. Store their input 
in a variable called user_choice.

On the next line, convert user_choice to upper case.
"""

"""
Step 18. Great! We now have the user's input. The instructions require that a user be able to:

View the calendar
Update the calendar
Add to the calendar
Delete from the calendar
Let's start with the behavior that will be the easiest to implement: viewing the calendar.
"""

"""
Step 19. Keeping inside the while loop, add an if statement that checks if the user's choice is V (for View).
"""
    user_choice = user_choice.upper()
    if user_choice == 'V':
         
"""
Step 20. If the user would like to view the calendar, first we have to make sure the calendar contains events. Otherwise, we'll print
the calendar for them.

Inside of the current if statement, add another if statement that checks if there are no dates (keys) in the calendar 
(i.e. less than 1 key).

You can use the .keys() function on calendar, and use the len() function to check the length (size) of the keys.

Inside of the new if statement, print a message to the user letting them know the calendar is empty.
"""
      if len(calendar.keys()) < 1:
        print("Calendar is empty")

"""
Step 21. That will take care of notifying the user if their calendar is empty. However, if it's not empty, we need to print 
the calendar for them.

Add an else block that corresponds to the if block you just added. Inside of the else block, print the calendar.
"""

"""
Step 22. Perfect - you just built a fifth of the functionality that's needed! Keep in mind that what you just coded represents the 
general flow of how each behavior will function. Now let's add functionality to update the calendar.

Add an elif block (corresponding to the first if block you coded) that checks if the user's choice is U (for Update).
"""
