# Before start coding(everytime)
Every time before you start coding, please do the following:
> git pull
This crucial step is to **download all the new updates** from remote to your local machine.

# Always Check your branch
We should always be on the **development branch**. To make sure:
> git branch
The output should be:
* development
  master
If not, please do the following to switch branch:
> git checkout development

# Upload your modifications
(Two things to make sure before uploading: 1. git pull already; 2. on the development branch)
Then, we are good to go!
> git add -A
> git commit -m "The message you want to yell"
> git push origin development
The steps above is to 
  1. add all the files
  2. commit them with message given
  3. push them onto the remove repository

# Comments
1. All the CSV files are ignored(not included) in GitHub, due to the large yet unnecessary memory taken by them. But you can/should keep them in your local folder(we need them for jupyter), because it will be **ignored automatically** when doing git add -A.
2. We will conquer it!!! ;p
