<h1 align="center"><b>0X04. UTF-8 VALIDATION</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Additional Resource
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/X1lZqipeyegt8pbQ9aXSFQ" target="_blank" title="Mock Technical Interview">Mock Technical Interview</a></li>
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

### 0. UTF-8 Validation
`mandatory`

File: [0-validate_utf8.py]()
</summary>

<p>Write a method that determines if a given data set represents a valid UTF-8 encoding.</p>

<ul>
<li>Prototype: <code>def validUTF8(data)</code></li>
<li>Return: <code>True</code> if data is a valid UTF-8 encoding, else return <code>False</code></li>
<li>A character in UTF-8 can be 1 to 4 bytes long</li>
<li>The data set can contain multiple characters</li>
<li>The data will be represented by a list of integers</li>
<li>Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer</li>
</ul>

<pre><code>carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
</code></pre>

<pre><code>carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
</code></pre>


</details>

