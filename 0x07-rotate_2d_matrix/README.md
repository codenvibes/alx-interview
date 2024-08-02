<h1 align="center"><b>0X07. ROTATE 2D MATRIX</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
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

