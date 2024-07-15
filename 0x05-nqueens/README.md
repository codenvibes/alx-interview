<h1 align="center"><b>0X05. N QUEENS</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Additional Resources
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/aQ3uJmGVeZa-R6B1jYTjXg" target="_blank" title="Mock Interview">Mock Interview</a></li>
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
- Your code should use the <code>PEP 8</code> style (version 1.7.*)
- All your files must be executable

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. N queens
`mandatory`

File: [0-nqueens.py]()
</summary>

<p><img src="./Project_ 0x05. N Queens _ Nairobi Intranet_files/Judit-photo1_602x433.jpg"/><br/>
<small>Chess grandmaster <a href="https://intranet.alxswe.com/rltoken/fZ1ecpPEmVL9nvkBn8WQGg" target="_blank" title="Judit Polgár">Judit Polgár</a>, the strongest female chess player of all time</small><br/>
<br/></p>

<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>

<ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don’t have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>

<p>Read: <a href="https://intranet.alxswe.com/rltoken/ghWqI1wvx6g-Ul7nrufMKA" target="_blank" title="Queen">Queen</a>, <a href="https://intranet.alxswe.com/rltoken/-hgZbgRFkwmxaKnLnCIuEQ" target="_blank" title="Backtracking">Backtracking</a></p>

<pre><code>julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>


</details>

