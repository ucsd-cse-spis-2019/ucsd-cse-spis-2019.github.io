---
topic: ACMS Disk Quota Issues
desc: "Disk or file quota exceeded, or what to do when you have weird issues and can't save files"
---

# How to diagnose a disk quota problem

If you suddenly are finding that multiple things that usually work on your ACMS account are not working, e.g. IDLE locks up, web browser locks up, can't open new windows, commands fail with strange error messages, etc., it may be a sign that you are over disk quota.


You can see whether disk quota is the problem by typing <code>quota -vs</code> at the Unix prompt. &nbsp;That looks like this:

```
[spis15t7@ieng6-240]:~:501$ quota -vs
Disk quotas for user spis15t7 (uid 4091): 
     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
acsnfs4:/vol/home/linux/ieng6
                  57328    196M    196M            3214    4000    4000        
[spis15t7@ieng6-240]:~:502$ 
```

*   The number `196M`  in the output above indicates that your quota and your limit in terms of how much disk space 
    you  are allowed to consume on your ACMS account is 196 MB (Megabytes). 

*   The number 57328 in the output above indicates that you are using 57328 blocks of your quota.
    That's fine (a block is usually either 0.5KB or 1KB, and there are 1024KB in a MB.) &nbsp;So this output
    indicates a "good" situation.


Here's what you DON'T want to see:

```
[spis15t7@ieng6-240]:~:501$ quota -vs
Disk quotas for user spis15t7 (uid 4091): 
     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
acsnfs4:/vol/home/linux/ieng6
                  196M    196M    196M            3214    4000    4000        
[spis15t7@ieng6-240]:~:502$
```

That's an example of a problem. &nbsp;The usage and the quota are the same, meaning that you've used up all of your available disk quota. &nbsp; If you try to write to any additional file, you'll end up having trouble. &nbsp;&nbsp;</div>

# Do you have a "disk space" problem, or a "number of files" problem?

The number `3214` in the output above is the "number of files". 

In this example, it is below the quota of 4000, so all is well.

BUT, if it were above the 4000, we'd have a "<b>too many files</b>" problem. &nbsp; Those are investigated in different ways. &nbsp;Read on!

# What is causing this "disk quota" or "number of files quota" being exceeded?

The thing is, it's unlikely that you filled up your disk with ordinary Python files. &nbsp;The problem is more likely some kind of bug either in the system software, or in one of your own programs, that is making REALLY big files somewhere unexpected. &nbsp;You need to *find where the problem is* before you can fix it.

# How to solve a disk quota problem

TEMPORARY VERSION OF INSTRUCTIONS:

TODO: Make these nicer.

<div><span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">1) Finding the problem</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">&nbsp; &nbsp; &nbsp; cd&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (goes to home directory)</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">&nbsp; &nbsp; &nbsp; du –sh *&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (check regular folders)</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">&nbsp; &nbsp; &nbsp; du –sh .[A-z]*&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (check hidden folders)</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">2) Probably:</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">&nbsp; &nbsp; &nbsp; The problem is in ~/.config/google-chrome</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">&nbsp; &nbsp; &nbsp; Try: du –sh ~/.config/google-chrome</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">&nbsp; &nbsp; &nbsp; If its huge (i.e. &gt;50MB) use echo rm –rf ~/.config/google-chromethen</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">up-arrow,</span><br style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">
<span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">&nbsp; &nbsp; &nbsp; and erase “echo”, then return again</span></div>
<div><br>
</div>
<h3>How to solve a too many files problem</h3>

Unlike "disk space", there isn't a nice handy utility built into unix to count the number of files you have. &nbsp;Fortunately, one of my colleagues at UC Santa Barbara, wrote such a utility, and has put it up on his public github repo here:&nbsp;<a href="https://github.com/rkip/countfiles">https://github.com/rkip/countfiles</a>


I've put that in my own directory on ACMS for SPIS 15, so you can run it with this command:

<div><code>~spis19t3/bin/countfiles</code></div>
<div><br>
</div>
<div>If you run that, it will show you which directory has lots of files under it. &nbsp;You can cd into that directory, and repeat the command. &nbsp;Eventually you may find something you can delete to reduce your file count below your quota.</div>
<div><br>
</div>
