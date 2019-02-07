## INTRODUCTION TO CLASSES
### Why Use Classes?

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Python is an object-oriented programming language, which means it manipulates programming constructs called <em>objects</em>. You can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its <em>methods</em>. For example, any time you call</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-builtin">len</span>(<span class="cm-string">"Eric"</span>)</div></span>
</code></pre>
<p>Python is checking to see whether the string object you passed it has a length, and if it does, it returns the value associated with that <em>attribute</em>. When you call</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">my_dict</span>.<span class="cm-property">items</span>(<!-- -->)</div></span>
</code></pre>
<p>Python checks to see if <code>my_dict</code> has an <code>items()</code> method (which all dictionaries have) and executes that method if it finds it.</p>
<p>But what makes <code>"Eric"</code> a string and <code>my_dict</code> a dictionary? The fact that they're instances of the <code>str</code> and <code>dict</code> classes, respectively. A class is just a way of organizing and producing objects with similar attributes and methods.</p>
</div>

###### TASK
<p>Check out the code in the editor to the right. We've defined our own class, <code>Fruit</code>, and created a <code>lemon</code> instance.When you're ready, click Run to get started creating classes and objects of your own.</p>

```python
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

#Output:
I'm a yellow lemon and I taste sour.
Yep! I'm edible.

```

