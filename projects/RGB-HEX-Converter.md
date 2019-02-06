## RGB-HEX Converter

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>In this project, we'll use Bitwise operators to build a calculator that can convert <a href="https://en.wikipedia.org/wiki/RGB_color_model" target="_blank">RGB values</a> to <a href="https://en.wikipedia.org/wiki/Hexadecimal" target="_blank">Hexadecimal (hex) values</a>, and vice-versa.</p>
<p>We'll add three methods to the project:</p>
<ul>
<li>A method to convert RGB to Hex</li>
<li>A method to convert Hex to RGB</li>
<li>A method that starts the prompt cycle</li>
</ul>
<p>The program should do the following:</p>
<ol>
<li>Prompt the user for the type of conversion they want</li>
<li>Ask the user to input the RGB or Hex value</li>
<li>Use Bitwise operators and shifting in order to convert the value</li>
<li>Print the converted value to the user</li>
</ol>
<p>It's useful to know some background on RGB and hex values, so we recommend reading the resources we linked to.</p>
<p>Note: As with professional software development, you should be saving your code very often. As you code, make sure you click the "Save" button below to save your code/changes. Otherwise, you run the risk of losing all your code.</p>
<p>Let's begin!</p>
<p>If you get stuck during this project, check out the <strong>project walkthrough video</strong> which can be found at the bottom of the page after the final step of the project.</p>
</div>

### Starting
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>First, we'll create the RGB to Hex method.</p>
<p>On line 1, add a method called <code>rgb_hex()</code>.</p>
</div>

```python
rgb_hex()
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>We should expect users to make accidental errors as they input RGB values. Let's create a constant error message that will store the message we will display to users when they make an accidental error.</p>
<p>Inside the method, create a variable called <code>invalid_msg</code> and set it equal to an appropriate error message. The message should say something about invalid values being entered.</p>
</div>

```python
invalid_msg = "Invalid values entered"
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>To convert RGB values, we'll have to prompt the user to enter values for red (R), green (G), and blue (B). Let's start by asking them enter a value for red.</p>
<p>On the next line, still inside of the method, prompt the user to enter a red value using <code>raw_input</code>. Wrap their input using<code>int()</code>. Finally, set the result equal to a variable called <code>red</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>We know that an RGB value contains three separate values, with each value representing an amount of red (R), green (G), and blue (B). Acceptable values are within the range of 0 to 255. Let's add error checking to make sure acceptable values are entered.</p>
<p>On the next line, add an <code>if</code> statement that checks if the value of <code>red</code> is less than 0, <code>or</code> greater than 255.</p>
</div>

```python
  red = int(raw_input("Enter red value: "))
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>We know that an RGB value contains three separate values, with each value representing an amount of red (R), green (G), and blue (B). Acceptable values are within the range of 0 to 255. Let's add error checking to make sure acceptable values are entered.</p>
<p>On the next line, add an <code>if</code> statement that checks if the value of <code>red</code> is less than 0, <code>or</code> greater than 255.</p>
</div>

```python
  if red < 0 and red > 255:
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Now, just as in Step 3, prompt the user to enter a value for green (G). Wrap the input using <code>int()</code> and set the result equal to a variable called <code>green</code>.</p>
</div>

```python
  green = int(raw_input("G: "))  
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Next, add error checking to make sure that the value the user enters for the color green is valid. Inside of the <code>if</code> statement, print the error message and then return on the next line.</p>
</div>

```python
  if green < 0 or red > 255:
    print("Invalid values entered")  
```
###### TASK
<p>Again, add error checking make sure the value entered for the color blue is valid. Inside of the <code>if</code> statement, print the error message and then return.</p>

```python
  blue = int(raw_input("B: "))
  if green < 0 or red > 255:
    print("Invalid values entered")      
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Now it's time to use <a href="https://www.codecademy.com/courses/learn-python/lessons/introduction-to-bitwise-operators/exercises/just-a-little-bit-" target="_blank">Bitwise operators</a> to build the rest of our method. We recommend becoming more familiar with <a href="https://en.wikipedia.org/wiki/Hexadecimal" target="_blank">hexadecimal numbers</a> first so that you can understand what the Bitwise operators in the method do.</p>
</div>

```python
  val = bin(red << 16) + bin(green << 8) + blue
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Finally, call the <code>hex()</code> method and pass <code>value</code> in as the argument. Use list slicing to print out everything except the first two characters of that string. Also, call the <code>upper()</code> method on the result.</p>
<p>See if you can use string formatting to complete all of this in one line of code.</p>
<p>Click <a href="https://docs.python.org/2/library/functions.html#hex" target="_blank">here</a> to learn more about how <code>hex()</code> works.</p>
</div>

```python
  val = (red << 16) + (green << 8) + (blue)
  print(hex(val[2:]).upper())
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Great! This method will convert an RGB value to a hex value.</p>
<p>Now, add a method called <code>hex_rgb()</code>. This is the method we'll use to convert the opposite way (from Hex to RGB).</p>
</div>

```python
def hex_rgb():
```

###### TASK
<p>Inside of the method, prompt the user to enter a hexadecimal value using <code>raw_input()</code>. Set the result equal to a variable called <code>hex_val</code>.</p>

