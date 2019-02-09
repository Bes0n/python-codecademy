## Bank Account
<div class="theme__22QeW-d-YRjfwg7z9oiZH_"><p>In this project, we'll create a Python class that can be used to create and manipulate a personal bank account.</p>
<p>The bank account class you'll create should have methods for each of the following:</p>
<ul>
<li>Accepting deposits</li>
<li>Allowing withdrawals</li>
<li>Showing the balance</li>
<li>Showing the details of the account</li>
</ul>
<p>Note: As with professional software development, you should be saving your code very often. As you code, make sure you click the "Save" button below to save your code/changes. Otherwise, you run the risk of losing all your code!</p>
<p>Let's begin!</p>
<p> If you get stuck during this project, check out the <strong>project walkthrough video</strong> which can be found at the bottom of the page after the final step of the project.</p>
</div>

###### TASK
<p>On line 1, create a <code>BankAccount</code> class.</p>

<p>Next, add a <a href="https://www.codecademy.com/en/courses/learn-python/lessons/introduction-to-classes/exercises/class-scope" target="_blank">member variable</a> called <code>balance</code> and set it equal to <code>0</code>. This will represent the starting balance of any new <code>BankAccount</code> object.</p>

<p>Add the <code>__init__()</code> method that takes the default <code>self</code> parameter and an additional <code>name</code> parameter. Later, we'll use the <code>name</code> parameter to specify who the account belongs to.</p>

<p>Inside the <code>__init__()</code> method, assign the <code>self.name</code> property to the <code>name</code> parameter that the method accepts.</p>

<div class="theme__22QeW-d-YRjfwg7z9oiZH_ narrativeMarkdown__1pqyNDZ_zljr-gC8Q1pur9"><p>Well done. This method will make sure that whatever name the user types (when creating an object of this class) will be attributed to that object.</p>
<p>Next, add a <code>__repr__()</code> method that takes the default <code>self</code> parameter.</p>
</div>

