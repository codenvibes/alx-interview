<h1 align="center"><b>0X02. MINIMUM OPERATIONS</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Additional Resources
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/HX0vuVl1V-9T4vvh8NDCyw" target="_blank" title="Mock Technical Interview">Mock Technical Interview</a></li>
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
- Your code should be documented
- Your code should use the <code>PEP 8</code> style (version 1.7.x)
- All your files must be executable

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Minimum Operations
`mandatory`

File: [0-minoperations.py]()
</summary>

<p>In a text file, there is a single character <code>H</code>. Your text editor can execute only two operations in this file: <code>Copy All</code> and <code>Paste</code>. Given a number <code>n</code>, write a method that calculates the fewest number of operations needed to result in exactly <code>n</code> <code>H</code> characters in the file.</p>

<ul>
<li>Prototype: <code>def minOperations(n)</code></li>
<li>Returns an integer</li>
<li>If <code>n</code> is impossible to achieve, return <code>0</code></li>
</ul>

<p><strong>Example:</strong></p>

<p><code>n = 9</code></p>

<p><code>H</code> =&gt; <code>Copy All</code> =&gt; <code>Paste</code> =&gt; <code>HH</code> =&gt; <code>Paste</code> =&gt;<code>HHH</code> =&gt; <code>Copy All</code> =&gt; <code>Paste</code> =&gt; <code>HHHHHH</code> =&gt; <code>Paste</code> =&gt; <code>HHHHHHHHH</code></p>

<p>Number of operations: <code>6</code></p>

<pre><code>carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
</code></pre>

<pre><code>carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
</code></pre>


</details>

