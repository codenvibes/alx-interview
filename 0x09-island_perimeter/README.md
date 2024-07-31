<h1 align="center"><b>0X09. ISLAND PERIMETER</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Additional Resources
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/9ZYjQgC9HvOLZiHxmgd89Q" target="_blank" title="Mock Technical Interviews">Mock Technical Interviews</a></li>
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

