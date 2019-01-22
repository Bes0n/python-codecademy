""" 
Area Calculator

Python is especially useful for doing math and can be used to automate many calculations. In this project, we'll create a calculator that can compute the area of the following shapes:

    Circle
    Triangle

The program should do the following:

    Prompt the user to select a shape.
    Calculate the area of that shape.
    Print the area of that shape to the user.

Let's begin!
"""

print "Area Calculator program is running."

option  = raw_input("Enter C for Circle or T for Triangle: ")
if option == 'C' :
  radius = float(raw_input("Enter radius: "))
  pi = 3.14159
  area = pi * radius ** 2
  print "Circle area: %d.2" % (area)
elif option == 'T' : 
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "Triangle area: %d.2" % (area)
else:
  print "Invalid shape entered"

print "Exiting Area Calculator program "
