## Practice Makes Perfect

### is_even
All right! Let's get started.

Remember how an even number is a number that is divisible by 2?

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function <code>is_even</code> that will take a number <code>x</code> as input.</p>
<p>If <code>x</code> is even, then <code>return True</code>.</p>
<p>Otherwise, <code>return False</code>.</p>
</div>

```python
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
```

### is_int
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>An integer is just a number without a decimal part (for instance, <code>-17</code>, <code>0</code>, and <code>42</code> are all integers, but <code>98.6</code> is not).</p>
<p>For the purpose of this lesson, we'll also say that <strong>a number with a decimal part that is all 0s is also an integer</strong>, such as <code>7.0</code>.</p>
<p>This means that, for this lesson, you can't just test the input to see if it's of type <code>int</code>.</p>
<p>If the difference between a number and that same number rounded is greater than zero, what does that say about that particular number?</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function <code>is_int</code> that takes a number <code>x</code> as an input.</p>
<p>Have it <code>return True</code> if the number is an integer (as defined above) and <code>False</code> otherwise.</p>
<p>For example:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">is_int</span>(<span class="cm-number">7.0</span>)<!-- -->   <span class="cm-comment"># True    </span>
<span class="cm-variable">is_int</span>(<span class="cm-number">7.5</span>)<!-- -->   <span class="cm-comment"># False    </span>
<span class="cm-variable">is_int</span>(<span class="cm-operator">-</span><span class="cm-number">1</span>)<!-- -->    <span class="cm-comment"># True</span></div></span>
</code></pre>
</div>

```python
def is_int(x):
  if x // 1 == x:
    return True
  else:
    return False
    
or codecademy solution:

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)
```

### digit_sum
Awesome! Now let's try something a little trickier. Try summing the digits of a number.

###### TASK 
<p>Write a function called <code>digit_sum</code> that takes a positive integer <code>n</code> as input and returns the sum of all that number's digits. For example: <code>digit_sum(1234)</code> should return <code>10</code> which is <code>1 + 2 + 3 + 4</code>. (Assume that the number you are given will always be positive.)</p>

```python
def digit_sum(n):
  n = str(n)
  dsum = 0
  for i in n:
    dsum += int(i)
  return dsum

#Alternate Solution:

#def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total
```

### factorial

<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>All right! Now we're cooking. Let's try a factorial problem.</p>
<p>To calculate the factorial of a non-negative integer <code>x</code>, just multiply all the integers from 1 through <code>x</code>. For example:</p>
<ul>
<li><code>factorial(4)</code> would equal <code>4 * 3 * 2 * 1</code>, which is 24.</li>
<li><code>factorial(1)</code> would equal <code>1</code>.</li>
<li><code>factorial(3)</code> would equal <code>3 * 2 * 1</code>, which is 6.</li>
</ul>
</div>

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function <code>factorial</code> that takes an integer <code>x</code> as input.</p>
<p>Calculate and return the factorial of that number.</p>
</div>

```python
def factorial(x):
  multiplier = 1
  while x > 1:
    multiplier *= x
    x -= 1
  return multiplier

print(factorial(4))
```

