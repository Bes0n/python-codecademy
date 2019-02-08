## CLASSES
### Class basics
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Classes can be very useful for storing complicated objects with their own methods and variables. Defining a class is much like defining a function, but we use the <code>class</code> keyword instead. We also use the word <code>object</code> in parentheses because we want our classes to <em>inherit</em> the <code>object</code> class. This means that our class has all the properties of an <code>object</code>, which is the simplest, most basic class. Later we'll see that classes can inherit other, more complicated classes. An empty class would look like this:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">ClassName</span>(<span class="cm-builtin">object</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-comment"># class statements go here</span></div></span>
</code></pre>
</div>

###### TASK
<p>Define a new class named "Car". For now, since we have to put something inside the class, use the <code>pass</code> keyword.</p>

```python
class Car(object):
  pass
```

### Create an instance of a class
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>We can use classes to create new objects, which we say are <strong>instances</strong> of those classes.</p>
<p>Creating a new instance of a class is as easy as saying:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">newObject</span> <span class="cm-operator">=</span> <span class="cm-variable">ClassName</span>(<!-- -->)</div></span>
</code></pre>
</div>

###### TASK
<p>Below your Car class, create a new object named <code>my_car</code> that is an instance of <code>Car</code>.</p>

```python
class Car(object):
  pass

my_car = Car()
```

### Class member variables
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Classes can have <em>member variables</em> that store information about each class object. We call them member variables since they are information that belongs to the class object.</p>

```python
class Car(object):
  condition = "new"

my_car = Car()
```
<p>Creating member variables and assigning them initial values is as easy as creating any other variable:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">ClassName</span>(<span class="cm-builtin">object</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-variable">memberVariable</span> <span class="cm-operator">=</span> <span class="cm-string">"initialValue"</span></div></span>
</code></pre>
</div>

###### TASK
<p>Inside your Car class, replace the <code>pass</code> statement with a new member variable named <code>condition</code> and give it an initial value of the string <code>"new"</code>.</p>

### Calling class member variables
<p>Each class object we create has its own set of member variables. Since we've created an object <code>my_car</code> that is an instance of the <code>Car</code> class, <code>my_car</code> should already have a member variable named <code>condition</code>. This attribute gets assigned a value as soon as <code>my_car</code> is created.</p>

###### TASK
<p>At the end of your code, use a <code>print</code> statement to display the <code>condition</code> of <code>my_car</code>.</p>

```python
class Car(object):
  condition = "new"

my_car = Car

print(my_car.condition)
```

### Initializing a class
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>There is a special function named <code>__init__()</code> that gets called whenever we create a new instance of a class. It exists by default, even though we don't see it. However, we can define our own <code>__init__()</code> function inside the class, overwriting the default version. We might want to do this in order to provide more input variables, just like we would with any other function.</p>
<p>The first argument passed to <code>__init__()</code> must always be the keyword <code>self</code> - this is how the object keeps track of itself internally - but we can pass additional variables after that.</p>
<p>In order to assign a variable to the class (creating a member variable), we use <em>dot notation</em>. For instance, if we passed <code>newVariable</code> into our class, inside the <code>__init__()</code> function we would say:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable-2">self</span>.<span class="cm-property">new_variable</span> <span class="cm-operator">=</span> <span class="cm-variable">new_variable</span></div></span>
</code></pre>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define the <code>__init__()</code> function of the <code>Car</code> class to take four inputs: self, model, color, and mpg. Assign the last three inputs to member variables of the same name by using the <code>self</code> keyword.</p>
<p>Then, modify the object <code>my_car</code> to provide the following inputs at initialization:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">model</span> <span class="cm-operator">=</span> <span class="cm-string">"DeLorean"</span>
<span class="cm-variable">color</span> <span class="cm-operator">=</span> <span class="cm-string">"silver"</span>
<span class="cm-variable">mpg</span> <span class="cm-operator">=</span> <span class="cm-number">88</span></div></span>
</code></pre>
<p>You don't need to include the <code>self</code> keyword when you create an instance of a class, because <code>self</code> gets added to the beginning of your list of inputs automatically by the class definition.</p>
</div>


```python
class Car(object):
  condition = "new"
  def __init__(self,model,color,mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg

my_car = Car("DeLorean", "silver", 88)

```

