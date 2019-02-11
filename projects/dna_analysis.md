## DNA Analysis
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>In this project, we'll use many of the concepts you've learned throughout the Python course in order to do some DNA analysis for a crime investigation.</p>
<p>The scenario:</p>
<p>A spy deleted important files from a computer. There were a few witnesses at the scene of the crime, but no one is sure who exactly the spy was. Three possible suspects were apprehended based on surveillance video. Each suspect had a sample of DNA taken from them. The computer's keyboard was also swabbed for DNA evidence and, luckily, one small DNA sample was successfully retrieved from the computer's keyboard.</p>
<p>Given the three suspects' DNA and the sample DNA retreived from the keyboard, it's up to you to figure out who the spy is!</p>
<p>The project should have methods for each of the following:</p>
<ol>
<li>Given a file, read in the DNA for each suspect and save it as a string</li>
<li>Take a DNA string and split it into a list of <a href="https://en.wikipedia.org/wiki/DNA_codon_table" target="_blank">codons</a></li>
<li>Iterate through a suspect's codon list to see how many of their codons match the sample codons</li>
<li>Pick the right suspect to continue the investigation on</li>
</ol>
<p>Note: As with professional software development, you should be saving your code very often. As you code, make sure you click the "Save" button below to save your code/changes. Otherwise, you run the risk of losing all your code!</p>
<p>Let's begin!</p>
<p>If you get stuck during this project, check out the <strong>project walkthrough video</strong> which can be found at the bottom of the page after the final step of the project.</p>
</div>

###### Step 1. 
<p>First, take a look at the list of codons on Line 1 of <strong>dna.py</strong>. It contains the three codons that were retrieved from the computer's keyboard. It will be up to you to match these codons to the suspects' DNA samples.</p>

```python
sample = ['GTA','GGG','CAC']

```

###### Step 2. 
<p>If you're curious, check out the suspects' DNA samples by clicking on the files titled <strong>suspect1.txt</strong>, <strong>suspect2.txt</strong>, or <strong>suspect3.txt</strong>. It's important that you do not edit them, as that could result in a project that functions incorrectly.</p>

###### Step 3. 
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Let's start off by writing the method that will read a suspect's DNA sample. </p>
<p>On Line 3, start by adding a method called <code>read_dna</code>. It should take one parameter, called <code>dna_file</code>.</p>
</div>

###### Step 4. 
<p>Inside of the method, create a variable called <code>dna_data</code> and set it equal to an empty string. This will be the string that will eventually contain a suspect's DNA.</p>

```python
def read_dna(dna_file):
  dna_data = ""
```

###### Step 5. 
<p>On the next line, still inside of the method, use <code>with</code> to open <code>dna_file</code> in read-only mode, as <code>f</code>. We're using <code>f</code> as short for "file." Using "file" would not be allowed since it's a keyword in Python.</p>

```python
  with open(dna_file, "r") as f:
```

###### Step 6. 
<p>Now that the file is open, add a <code>for</code> loop inside the <code>with</code> block. The loop should iterate through each <code>line</code> in <code>f</code>.</p>

###### Step 7.
<p>On the next line, inside of the <code>for</code> loop, add <code>line</code> to the empty <code>dna_data</code> using <code>+=</code>.</p>