```python
  hex_val = raw_input("Enter HEX value: ")
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Let's add some error checking that will make sure the user inputs a valid hexadecimal value. Valid hexadecimal values are six characters long, so let's check for that first.</p>
<p>Add an <code>if</code> statement that checks if the length of <code>hex_val</code> is not equal to six.</p>
</div>


```python
  if len(hex_val) != 6:
```

###### TASK
<p>Inside of the <code>if</code> statement, print a message to the user indicating that an invalid value was entered. On the next line, return.</p>

<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Otherwise, we should accept the hex value as an integer. </p>
<p>Add a corresponding <code>else</code> block that sets <code>hex_val</code> equal to calling <code>int()</code> with the arguments <code>hex_val</code> and <code>16</code>.</p>
</div>

```python
  if len(hex_val) != 6:
    invalid_msg
    return
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Otherwise, we should accept the hex value as an integer. </p>
<p>Add a corresponding <code>else</code> block that sets <code>hex_val</code> equal to calling <code>int()</code> with the arguments <code>hex_val</code> and <code>16</code>.</p>
</div>

```python
  else:
    hex_val = int(hex_val, 16)
```

###### TASK
<p>Next, outside of the <code>else</code> block, but still within the method, create a variable called <code>two_hex_digits</code> and set it equal to 2 raised to the power of 8.</p>

```python
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Next, we'll start calculating the RGB values.</p>
<p>Create a variable called <code>blue</code> and set it equal to <code>hex_val</code> modulo <code>two_hex_digits</code>.</p>
</div>

```python
  blue = hex_val % two_hex_digits 
```

###### TASK
<p>Next, shift <code>hex_val</code> to the right by 8 bits.</p>

```python
  hex_val = hex_val << 8 
```

##### TASK
<p>Finally, calculate the red value by creating a variable called <code>red</code> and setting it equal to <code>hex_val</code> modulo <code>two_hex_digits</code>.</p> Same for last color. 

```python
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits 
  hex_val = hex_val << 8 
  green = hex_val % two_hex_digits
  hex_val = hex_val << 8 
  red = hex_val % two_hex_digits
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Fantastic! The method you just wrote will convert a hexadecimal value to an RGB value.</p>
<p>Let's add the last method that will run our program. Create a new method called <code>convert()</code>.</p>
</div>

```python
def convert():
```

###### TASK
<p>Inside the method, add a <code>while</code> loop with the Boolean <code>True</code> as the condition.</p>

```python
def convert():
  while True:
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>On the next line, inside of the <code>while</code> loop, prompt the user for input with the following message: <code>Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:</code>.</p>
<p>Set the result equal to a variable called <code>option</code>.</p>
</div>

```python
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:")
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Now let's handle all the cases of user input. </p>
<p>Start an <code>if</code> statement that checks if <code>option</code> is equal to <code>'1'</code> (as a string).</p>
</div>

```python
    if option == '1':
      print("RGB to Hex...")
      rgb_hex()
```

###### TASK
<p>Add a corresponding <code>elif</code> block that checks if the option is <code>'2'</code>. If it is, print <code>Hex to RGB...</code> first. Then, on the next line, call the <code>hex_rgb()</code> method.</p>

```python
    elif option == '2':
      print("Hex to RGB")
      hex_rgb()
```

###### TASK
<p>Add another <code>elif</code> statement that checks if the option is <code>'X'</code> or <code>'x'</code>. If it is, exit the loop with the <code>break</code> keyword.</p>

```python
    elif option == 'X' or option == 'x':
      break
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Finally, finish the <code>if</code> statement by adding an <code>else</code> block. This part of the statement will handle any other input from the user. Inside of the <code>else</code> block, print <code>Error.</code>.</p>
</div>

```python
    else:
      print("Error")
```

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>You're nearly done - great job! The next step is to actually call the method that will run our program.</p>
<p>As the final line of your code (outside of any method), call the <code>convert()</code> method.</p>
</div>

```python
convert()      
```

```python
#Full Code:
#Code has a bug, which I was not able to find. HEX to RGB is not working properly. 

def rgb_hex():
  invalid_msg = "Invalid values entered"
  red = int(raw_input("R: "))
  if red < 0 or red > 255:
    print(invalid_msg)
    return
  green = int(raw_input("G: "))
  if green < 0 or red > 255:
    print(invalid_msg)
    return
  blue = int(raw_input("B: "))
  if green < 0 or red > 255:
    print(invalid_msg)
    return 
  val = (red << 16) + (green << 8) + blue
  print(hex(val)[2:]).upper()
  
def hex_rgb():
  hex_val = raw_input("Enter HEX value: ")
  if len(hex_val) != 6:
    print(invalid_msg)
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val << 8
  green = hex_val % two_hex_digits
  hex_val = hex_val << 8
  red = hex_val % two_hex_digits
  print "rgd(%s, %s, %s)" % (red, green, blue)
  
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:")
    if option == '1':
      print("RGB to Hex...")
      rgb_hex()
    elif option == '2':
      print("Hex to RGB")
      hex_rgb()
    elif option == 'X' or option == 'x':
      break
    else:
      print("Error")
      
convert()

```