### is_prime
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>A <em>prime number</em> is a positive integer greater than 1 that has no positive divisors other than 1 and itself. (That's a mouthful!)</p>
<p>In other words, if you want to test if a number in a variable <code>x</code> is prime, then no other number should go into <code>x</code> evenly besides 1 and <code>x</code>. So <code>2</code> and <code>5</code> and <code>11</code> are all prime, but <code>4</code> and <code>18</code> and <code>21</code> are not.</p>
<p>If there is a number between 1 and <code>x</code> that goes in evenly, then <code>x</code> is not prime.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>is_prime</code> that takes a number <code>x</code> as input.</p>
<p>For each number <code>n</code> from 2 to <code>x - 1</code>, test if <code>x</code> is evenly divisible by <code>n</code>.</p>
<p>If it is, <code>return False</code>.</p>
<p>If none of them are, then <code>return True</code>.</p>
</div>

```python
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print is_prime(13)
print is_prime(10)
```

### reverse

Great work so far! Let's practice writing some functions that work with strings.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>reverse</code> that takes a string <code>text</code>and returns that string in reverse. For example: <code>reverse("abcd")</code> should return <code>"dcba"</code>.</p>
<p>You may not use <code>reversed</code> or <code>[::-1]</code> to help you with this.</p>
<p>You may get a string containing special characters (for example, !, @, or #).</p>
</div>

```python
def reverse(text):
  new_str = ''
  for i in range(len(text)):
    new_str += text[len(text) - 1 - i]
  return new_str
    
print(reverse("Python!"))
```

### anti_vowel
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>anti_vowel</code> that takes one string, <code>text</code>, as input and returns the text with all of the vowels removed.</p>
<p>For example: <code>anti_vowel("Hey You!")</code> should return <code>"Hy Y!"</code>. Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.</p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>anti_vowel</code> that takes one string, <code>text</code>, as input and returns the text with all of the vowels removed.</p>
<p>For example: <code>anti_vowel("Hey You!")</code> should return <code>"Hy Y!"</code>. Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.</p>
</div>

```python
#My really bad code:
def anti_vowel(text):
    vowel = ['A','E','I','O','U']
    text_list = []
    need_to_remove = []
    new_string = ''
    for i in text:
        text_list.append(i)
    for char in text_list:
        if char in vowel or char.upper() in vowel:
            need_to_remove.append(char)
    for char in need_to_remove:
        if char in text_list:
            text_list.remove(char)
    for char in text_list:
        new_string += char
    return new_string

#Codecademy:
def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print anti_vowel("hello book")
```

### scrabble_score
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter (we'll leave out the double and triple letter and word scores for now).</p>
<p>To the right is a dictionary containing all of the letters in the alphabet with their corresponding Scrabble point values. </p>
<p>For example: the word <code>"Helix"</code> would score <code>15</code> points due to the sum of the letters: <code>4 + 1 + 1 + 1 + 8</code>. </p>
</div>

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function <code>scrabble_score</code> that takes a string <code>word</code> as input and returns the equivalent scrabble score for that word.  </p>
<ul>
<li>Assume your input is only one word containing no spaces or punctuation.</li>
<li>As mentioned, no need to worry about score multipliers!</li>
<li>Your function should work even if the letters you get are uppercase, lowercase, or a mix.</li>
<li>Assume that you're only given non-empty strings.</li>
</ul>
</div>

```python
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  total = 0
  for char in word:
    if char in score:
      total += score[char]
  return total
```

### censor 
You're doing great with these string function challenges. Last one!

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Write a function called <code>censor</code> that takes two strings, <code>text</code> and <code>word</code>, as input. It should return the <code>text</code> with the <code>word</code> you chose replaced with asterisks. For example:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-variable">censor</span>(<span class="cm-string">"this hack is wack hack"</span>,<!-- --> <span class="cm-string">"hack"</span>)</div></span>
</code></pre>
<p>should return: </p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-string">"this **** is wack ****"</span></div></span>
</code></pre>
<ul>
<li>Assume your input strings won't contain punctuation or upper case letters.</li>
<li>The number of asterisks you put should correspond to the number of letters in the censored word.</li>
</ul>
</div>

```python 
#my code
def censor(text,word):
  separated_text = text.split(' ')
  censored = ''
  censored = '*' * len(word)
  for words in separated_text:
    if words == word:
      updated_text = text.replace(words,censored)
  return updated_text

print(censor("this hack is wack hack", "hack"))

#codecademy:
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print censor("this hack is wack hack", "hack")
```

### count
Great work so far. Let's finish up by practicing with a few functions that take lists as arguments.

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>count</code> that has two arguments called <code>sequence</code> and <code>item</code>. </p>
<p>Return the number of times the item occurs in the list.</p>
<p>For example: <code>count([1, 2, 1, 1], 1)</code> should return <code>3</code> (because <code>1</code> appears 3 times in the list).</p>
<ul>
<li>There is a list method in Python that you can use for this, but you should do it the long way for practice.</li>
<li>Your function should return an integer.</li>
<li>The item you input may be an integer, string, float, or even another list!</li>
<li>Be careful not to use <code>list</code> as a variable name in your code—it's a reserved word in Python!</li>
</ul>
</div>

```python
#my code:

def count(sequence,item):
  count = 0
  for num in sequence:
    if num == item:
      count += 1
  return count

print(count([1, 2, 1, 1], 1))

#second way:
def count(sequence,item):
  count = 0
  while item in sequence:
    sequence.remove(item)
    count += 1
  else:
    count = 0
  return count

print(count([1, 2, 1, 1], 1))

#codecademy code:
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count
  
print count([1, 2, 1, 1], 1)
```

### purify
Awesome! Now let's practice filtering a list.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>purify</code> that takes in a list of numbers, removes all odd numbers in the list, and <code>return</code>s the result. For example, <code>purify([1,2,3])</code> should return <code>[2]</code>.</p>
<p>Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.</p>
</div>

```python
#my code
def purify(numbers):
  even_numbers = []
  for i in numbers:
    if i % 2 == 0:
      even_numbers.append(i)
  return even_numbers    

print(purify([2,3,4,5]))
```

### product
Great! Now let's try a little multiplication.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Define a function called <code>product</code> that takes a list of integers as input and returns the product of all of the elements in the list. For example: <code>product([4, 5, 5])</code>  should return <code>100</code> (because <code>4 * 5 * 5</code> is <code>100</code>).</p>
<ul>
<li>Don't worry about the list being empty. </li>
<li>Your function should return an integer.</li>
</ul>
</div>

```python
def product(num):
  product = 1
  for i in num:
    product *= i
  return product 
```

### remove_duplicates
Awesome! Now for something a bit trickier.

###### TASK
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Write a function <code>remove_duplicates</code> that takes in a list and removes elements of the list that are the same.</p>
<p>For example: <code>remove_duplicates([1, 1, 2, 2])</code> should return <code>[1, 2]</code>.</p>
<ul>
<li>Don't remove every occurrence, since you need to keep a single occurrence of a number.</li>
<li>The order in which you present your output does not matter. So returning <code>[1, 2, 3]</code> is the same as returning <code>[3, 1, 2]</code>.</li>
<li><strong>Do not</strong> modify the list you take as input! Instead, <code>return</code> a new list.</li>
</ul>
</div>

```python 
#my code:
def remove_duplicates(dupl):
  rem_dupl = []
  for num in dupl:
    if num not in rem_dupl:
      rem_dupl.append(num)
  return rem_dupl
  
#codecademy:
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
    # Sort the input list from low to high    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
  
print remove_duplicates([1, 1, 2, 2])
```

### median
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Great work! You've covered a lot in these exercises. Last but not least, let's write a function to find the median of a list.</p>
<p>The <em>median</em> is the middle number in a sorted sequence of numbers. </p>
<p>Finding the median of <code>[7, 12, 3, 1, 6]</code> would first consist of sorting the sequence into <code>[1, 3, 6, 7, 12]</code> and then locating the middle value, which would be <code>6</code>. </p>
<p>If you are given a sequence with an <strong>even</strong> number of elements, you must average the two elements surrounding the middle.</p>
<p>For example, the median of the sequence <code>[7, 3, 1, 4]</code> is <code>3.5</code>, since the middle elements after sorting the list are <code>3</code> and <code>4</code> and <code>(3 + 4) / (2.0)</code> is <code>3.5</code>.</p>
<p>You can sort the sequence using the <code>sorted()</code> function, like so:</p>
<pre><code class="lang-py"><span language="py" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror"><span class="cm-builtin">sorted</span>(<!-- -->[<span class="cm-number">5</span>,<!-- --> <span class="cm-number">2</span>,<!-- --> <span class="cm-number">3</span>,<!-- --> <span class="cm-number">1</span>,<!-- --> <span class="cm-number">4</span>]<!-- -->)<!-- -->
<!-- -->[<span class="cm-number">1</span>,<!-- --> <span class="cm-number">2</span>,<!-- --> <span class="cm-number">3</span>,<!-- --> <span class="cm-number">4</span>,<!-- --> <span class="cm-number">5</span>]</div></span>
</code></pre>
</div>

###### TASK 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>Write a function called <code>median</code> that takes a list as an input and returns the median value of the list. For example: <code>median([1, 1, 2])</code> should return <code>1</code>. </p>
<ul>
<li>The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!</li>
<li>If the list contains an even number of elements, your function should return the average of the middle two.</li>
</ul>
</div>

```python
#my code
def median(numbers):
  numbers = sorted(numbers)
  length = len(numbers)
  if length % 2 == 0:
    return (numbers[length/2] + numbers[length/2 - 1]) / 2.0
  else:
    return numbers[length/2]
    
#codecademy
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])
```
