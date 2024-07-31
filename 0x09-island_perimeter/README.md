<h1 align="center"><b>0X09. ISLAND PERIMETER</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>
<p>For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.</p>


<br>
<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>2D Arrays (Matrices)</strong>:</p>

<ul>
<li>Accessing and iterating over elements in a 2D array.</li>
<li>Understanding how to navigate through adjacent cells (horizontally and vertically).</li>
</ul></li>
<li><p><strong>Conditional Logic</strong>:</p>

<ul>
<li>Applying conditions to determine whether a cell contributes to the perimeter of the island.</li>
</ul></li>
<li><p><strong>Counting Techniques</strong>:</p>

<ul>
<li>Developing a method to count the edges that contribute to the island’s perimeter.</li>
</ul></li>
<li><p><strong>Problem-Solving Strategies</strong>:</p>

<ul>
<li>Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.</li>
</ul></li>
<li><p><strong>Python Programming</strong>:</p>

<ul>
<li>Nested loops for iterating over grid cells.</li>
<li>Conditional statements to check the status of adjacent cells.</li>
</ul></li>
</ol>

<br>
<h3>Resources:</h3>

<ul>
<li><p><strong>Python Official Documentation</strong>:</p>

<ul>
<li><a href="https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions" title="Nested Lists" target="_blank">Nested Lists</a>: Understanding how to work with lists within lists in Python.</li>
</ul></li>
<li><p><strong>GeeksforGeeks Articles</strong>:</p>

<ul>
<li><a href="https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/" title="Python Multi-dimensional Arrays" target="_blank">Python Multi-dimensional Arrays</a>: A guide to working with 2D arrays in Python effectively.</li>
</ul></li>
<li><p><strong>TutorialsPoint</strong>:</p>

<ul>
<li><a href="https://www.tutorialspoint.com/python/python_lists.htm" title="Python Lists" target="_blank">Python Lists</a>: Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.</li>
</ul></li>
<li><p><strong>YouTube Tutorials</strong>:</p>

<ul>
<li><a href="https://www.youtube.com/watch?v=aNzepGawwCI" title="Python 2D arrays and lists" target="_blank">Python 2D arrays and lists</a></li>
</ul></li>
</ul>

<p>By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.</p>


<br>

## Additional Resources
<ul>
<li><a href="https://www.youtube.com/watch?feature=shared&v=fFgEM6CMQc4" target="_blank" title="Mock Technical Interviews">Mock Technical Interviews</a></li>
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
- Your code should use the <code>PEP 8</code> style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Island Perimeter
`mandatory`

File: [0-island_perimeter.py]()
</summary>

<p>Create a function <code>def island_perimeter(grid):</code> that returns the perimeter of the island described in <code>grid</code>:</p>

<ul>
<li><code>grid</code> is a list of list of integers:

<ul>
<li>0 represents water</li>
<li>1 represents land</li>
<li>Each cell is square, with a side length of 1</li>
<li>Cells are connected horizontally/vertically (not diagonally). </li>
<li><code>grid</code> is rectangular, with its width and height not exceeding 100</li>
</ul></li>
<li>The grid is completely surrounded by water</li>
<li>There is only one island (or nothing).</li>
<li>The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$ 
</code></pre>


</details>

