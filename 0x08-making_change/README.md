<h1 align="center"><b>0X08. MAKING CHANGE</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Additional Resources
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/ktLaKIVRkq_-byFO-_-aGg" target="_blank" title="Mock Technical Interview">Mock Technical Interview</a></li>
</ul>


<!--==================================================-->
<br>

## Requirements
<h3>General</h3>

- Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly <code>#!/usr/bin/python3</code>
- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Your code should use the <code>PEP 8</code> style (version 1.7.x)
- All your files must be executable

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Change comes from within
`mandatory`

File: [0-making_change.py]()
</summary>

<p>Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount <code>total</code>.</p>

<ul>
<li>Prototype: <code>def makeChange(coins, total)</code></li>
<li>Return: fewest number of coins needed to meet <code>total</code>
<ul>
<li>If <code>total</code> is <code>0</code> or less, return <code>0</code></li>
<li>If <code>total</code> cannot be met by any number of coins you have, return <code>-1</code></li>
</ul></li>
<li><code>coins</code> is a list of the values of the coins in your possession</li>
<li>The value of a coin will always be an integer greater than <code>0</code></li>
<li>You can assume you have an infinite number of each denomination of coin in the list</li>
<li>Your solution’s runtime will be evaluated in this task</li>
</ul>

<pre><code>carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
</code></pre>

<pre><code>carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
</code></pre>


</details>