### Referring to member variables
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Calling class member variables works the same whether those values are created within the class (like our car's <code>condition</code>) or values are passed into the new object at initialization. We use dot notation to access the member variables of classes since those variables belong to the object.</p>
<p>For instance, if we had created a member variable named <code>new_variable</code>, a new instance of the class named <code>new_object</code> could access this variable by saying:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">new_object</span>.<span class="cm-property">new_variable</span></div></span>
</code></pre>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Now that you've created <code>my_car</code> print its member variables:</p>
<ul>
<li>First <code>print</code> the model of <code>my_car</code>. Click "Stuck? Get a hint!" for an example.</li>
<li>Then <code>print</code> out the color of <code>my_car</code>.</li>
<li>Then <code>print</code> out the mpg of <code>my_car</code>.</li>
</ul>
</div>

```python
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg

my_car = Car("DeLorean", "silver", 88)

print(my_car.model)
print(my_car.color)
print(my_car.mpg)
```

### Creating class methods
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Besides member variables, classes can also have their own methods. For example:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">Square</span>(<span class="cm-builtin">object</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-keyword">def</span> <span class="cm-def">__init__</span>(<span class="cm-variable-2">self</span>,<!-- --> <span class="cm-variable">side</span>)<!-- -->:<!-- -->
<!-- -->    <span class="cm-variable-2">self</span>.<span class="cm-property">side</span> <span class="cm-operator">=</span> <span class="cm-variable">side</span>
<!-- -->
<!-- -->  <span class="cm-keyword">def</span> <span class="cm-def">perimeter</span>(<span class="cm-variable-2">self</span>)<!-- -->:<!-- -->
<!-- -->    <span class="cm-keyword">return</span> <span class="cm-variable-2">self</span>.<span class="cm-property">side</span> <span class="cm-operator">*</span> <span class="cm-number">4</span></div></span>
</code></pre>
<p>The <code>perimeter()</code> class method is identical to defining any other function, except that it is written inside of the <code>Square</code> class definition.</p>
<p>Just like when we defined <code>__init__()</code>, you need to provide <code>self</code> as the first argument of any class method.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Inside the <code>Car</code> class, add a method named <code>display_car</code> to <code>Car</code> that will reference the Car's member variables to return the string, <code>"This is a [color] [model] with [mpg] MPG."</code> You can use the <code>str()</code> function to turn your <code>mpg</code> into a string when creating the display string.</p>
<p>Replace the individual <code>print</code> statements with a single <code>print</code> command that displays the result of calling <code>my_car.display_car()</code></p>
</div>

```python
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)

print(my_car.display_car())

```

### Modifying member variables
<p>We can modify variables that belong to a class the same way that we initialize those member variables. This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Inside the <code>Car</code> class, add a method <code>drive_car</code> that sets <code>self.condition</code> to the string <code>"used"</code>.</p>
<p>Remove the call to <code>my_car.display_car()</code> and instead <code>print</code> only the <code>condition</code> of your car.</p>
<p>Then drive your car by calling the <code>drive_car</code> method.</p>
<p>Finally, <code>print</code> the <code>condition</code> of your car again to see how its value changes.</p>
</div>

```python
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print my_car.condition
my_car.drive_car()
print my_car.condition
```

### Inheritance
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>One of the benefits of classes is that we can create more complicated classes that inherit variables or methods from their <strong>parent classes</strong>. This saves us time and helps us build more complicated objects, since these <strong>child classes</strong> can also include additional variables or methods.</p>
<p>We define a "child" class that inherits all of the variables and functions from its "parent" class like so:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-keyword">class</span> <span class="cm-def">ChildClass</span>(<span class="cm-variable">ParentClass</span>)<!-- -->:<!-- -->
<!-- -->  <span class="cm-comment"># new variables and functions go here</span></div></span>
</code></pre>
<p>Normally we use <code>object</code> as the parent class because it is the most basic type of class, but by specifying a different class, we can inherit more complicated functionality.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Create a class <code>ElectricCar</code> that inherits from <code>Car</code>. Give your new class an <code>__init__()</code> method of that includes a <code>battery_type</code> member variable in addition to the model, color and mpg.</p>
<p>Then, create an electric car named <code>my_car</code> with a <code>"molten salt"</code> <code>battery_type</code>. Supply values of your choice for the other three inputs (model, color and mpg).</p>
</div>

```python
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"
    
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
```


### Overriding methods
<p>Since our ElectricCar is a more specialized type of Car, we can give the ElectricCar its own <code>drive_car()</code> method that has different functionality than the original Car class's.</p>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Inside <code>ElectricCar</code> add a new method <code>drive_car</code> that changes the car's <code>condition</code> to the string <code>"like new"</code>.</p>
<p>Then, outside of <code>ElectricCar</code>, print the <code>condition</code> of <code>my_car</code></p>
<p>Next, drive <code>my_car</code> by calling the <code>drive_car</code> function</p>
<p>Finally, print the <code>condition</code> of <code>my_car</code> again</p>
</div>

```python
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"
    
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
  def drive_car(self):
    self.condition = "like new"
    

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition

```

### Building useful classes

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Chances are, you won't be designing Car classes in the real world anytime soon. Usually, classes are most useful for holding and accessing abstract collections of data.</p>
<p>One useful class method to override is the built-in <code>__repr__()</code> method, which is short for <em>representation</em>; by providing a return value in this method, we can tell Python how to represent an object of our class (for instance, when using a <code>print</code> statement).</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a <code>Point3D</code> class that inherits from <code>object</code></p>
<p>Inside the <code>Point3D</code> class, define an <code>__init__()</code> function that accepts <code>self</code>, <code>x</code>, <code>y</code>, and <code>z</code>, and assigns these numbers to the member variables <code>self.x</code>, <code>self.y</code>, <code>self.z</code></p>
<p>Define a <code>__repr__()</code> method that returns <code>"(%d, %d, %d)" % (self.x, self.y, self.z)</code>. This tells Python to represent this object in the following format: <code>(x, y, z)</code>.</p>
<p>Outside the class definition, create a variable named <code>my_point</code> containing a new instance of <code>Point3D</code> with x=1, y=2, and z=3.</p>
<p>Finally, print <code>my_point</code>.</p>
</div>

```python
class Point3D(object):
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(x = 1, y = 2, z = 3)  

print(my_point)

#output
(1,2,3)
```
