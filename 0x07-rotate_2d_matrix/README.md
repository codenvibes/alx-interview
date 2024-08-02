<h1 align="center"><b>0X07. ROTATE 2D MATRIX</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>
<p>For the “0. Rotate 2D Matrix” project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.</p>

<br>
<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>Matrix Representation in Python</strong>:</p>

<ul>
<li>Understanding how 2D matrices are represented using lists of lists in Python.</li>
<li>Accessing and modifying elements in a 2D matrix.</li>
</ul></li>
<li><p><strong>In-place Operations</strong>:</p>

<ul>
<li>Performing operations on data without creating a copy of the data structure.</li>
<li>The importance of minimizing space complexity by modifying the matrix in place.</li>
</ul></li>
<li><p><strong>Matrix Transposition</strong>:</p>

<ul>
<li>Understanding the concept of transposing a matrix (swapping rows and columns).</li>
<li>Implementing matrix transposition as a step in the rotation process.</li>
</ul></li>
<li><p><strong>Reversing Rows in a Matrix</strong>:</p>

<ul>
<li>Manipulating rows of a matrix by reversing their order as part of the rotation process.</li>
</ul></li>
<li><p><strong>Nested Loops</strong>:</p>

<ul>
<li>Using nested loops to iterate through 2D data structures like matrices.</li>
<li>Modifying elements within nested loops to achieve the desired rotation.</li>
</ul></li>
</ol>

<br>
<h3>Resources:</h3>

<ul>
<li><p><strong>Python Official Documentation</strong>:</p>

<ul>
<li><a href="https://intranet.alxswe.com/rltoken/eZc_ELGxUgkuc4kkE_fd7Q" title="Data Structures (list comprehensions, nested list comprehension)" target="_blank">Data Structures (list comprehensions, nested list comprehension)</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/0ORj179giGhGe8jpcxBkXg" title="More on Lists" target="_blank">More on Lists</a></li>
</ul></li>
<li><p><strong>GeeksforGeeks Articles</strong>:</p>

<ul>
<li><a href="https://intranet.alxswe.com/rltoken/9T8w4mtiIIRDtfLSmEmrLA" title="Inplace rotate square matrix by 90 degrees" target="_blank">Inplace rotate square matrix by 90 degrees</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/JdIFvtej2hMW-Wd9ABHMOA" title="Transpose a matrix in Single line in Python" target="_blank">Transpose a matrix in Single line in Python</a></li>
</ul></li>
<li><p><strong>TutorialsPoint</strong>:</p>

<ul>
<li><a href="https://intranet.alxswe.com/rltoken/rFmzUTpaLGqDXjGA6D9eYw" title="Python Lists" target="_blank">Python Lists</a> for basics of list manipulation in Python.</li>
</ul></li>
</ul>

<p>By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.</p>


<br>

## Additional Resources
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/4GPWA9C2AJHtpdGxuIHEPA" target="_blank" title="Mock Technical Interview">Mock Technical Interview</a></li>
</ul>


<!--==================================================-->
<br>

## Requirements
<h3>General</h3>

- Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.8.10)
- All your files should end with a new line
- The first line of all your files should be exactly <code>#!/usr/bin/python3</code>
- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Your code should use the <code>pycodestyle</code> style (version 2.8.0)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Rotate 2D Matrix
`mandatory`

File: [0-rotate_2d_matrix.py]()
</summary>

<p>Given an <code>n</code> x <code>n</code> 2D matrix, rotate it 90 degrees clockwise.</p>

<ul>
<li>Prototype: <code>def rotate_2d_matrix(matrix):</code></li>
<li>Do not return anything. The matrix must be edited <strong>in-place</strong>.</li>
<li>You can assume the matrix will have 2 dimensions and will not be empty.</li>
</ul>

<pre><code>jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
</code></pre>


</details>

