## Before start coding (everytime)
Every time before you start coding, please do the following:
<pre><code>git pull</code></pre>
This crucial step is to **download all the new updates** from remote repository to your local machine.
<br />

## Always Check your branch
We should always be on the **development branch**. To make sure:
<pre><code>git branch</code></pre>
The output should be:
<pre><code>* development
  master</code></pre>
If not, please do the following to switch branch:
<pre><code>git checkout development</code></pre>
<br />

## Upload your modifications
Two things to make sure before uploading: 
  1. git pull already
  2. you're on the development branch
<br />
Then, we are good to go!
```git
git add -A
git commit -m "The message you want to yell"
git push origin development
```
The steps above is to 
  1. add all the files
  2. commit them with message given
  3. push them onto the remove repository
<br />

## Comments
1. All the CSV files are ignored(not included) in GitHub, due to the large yet unnecessary memory taken by them. But you can/should keep them in your local folder(we need them for jupyter), because it will be **ignored automatically** when doing <code>git add -A</code>.
2. We will conquer it!!! ;p
