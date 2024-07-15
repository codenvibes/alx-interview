<h1 align="center"><b>0X01. LOCKBOXES</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Must Know
For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>Lists and List Manipulation</strong>:</p>
<ul>
<li>Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.</li>
<li><a href="https://docs.python.org/3/tutorial/datastructures.html" target="_blank" title="Python Lists (Python Official Documentation)">Python Lists (Python Official Documentation)</a></li>
</ul></li>
<li><p><strong>Graph Theory Basics</strong>:</p>
<ul>
<li>Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.</li>
<li><a href="https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs" target="_blank" title="Graph Theory (Khan Academy)">Graph Theory (Khan Academy)</a></li>
</ul></li>
<li><p><strong>Algorithmic Complexity</strong>:</p>
<ul>
<li>Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.</li>
<li><a href="https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/g" target="_blank" title="Big O Notation (GeeksforGeeks)">Big O Notation (GeeksforGeeks)</a></li>
</ul></li>
<li><p><strong>Recursion</strong>:</p>
<ul>
<li>Some solutions might require a recursive approach to traverse through the boxes and keys.</li>
<li><a href="https://realpython.com/python-recursion/" target="_blank" title="Recursion in Python (Real Python)">Recursion in Python (Real Python)</a></li>
</ul></li>
<li><p><strong>Queue and Stack</strong>:</p>
<ul>
<li>Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.</li>
<li><a href="https://intranet.alxswe.com/rltoken/CQLm4RJrdwyo2DAcNCtwIA" target="_blank" title="Python Queue and Stack (GeeksforGeeks)">Python Queue and Stack (GeeksforGeeks)</a></li>
</ul></li>
<li><p><strong>Set Operations</strong>:</p>
<ul>
<li>Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.</li>
<li><a href="https://intranet.alxswe.com/rltoken/zkmtaPqAbKyxx41kRw7ulA" target="_blank" title="Python Sets (Python Official Documentation)">Python Sets (Python Official Documentation)</a></li>
</ul></li>
</ol>

By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.


<!--==================================================-->
<br>

## Additional Resources
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/TJ0FJhWeEGolIqMpwBn7Pg" target="_blank" title="Mock Technical Interview">Mock Technical Interview</a></li>
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

### 0. Lockboxes
`mandatory`

File: [0-lockboxes.py]()
</summary>

<p>You have <code>n</code> number of locked boxes in front of you. 
Each box is numbered sequentially from <code>0</code> to <code>n - 1</code> and each box may contain keys to the other boxes. </p>

<p>Write a method that determines if all the boxes can be opened.</p>

<ul>
<li>Prototype: <code>def canUnlockAll(boxes)</code></li>
<li><code>boxes</code> is a list of lists</li>
<li>A key with the same number as a box opens that box</li>
<li>You can assume all keys will be positive integers

<ul>
<li>There can be keys that do not have boxes</li>
</ul></li>
<li>The first box <code>boxes[0]</code> is unlocked</li>
<li>Return <code>True</code> if all boxes can be opened, else return <code>False</code></li>
</ul>

<pre><code>carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
</code></pre>

<pre><code>carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
</code></pre>


</details>

