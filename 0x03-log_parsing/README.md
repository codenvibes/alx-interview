<h1 align="center"><b>0X03. LOG PARSING</b></h1>
<div align="center"><code>Algorithm</code> <code>Python</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->

<br>

<p>For the “0x03. Log Parsing” project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. 
This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. 
Here’s a list of concepts and resources that you might find useful:</p>

<br>

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>File I/O in Python</strong>:</p>

<ul>
<li>Understand how to read from <code>sys.stdin</code> line by line.</li>
<li><a href="https://docs.python.org/3/tutorial/inputoutput.html" title="Python Input and Output" target="_blank">Python Input and Output</a></li>
</ul></li>
<li><p><strong>Signal Handling in Python</strong>:</p>

<ul>
<li>Handling keyboard interruption (CTRL + C) using signal handling in Python.</li>
<li><a href="https://docs.python.org/3/library/signal.html" title="Python Signal Handling" target="_blank">Python Signal Handling</a></li>
</ul></li>
<li><p><strong>Data Processing</strong>:</p>

<ul>
<li>Parsing strings to extract specific data points.</li>
<li>Aggregating data to compute summaries.</li>
</ul></li>
<li><p><strong>Regular Expressions</strong>:</p>

<ul>
<li>Using regular expressions to validate the format of each line.</li>
<li><a href="https://docs.python.org/3/library/re.html" title="Python Regular Expressions" target="_blank">Python Regular Expressions</a></li>
</ul></li>
<li><p><strong>Dictionaries in Python</strong>:</p>

<ul>
<li>Using dictionaries to count occurrences of status codes and accumulate file sizes.</li>
<li><a href="https://intranet.alxswe.com/rltoken/JM-RpavKkb8yanxWEnNYJw" title="Python Dictionaries" target="_blank">Python Dictionaries</a></li>
</ul></li>
<li><p><strong>Exception Handling</strong>:</p>

<ul>
<li>Handling possible exceptions that may arise during file reading and data processing.</li>
<li><a href="https://intranet.alxswe.com/rltoken/OA2PlryrYA2gyCCKIsdgUw" title="Python Exceptions" target="_blank">Python Exceptions</a></li>
</ul></li>
</ol>

<p>By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.</p>


<br>

## Additional Resources
<ul>
<li><a href="https://intranet.alxswe.com/rltoken/VlOaXKkbecRYdnTLaLU1lg" target="_blank" title="Mock Technical Interview">Mock Technical Interview</a></li>
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
- The length of your files will be tested using <code>wc</code>

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Log parsing
`mandatory`

File: [0-stats.py]()
</summary>

<p>Write a script that reads <code>stdin</code> line by line and computes metrics:</p>

<ul>
<li>Input format: <code>&lt;IP Address&gt; - [&lt;date&gt;] "GET /projects/260 HTTP/1.1" &lt;status code&gt; &lt;file size&gt;</code> (if the format is not this one, the line must be skipped)</li>
<li>After every 10 lines and/or a keyboard interruption (<code>CTRL + C</code>), print these statistics from the beginning:

<ul>
<li>Total file size: <code>File size: &lt;total size&gt;</code></li>
<li>where <code>&lt;total size&gt;</code> is the sum of all previous <code>&lt;file size&gt;</code> (see input format above)</li>
<li>Number of lines by status code: 

<ul>
<li>possible status code: <code>200</code>, <code>301</code>, <code>400</code>, <code>401</code>, <code>403</code>, <code>404</code>, <code>405</code> and <code>500</code></li>
<li>if a status code doesn’t appear or is not an integer, don’t print anything for this status code</li>
<li>format: <code>&lt;status code&gt;: &lt;number&gt;</code></li>
<li>status codes should be printed in ascending order</li>
</ul></li>
</ul></li>
</ul>

<p><strong>Warning:</strong> In this sample, you will have random value - it’s normal to not have the same output as this one.</p>

<pre><code>alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in &lt;module&gt;
Traceback (most recent call last):
  File "./0-generator.py", line 8, in &lt;module&gt;
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
</code></pre>


</details>

