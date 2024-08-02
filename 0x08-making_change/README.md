<h1 align="center"><b>0X08. MAKING CHANGE</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->

<br>
<p>For the “0. Change comes from within” project, you will tackle a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient. Below are the key concepts and resources necessary to complete this project successfully.</p>


<br>
<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>Greedy Algorithms</strong>:</p>

<ul>
<li>Understanding how greedy algorithms work and why they are suitable for the coin change problem.</li>
<li>Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.</li>
</ul></li>
<li><p><strong>Dynamic Programming</strong>:</p>

<ul>
<li>Basic principles of dynamic programming as a method to solve optimization problems.</li>
<li>The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.</li>
</ul></li>
<li><p><strong>Algorithmic Complexity</strong>:</p>

<ul>
<li>Analyzing the time and space complexity of algorithms.</li>
<li>Striving for solutions with lower complexity to meet runtime constraints.</li>
</ul></li>
<li><p><strong>Problem-Solving Strategies</strong>:</p>

<ul>
<li>Breaking down the problem into smaller, manageable sub-problems.</li>
<li>Iterative vs recursive approaches to dynamic programming.</li>
</ul></li>
<li><p><strong>Python Programming</strong>:</p>

<ul>
<li>Manipulating lists and using list comprehensions.</li>
<li>Implementing functions with efficient looping and conditional statements.</li>
</ul></li>
</ol>


<br>
<h3>Resources:</h3>

<ul>
<li><p><strong>Python Official Documentation</strong>:</p>

<ul>
<li><a href="https://docs.python.org/3/tutorial/controlflow.html" title="More Control Flow Tools (for loops, if statements)" target="_blank">More Control Flow Tools (for loops, if statements)</a></li>
</ul></li>
<li><p><strong>GeeksforGeeks Articles</strong>:</p>

<ul>
<li><a href="https://www.geeksforgeeks.org/coin-change-dp-7/" title="Coin Change | DP-7" target="_blank">Coin Change | DP-7</a></li>
<li><a href="https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/" title="Greedy Algorithm to find Minimum number of Coins" target="_blank">Greedy Algorithm to find Minimum number of Coins</a></li>
</ul></li>
<li><p><strong>YouTube Tutorials</strong>:</p>

<ul>
<li><a href="https://www.youtube.com/watch?v=jgiZlGzXMBwQ" title="Dynamic Programming - Coin Change Problem" target="_blank">Dynamic Programming - Coin Change Problem</a> for a visual and step-by-step explanation of the dynamic programming approach.</li>
</ul></li>
</ul>

<p>By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. You will need to decide whether a greedy algorithm suffices for your particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests algorithmic skills but also reinforces the importance of choosing the right strategy based on problem constraints.</p>



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

