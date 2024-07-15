<h1 align="center"><b>0X06. STAR WARS API</b></h1>
<div align="center"><code>Algorithm</code> <code>API</code> <code>JavaScript</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->

<br>

<p>The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.</p>

<br>

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>HTTP Requests in JavaScript</strong>:</p>

<ul>
<li>Understanding how to make HTTP requests to external services using the <code>request</code> module or alternatives like <code>fetch</code> in Node.js.</li>
<li><a href="https://www.memberstack.com/blog/node-http-request" title="A Complete Guide to Making HTTP Requests in Node.js" target="_blank">A Complete Guide to Making HTTP Requests in Node.js</a></li>
</ul></li>
<li><p><strong>Working with APIs</strong>:</p>

<ul>
<li>Understanding the basics of RESTful APIs and how to interact with them.</li>
<li>Parsing JSON data returned by APIs.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction" title="Working with APIs in JavaScript" target="_blank">Working with APIs in JavaScript</a></li>
</ul></li>
<li><p><strong>Asynchronous Programming</strong>:</p>

<ul>
<li>Managing asynchronous operations with callbacks, promises, and async/await syntax.</li>
<li>Handling API response data asynchronously.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous" title="Asynchronous Programming in JavaScript" target="_blank">Asynchronous Programming in JavaScript</a></li>
</ul></li>
<li><p><strong>Command Line Arguments in Node.js</strong>:</p>

<ul>
<li>Using the <code>process.argv</code> array to access command-line arguments passed to a Node.js script.</li>
<li><a href="https://tecadmin.net/how-to-parse-command-line-arguments-in-nodejs/" title="How to Parse Command Line Arguments in Node.js" target="_blank">How to Parse Command Line Arguments in Node.js</a></li>
</ul></li>
<li><p><strong>Array Manipulation and Iteration</strong>:</p>

<ul>
<li>Iterating over arrays and manipulating data structures to format and display character names.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array" title="JavaScript Array Methods" target="_blank">JavaScript Array Methods</a></li>
</ul></li>
</ol>

<p>By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.</p>


<br>

## Additional Resources
<ul>
<li><a href="https://www.youtube.com/watch?feature=shared&v=bmqZ5AhNr3g" target="_blank" title="Mock Technical Interview">Mock Technical Interview</a></li>
</ul>


<!--==================================================-->
<br>

## Requirements
<h3>General</h3>

- Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>
- All your files will be interpreted on Ubuntu 20.04 LTS using <code>node</code> (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly <code>#!/usr/bin/node</code>
- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Your code should be <code>semistandard</code> compliant. <a href="https://intranet.alxswe.com/rltoken/9P3gH5mVdJCEKL87E-IMaA" target="_blank" title="Rules of Standard">Rules of Standard</a> + <a href="https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw" target="_blank" title="semicolons on top">semicolons on top</a>. Also as reference: <a href="https://intranet.alxswe.com/rltoken/Xp81RT-Sfi7uE_kNCSXunw" target="_blank" title="AirBnB style">AirBnB style</a>
- All your files must be executable
- The length of your files will be tested using <code>wc</code>
- You are not allowed to use <code>var</code>

<!--==================================================-->
<br>

## More Info
<h3>Install Node 10</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<a href="https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw" target="_blank" title="Documentation">Documentation</a>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

<h3>Install <code>request</code> module and use it</h3>

<a href="https://intranet.alxswe.com/rltoken/BWz2gc45S-nZaxEY6GA6Zw" target="_blank" title="Documentation">Documentation</a>

<pre><code>$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>


<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Star Wars Characters
`mandatory`

File: [0-starwars_characters.js]()
</summary>

<p>Write a script that prints all characters of a Star Wars movie:</p>

<ul>
<li>The first positional argument passed is the Movie ID - example: <code>3</code> = “Return of the Jedi” </li>
<li>Display one character name per line <strong>in the same order as the “characters” list in the <code>/films/</code> endpoint</strong></li>
<li>You must use the <a href="https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg" target="_blank" title="Star wars API">Star wars API</a></li>
<li>You must use the <code>request</code> module</li>
</ul>

<pre><code>alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ 
</code></pre>


</details>

