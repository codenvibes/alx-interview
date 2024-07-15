<h1 align="center"><b>0X04. UTF-8 VALIDATION</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<p>For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts and resources that will be helpful:</p>

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>Bitwise Operations in Python</strong>:</p>

<ul>
<li>Understanding how to manipulate bits in Python, including operations like AND (<code>&amp;</code>), OR (<code>|</code>), XOR (<code>^</code>), NOT (<code>~</code>), shifts (<code>&lt;&lt;</code>, <code>&gt;&gt;</code>).</li>
<li><a href="https://intranet.alxswe.com/rltoken/BslyYNZlXdyxW3_b0WNOcg" title="Python Bitwise Operators" target="_blank">Python Bitwise Operators</a></li>
</ul></li>
<li><p><strong>UTF-8 Encoding Scheme</strong>:</p>

<ul>
<li>Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.</li>
<li>Understanding the patterns that represent a valid UTF-8 encoded character.</li>
<li><a href="https://intranet.alxswe.com/rltoken/oqFi6P1hNvp9aSuNv---IQ" title="UTF-8 Wikipedia" target="_blank">UTF-8 Wikipedia</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/d--jVK8sBSlhkosu7pFzdw" title="Characters, Symbols, and the Unicode Miracle" target="_blank">Characters, Symbols, and the Unicode Miracle</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/9EwaXVds22dSK3IvF5nNCA" title="The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets" target="_blank">The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets</a></li>
</ul></li>
<li><p><strong>Data Representation</strong>:</p>

<ul>
<li>How to represent and work with data at the byte level.</li>
<li>Handling the least significant bits (LSB) of integers to simulate byte data.</li>
</ul></li>
<li><p><strong>List Manipulation in Python</strong>:</p>

<ul>
<li>Iterating through lists, accessing list elements, and understanding list comprehensions.</li>
<li><a href="https://intranet.alxswe.com/rltoken/TaN91MgmOL80GeOGvmldIw" title="Python Lists" target="_blank">Python Lists</a></li>
</ul></li>
<li><p><strong>Boolean Logic</strong>:</p>

<ul>
<li>Applying logical operations to make decisions within the program.</li>
</ul></li>
</ol>

<p>By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.</p>


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