###### Step 8.
<p>Finally, to complete the method, return <code>dna_data</code> on the next line. This line of code should align with the first line of indented code in the method (which means it's not included in the <code>with</code> block).</p>

```python
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data
```

###### Step 9.
<p>Great! When used, this method will take in a file, read it, add the file's contents to an empty string, and return the updated string. This will come in handy in catching the spy.</p>

###### Step 10.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Next, we'll need a method that will take a string, create a list of codons from that string, and return the list. This will make the DNA analysis much easier later.</p>
<p>Add a new method called <code>dna_codons</code>. It should take one parameter called <code>dna</code>.</p>
</div>

###### Step 11.
<p>We'll need an empty list to add the codons to. On the next line, inside the method, create an empty list called <code>codons</code>.</p>

###### Step 12.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>If you previewed a suspect's DNA sample (for example, in <strong>suspect1.txt</strong>), you should have seen that the DNA sample contains a lot of <a href="https://en.wikipedia.org/wiki/DNA#Base_pairing" target="_blank">letters (DNA base pairs)</a>.</p>
<p><a href="http://dictionary.reference.com/browse/codon" target="_blank">Codons</a> are 3-letter-long units of genetic code. We'll have to iterate through a suspect's DNA string and chop the string into codons (3 letter strings).</p>
<p>On the next line, add a <code>for</code> loop. The loop should have a <code>range</code> from <code>0</code> to the length of <code>dna</code>. It should also iterate in increments of <code>3</code>.</p>
<p><a href="https://docs.python.org/2/library/functions.html#range" target="_blank">This documentation</a> shows to specify increments with <code>range</code>.</p>
</div>

###### Step 13.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Next, we'll want to make sure that the iterator <code>i</code> doesn't exceed the length of <code>dna</code>, so let's check for that on the next line.</p>
<p>Inside the <code>for</code> loop, add a line that checks if the iterator, when incremented by 3, exceeds the length of <code>dna</code>.</p>
</div>

```python
  def dna_codons(dna):
    codons = []
    for letters in range(0, len(dna), 3):
      if (letters + 3) < len(dna):
```

###### Step 14.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>The line of code that you just wrote will make sure that you don't add a string to the codon list that isn't at least 3 letters long.</p>
<p>Now, we'll want to add the codon into the <code>codon</code> list that is currently empty. </p>
<p>On the next line, add to the list using the <code>.append()</code> method. Since the iterator <code>i</code> starts at 0, we'll be adding the first three characters only.</p>
</div>

###### Step 15.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Great! Now that the codon list contains all the codons we need, we'll need to return the list.</p>
<p>On the next line, return <code>codons</code>. This line of code will have to be written at the level of indentation that aligns with the <code>for</code> loop.</p>
</div>

```python
  def dna_codons(dna):
    codons = []
    for letters in range(0, len(dna), 3):
      if (letters + 3) < len(dna):
        codons.append(dna[i:i + 3])
    return codons
```

###### Step 16.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Perfect - you just added a method that will iterate through a string, slice it into smaller strings that are 3 letters long, and add them to a list. This functionality will help us match the sample to a suspect's DNA later.</p>
<p>The next step is to create a method that will iterate through both the sample and a suspect's DNA. The method should count the number of times a codon in the sample matches a codon in the suspect's DNA.</p>
<p>On the next line, add a method called <code>match_dna</code>. It should take one parameter called <code>dna</code>.</p>
</div>

###### Step 17.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>We'll need a way to count the number of times a codon from the sample matches a codon from a suspect's DNA. </p>
<p>Inside the method, add a variable called <code>matches</code> and set it equal to zero. We will increment this variable by 1 every time there is a match.</p>
</div>

###### Step 18.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>The parameter that this method takes is a list, so we'll have to start iterating through the list first to find matches.</p>
<p>On the next line, add a <code>for</code> loop that iterates through the <code>dna</code> list. Call the iterator <code>codon</code>.</p>
</div>

###### Step 19.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>If a codon in the DNA matches a codon in the sample, then we've got a single match! We'll increment the <code>matches</code> variable to reflect that.</p>
<p>Inside the <code>if</code> statement, increment <code>matches</code> by <code>1</code> using the <code>+=</code> operator.</p>
</div>

###### Step 20.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>If a codon in the DNA matches a codon in the sample, then we've got a single match! We'll increment the <code>matches</code> variable to reflect that.</p>
<p>Inside the <code>if</code> statement, increment <code>matches</code> by <code>1</code> using the <code>+=</code> operator.</p>
</div>

###### Step 21.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Since the <code>match_dna()</code> method counts matches, it would be useful if it returned the number of matches as well.</p>
<p>As the last line of this method, return the <code>matches</code> variable.</p>
</div>

```python
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches
```

###### Step 22.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Fantastic! You've added a method that automates a task that would normally take a long time to manually complete. Instead of having to manually match codons for three different suspects, this method does it for us and counts the matches.</p>
<p>We have most of the methods we need, but let's add one more that will determine if a suspect is the criminal.</p>
<p>Next, add a method called <code>is_criminal</code> that takes a parameter called <code>dna_sample</code>.</p>
</div>

###### Step 23.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>The <code>is_criminal()</code> method should use the other methods we've created to determine who the criminal is.</p>
<p>The first thing the method will do is read in DNA samples and create a string to hold them.</p>
<p>Inside the method, create a variable called <code>dna_data</code>. Set it equal to the result of calling the <code>read_dna()</code> method on the <code>dna_sample</code> parameter.</p>
</div>

###### Step 24.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Now that we have the DNA data in a string, it's time to call the <code>dna_codons()</code> method to chop the string into a list of codons.</p>
<p>On the next line, create a variable called <code>codons</code>. Set it equal to the result of calling the <code>dna_codons()</code> method with <code>dna_data</code> as the argument.</p>
</div>

###### Step 25.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Now that we have the codon list, it's time to match the sample with the DNA.</p>
<p>On the next line, create a variable called <code>num_matches</code>. Set it equal to the result of calling the <code>match_dna()</code> method  with <code>codons</code> as the argument.</p>
</div>

###### Step 26.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>To complete the method, we will have to add in statements that check to see if the number of matches is significant.</p>
<p>Next, add an <code>if</code> statement that checks if the number of matches is greater than or equal to three.</p>
</div>

###### Step 27.
<p>If the number of matches is greater than or equal to three, print out the number of matches using string formatting, as well as a message stating that the investigation should continue.</p>

###### Step 28.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Otherwise, the suspect can be set free.</p>
<p>Add an <code>else</code> block that prints the number of matches using string formatting, as well as a message stating the suspect can be freed.</p>
</div>

```python
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print("Number of matches is: %s" % num_matches)
    print("Investigation should continue")
  else:
    print("Number of matches is: %s" % num_matches)
    print("Suspect can be freed")
```

###### Step 29.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>That's it! This method will do all the hard work of reading a DNA sample from a suspect, comparing it to a DNA sample from the crime scene, and letting the user know whether the suspect is a criminal.</p>
<p>For all of this to work, we actually have to call the method <code>is_criminal()</code> on the <code>.txt</code> files you previewed earlier.</p>
<p>On the next three lines, outside of any method, call the <code>is_criminal()</code> method separately on the three <code>.txt</code> files.</p>
</div>

```python
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
```

###### Step 30.
<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Ready to find out who the spy is?</p>
<p>In the terminal, type the following command and hit "Enter" on your keyboard:</p>
<pre><code class="lang-bash"><span language="bash" class="CodeBlock__3-kebd7REMI5aXkez6K-B wrap__yxnEyEmMpigk6-3_Wvbzo defaults__1l9bk0Z91YqvzRByZKNgHF cc__1zsV8w8Rj_vs2ayVLJ-2x undefined" data-reactroot=""><div class="CodeMirror">python dna.py</div></span>
</code></pre>
<p>You should see the analysis run and find out who the spy is!</p>
</div>

###### COMPLETE CODE

```python

sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data

def dna_codons(dna):
  codons = []
  for letters in range(0, len(dna), 3):
    if (letters + 3) < len(dna):
      codons.append(dna[letters:letters + 3])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print("Number of matches is: %s" % num_matches)
    print("Investigation should continue")
  else:
    print("Number of matches is: %s" % num_matches)
    print("Suspect can be freed")
    
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")

#Output
```