### Class Syntax
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>A basic class consists only of the <code>class</code> keyword, the name of the class, and the class from which the new class <strong>inherits</strong> in parentheses. (We'll get to inheritance soon.) For now, our classes will inherit from the <code>object</code> class, like so:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">NewClass</span>(<span class="cm-builtin">object</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-comment"># Class magic here</span></div></span>
</code></pre>
<p>This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.</p>
</div>

###### TASK
<p>Create a class called <code>Animal</code> in the editor. For now, in the body of your class, use the <code>pass</code> keyword. (<code>pass</code> doesn't do anything, but it's useful as a placeholder in areas of your code where Python expects an expression.)</p>

```python
class Animal(object):
  pass
```

### Classier Classes
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>We'd like our classes to do more than... well, <em>nothing</em>, so we'll have to replace our <code>pass</code> with something else.</p>
<p>You may have noticed in our example back in the first exercise that we started our class definition off with an odd-looking function: <code>__init__()</code>. This function is required for classes, and it's used to <strong>initialize</strong> the objects it creates. <code>__init__()</code> always takes at least one argument, <code>self</code>, that refers to the object being created. You can think of <code>__init__()</code> as the function that "boots up" each object the class creates.</p>
</div>

###### TASK
<p>Remove the <code>pass</code> statement in your <code>class</code> definition, then go ahead and <code>def</code>ine an <code>__init__()</code> function for your <code>Animal</code> class. Pass it the argument <code>self</code> for now; we'll explain how this works in greater detail in the next section. Finally, put the <code>pass</code> into the body of the <code>__init__()</code> definition, since it will expect an indented block.</p>

```python
class Animal(object):
  def __init__(self):
    pass
```

### Let's Not Get Too Selfish
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Excellent! Let's make one more tweak to our class definition, then go ahead and <strong>instantiate</strong> (create) our first object.</p>
<p>So far, <code>__init__()</code> only takes one parameter: <code>self</code>. This is a Python convention; there's nothing magic about the word <code>self</code>. However, it's overwhelmingly common to use <code>self</code> as the first parameter in <code>__init__()</code>, so you should do this so that other people will understand your code.</p>
<p>The part that <em>is</em> magic is the fact that <code>self</code> is the <em>first</em> parameter passed to <code>__init__()</code>. Python will use the first parameter that <code>__init__()</code> receives to refer to the object being created; this is why it's often called <code>self</code>, since this parameter gives the object being created its identity.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Let's do two things in the editor:</p>
<ul>
<li>Pass <code>__init__()</code> a second parameter, <code>name</code>.</li>
<li>In the body of <code>__init__()</code>, let the function know that <code>name</code> refers to the created object's name by typing <code>self.name = name</code>. (This will become crystal clear in the next section.)</li>
</ul>
</div>

```python
class Animal(object):
  def __init__(self,name):
    pass
    self.name = name
```

### Instantiating Your First Object
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Perfect! Now we're ready to start creating objects.</p>
<p>We can access attributes of our objects using <em>dot notation</em>. Here's how it works:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">Square</span>(<span class="cm-builtin">object</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-keyword">def</span> <span class="cm-def">__init__</span>(<span class="cm-variable-2">self</span>)<!-- -->:<!-- -->
<!-- -->    <span class="cm-variable-2">self</span>.<span class="cm-property">sides</span> <span class="cm-operator">=</span> <span class="cm-number">4</span>
<!-- -->
<span class="cm-variable">my_shape</span> <span class="cm-operator">=</span> <span class="cm-variable">Square</span>(<!-- -->)<!-- -->
<span class="cm-builtin">print</span> <span class="cm-variable">my_shape</span>.<span class="cm-property">sides</span></div></span>
</code></pre>
<ol>
<li>First we create a class named <code>Square</code> with an attribute <code>sides</code>.</li>
<li>Outside the class definition, we create a new instance of <code>Square</code> named <code>my_shape</code> and access that attribute using <code>my_shape.sides</code>.</li>
</ol>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Outside the <code>Animal</code> class definition, create a variable named <code>zebra</code> and set it equal to <code>Animal("Jeffrey")</code>.</p>
<p>Then <code>print</code> out <code>zebra</code>'s name.</p>
</div>

```python
class Animal(object):
  def __init__(self,name):
    pass
    self.name = name
    
zebra = Animal("Jeffrey")

print(zebra.name)

#output 
Jeffrey
```

### More on __init__() and self
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Now that you're starting to understand how classes and objects work, it's worth delving a bit more into <code>__init__()</code> and <code>self</code>. They can be confusing!</p>
<p>As mentioned, you can think of <code>__init__()</code> as the method that "boots up" a class' instance object: the <code>init</code> bit is short for "initialize."</p>
<p>The first argument <code>__init__()</code> gets is used to refer to the instance object, and by convention, that argument is called <code>self</code>. If you add additional arguments—for instance, a <code>name</code> and <code>age</code> for your animal—setting each of those equal to <code>self.name</code> and <code>self.age</code> in the body of <code>__init__()</code> will make it so that when you create an instance object of your <code>Animal</code> class, you need to give each instance a name and an age, and those will be associated with the particular instance you create.</p>
</div>

###### TASK
<p>Check out the examples in the editor. See how <code>__init__()</code> "boots up" each object to expect a name and an age, then uses <code>self.name</code> and <code>self.age</code> to assign those names and ages to each object? Add a third attribute, <code>is_hungry</code> to <code>__init__()</code>, and click Run to see the results.</p>

```python
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

#output
Jeffrey 2 True
Bruce 1 False
Chad 7 True
```

### Class Scope
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Another important aspect of Python classes is <em>scope</em>. The scope of a variable is the context in which it's visible to the program.</p>
<p>It may surprise you to learn that not all variables are accessible to all parts of a Python program at all times. When dealing with classes, you can have variables that are available everywhere (<em>global variables</em>), variables that are only available to members of a certain class (<em>member variables</em>), and variables that are only available to particular instances of a class (<em>instance variables</em>).</p>
<p>The same goes for functions: some are available everywhere, some are only available to members of a certain class, and still others are only available to particular instance objects.</p>
</div>

###### TASK
<p>Check out the code in the editor. Note that each individual animal gets its own <code>name</code> and <code>age</code> (since they're all initialized individually), but they all have access to the member variable <code>is_alive</code>, since they're all members of the <code>Animal</code> class. Click Run to see the output!</p>

```python
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

#output 
Jeffrey 2 True
Bruce 1 True
Chad 7 True
```

### A Methodical Approach
<p>When a class has its own functions, those functions are called <em>methods</em>. You've already seen one such method: <code>__init__()</code>. But you can also define your own methods!</p>

###### TASK
<p>Add a method, <code>description</code>, to your <code>Animal</code> class. Using two separate <code>print</code> statements, it should print out the <code>name</code> and <code>age</code> of the animal it's called on. Then, create an instance of <code>Animal</code>, <code>hippo</code> (with whatever name and age you like), and call its <code>description</code> method.</p>

```python
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age

#calling our custom method    
print(Animal('Jacala', 41).description())

#or calling __init__ method
giraffe = Animal("Bruce", 1)
print(giraffe.name, giraffe.age)
```

### They're Multiplying!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>A class can have any number of <strong>member variables</strong>. These are variables that are available to all members of a class.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">hippo</span> <span class="cm-operator">=</span> <span class="cm-variable">Animal</span>(<span class="cm-string">"Jake"</span>,<!-- --> <span class="cm-number">12</span>)<!-- -->
<span class="cm-variable">cat</span> <span class="cm-operator">=</span> <span class="cm-variable">Animal</span>(<span class="cm-string">"Boots"</span>,<!-- --> <span class="cm-number">3</span>)<!-- -->
<span class="cm-builtin">print</span> <span class="cm-variable">hippo</span>.<span class="cm-property">is_alive</span>
<span class="cm-variable">hippo</span>.<span class="cm-property">is_alive</span> <span class="cm-operator">=</span> <span class="cm-keyword">False</span>
<span class="cm-builtin">print</span> <span class="cm-variable">hippo</span>.<span class="cm-property">is_alive</span>
<span class="cm-builtin">print</span> <span class="cm-variable">cat</span>.<span class="cm-property">is_alive</span></div></span>
</code></pre>
<ol>
<li>In the example above, we create two instances of an <code>Animal</code>.</li>
<li>Then we print out <code>True</code>, the default value stored in hippo's <code>is_alive</code> member variable.</li>
<li>Next, we set that to False and print it out to make sure.</li>
<li>Finally, we print out <code>True</code>, the value stored in cat's <code>is_alive</code> member variable. We only changed the variable in hippo, not in cat.</li>
</ol>
<p>Let's add another member variable to <code>Animal</code>.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>After line 3, add a second member variable called <code>health</code> that contains the string <code>"good"</code>.</p>
<p>Then, create two new <code>Animals</code>: <code>sloth</code> and <code>ocelot</code>. (Give them whatever names and ages you like.)</p>
<p>Finally, on three separate lines, <code>print</code> out the <code>health</code> of your <code>hippo</code>, <code>sloth</code>, and <code>ocelot</code>.</p>
</div>

```python
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Bruce", 1)
print(hippo.health)
sloth = Animal("Baby", 20)
print(sloth.health)
ocelot = Animal("Johny", 25)
print(ocelot.health)

```

### It's Not All Animals and Fruits
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Classes like <code>Animal</code> and <code>Fruit</code> make it easy to understand the concepts of classes and instances, but you probably won't see many zebras or lemons in real-world programs.</p>
<p>However, classes and objects are often used to model real-world objects. The code in the editor is a more realistic demonstration of the kind of classes and objects you might find in commercial software. Here we have a basic <code>ShoppingCart</code> class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.</p>
</div>

###### TASK
<p>Create an instance of <code>ShoppingCart</code> called <code>my_cart</code>. Initialize it with any values you like, then use the <code>add_item</code> method to add an item to your cart.</p>

```python
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."
      
my_cart = ShoppingCart("Eric")
my_cart.add_item("Apples", 5)
    
#Output:
Apples added

```

### Warning: Here Be Dragons
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p><em>Inheritance</em> is a tricky concept, so let's go through it step by step.</p>
<p>Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an <em>is-a</em> relationship. For example, a Panda is a bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.</p>
</div>

###### TASK
<p>Check out the code in the editor. We've defined a class, <code>Customer</code>, as well as a <code>ReturningCustomer</code> class that inherits from <code>Customer</code>. Note that we don't define the <code>display_cart</code> method in the body of <code>ReturningCustomer</code>, but it will still have access to that method via inheritance. Click Run to see for yourself!</p>

```python
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#output
I'm a string that stands in for the contents of your shopping cart!
I'm a string that stands in for your order history!
```

### Inheritance Syntax
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>In Python, inheritance works like this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">DerivedClass</span>(<span class="cm-variable">BaseClass</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-comment"># code goes here</span></div></span>
</code></pre>
<p>where <code>DerivedClass</code> is the new class you're making and <code>BaseClass</code> is the class from which that new class inherits.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>On lines 1-4, we've created a class named <code>Shape</code>.</p>
<ul>
<li>Create your own class, <code>Triangle</code>, that inherits from <code>Shape</code>, like this:<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">Triangle</span>(<span class="cm-variable">Shape</span>)<!-- -->:<!-- -->
<span class="cm-comment"># code goes here</span></div></span>
</code></pre>
</li>
<li>Inside the <code>Triangle</code> class, write an <code>__init__()</code> function that takes four arguments: <code>self</code>, <code>side1</code>, <code>side2</code>, and <code>side3</code>. </li>
<li>Inside the <code>__init__()</code> function, set <code>self.side1 = side1</code>, <code>self.side2 = side2</code>, and <code>self.side3 = side3</code>.</li>
</ul>
<p>Click "Stuck? Get a hint!" for an example.</p>
</div>

```python
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
    
```

### Override!
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to <em>override</em> one or more of them.</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">Employee</span>(<span class="cm-builtin">object</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-keyword">def</span> <span class="cm-def">__init__</span>(<span class="cm-variable-2">self</span>,<!-- --> <span class="cm-variable">name</span>)<!-- -->:<!-- -->
<!-- -->    <span class="cm-variable-2">self</span>.<span class="cm-property">name</span> <span class="cm-operator">=</span> <span class="cm-variable">name</span>
<!-- -->  <span class="cm-keyword">def</span> <span class="cm-def">greet</span>(<span class="cm-variable-2">self</span>,<!-- --> <span class="cm-variable">other</span>)<!-- -->:<!-- -->
<!-- -->    <span class="cm-builtin">print</span> <span class="cm-string">"Hello, %s"</span> <span class="cm-operator">%</span> <span class="cm-variable">other</span>.<span class="cm-property">name</span>
<!-- -->
<span class="cm-keyword">class</span> <span class="cm-def">CEO</span>(<span class="cm-variable">Employee</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-keyword">def</span> <span class="cm-def">greet</span>(<span class="cm-variable-2">self</span>,<!-- --> <span class="cm-variable">other</span>)<!-- -->:<!-- -->
<!-- -->    <span class="cm-builtin">print</span> <span class="cm-string">"Get back to work, %s!"</span> <span class="cm-operator">%</span> <span class="cm-variable">other</span>.<span class="cm-property">name</span>
<!-- -->
<span class="cm-variable">ceo</span> <span class="cm-operator">=</span> <span class="cm-variable">CEO</span>(<span class="cm-string">"Emily"</span>)<!-- -->
<span class="cm-variable">emp</span> <span class="cm-operator">=</span> <span class="cm-variable">Employee</span>(<span class="cm-string">"Steve"</span>)<!-- -->
<span class="cm-variable">emp</span>.<span class="cm-property">greet</span>(<span class="cm-variable">ceo</span>)<!-- -->
<span class="cm-comment"># Hello, Emily</span>
<span class="cm-variable">ceo</span>.<span class="cm-property">greet</span>(<span class="cm-variable">emp</span>)<!-- -->
<span class="cm-comment"># Get back to work, Steve!</span></div></span>
</code></pre>
<p>Rather than have a separate <code>greet_underling</code> method for our CEO, we override (or re-create) the <code>greet</code> method on top of the base <code>Employee.greet</code> method. This way, we don't need to know what type of Employee we have before we greet another Employee.</p>
</div>


###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a new class, <code>PartTimeEmployee</code>, that inherits from <code>Employee</code>.</p>
<p>Give your derived class a <code>calculate_wage</code> method that overrides <code>Employee</code>'s. It should take <code>self</code> and <code>hours</code> as arguments.</p>
<p>Because <code>PartTimeEmployee.calculate_wage</code> overrides <code>Employee.calculate_wage</code>, it still needs to set <code>self.hours = hours</code>.</p>
<p>It should <code>return</code> the part-time employee's number of <code>hours</code> worked multiplied by <code>12.00</code> (that is, they get $12.00 per hour instead of $20.00).</p>
</div>

```python
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
```

### This Looks Like a Job For...
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>On the flip side, sometimes you'll be working with a derived class (or <em>subclass</em>) and realize that you've overwritten a method or attribute defined in that class' base class (also called a <em>parent</em> or <em>superclass</em>) that you actually need. Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in <code>super</code> call.</p>
<p>The syntax looks like this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">Derived</span>(<span class="cm-variable">Base</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-keyword">def</span> <span class="cm-def">m</span>(<span class="cm-variable-2">self</span>)<!-- -->:<!-- -->
<!-- -->    <span class="cm-keyword">return</span> <span class="cm-builtin">super</span>(<span class="cm-variable">Derived</span>,<!-- --> <span class="cm-variable-2">self</span>)<!-- -->.<span class="cm-property">m</span>(<!-- -->)</div></span>
</code></pre>
<p>Where <code>m()</code> is a method from the base class.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>First, inside your <code>PartTimeEmployee</code> class:</p>
<ul>
<li>Add a new method called <code>full_time_wage</code> with the arguments <code>self</code> and <code>hours</code>.</li>
<li>That method should <code>return</code> the result of a <code>super</code> call to the <code>calculate_wage</code> method of <code>PartTimeEmployee</code>'s parent class. Use the example above for help.</li>
</ul>
<p>Then, after your class:</p>
<ul>
<li>Create an instance of the <code>PartTimeEmployee</code> class called <code>milton</code>. Don't forget to give it a name.</li>
<li>Finally, <code>print</code> out the result of calling his <code>full_time_wage</code> method. You should see his wage printed out at $20.00 per hour! (That is, for <code>10</code> hours, the result should be <code>200.00</code>.)</li>
</ul>
</div>

```python

```
