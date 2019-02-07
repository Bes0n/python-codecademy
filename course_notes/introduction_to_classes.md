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

