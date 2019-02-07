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
