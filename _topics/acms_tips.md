---
topic: ACMS Account Tips
desc: "A variety of helpful tips for using your ACMS account"
---

Here are a few tips for using your ACMS account.
<div><br>
</div>
<h2>About your ACMS Account</h2>
<h3>What is my spis15xx account?</h3>
<div>
<div style="font-size:13.3333330154419px">Your spis15xx account (where xx are two letters such as aa, ah, bc, etc.) is a username and password that allows you to login to the computers in the basement of the UC Sa Diego CSE building. &nbsp; &nbsp;You can also login to the computer ieng6-240.ucsd.edu using ssh (the Secure Shell.)</div>
</div>
<div>
<h3>How long will I have my spis15xx account?</h3>
<div>You will have it until the end of the SPIS program, but sometime after that, it will be disabled.</div>
<div><br>
</div>
<div><span style="font-size:10pt;background-color:transparent">So be sure that before SPIS ends, anything you want to save after SPIS ends is copied somewhere else. &nbsp;</span></div>
</div>
<div><span style="font-size:10pt;background-color:transparent"><br>
</span></div>
<div><span style="font-size:10pt;background-color:transparent">Note: your github repos will stay around for a while longer. They are likely to stick around &nbsp;for months, or even years after SPIS ends. &nbsp; &nbsp;Github.com hasn't made any guarantees for how long they will stick around, but they haven't expressed any need to get rid of them either. &nbsp; They will probably stay around as long as github.com is in business. &nbsp; &nbsp; &nbsp; So, anything you push into a github.com repo is probably still accessible to you after SPIS is over.</span></div>
<div><span style="font-size:10pt;background-color:transparent"><br>
</span></div>
<h3>What is Linux and Unix, and how does it related to my spis15xx account?</h3>
<div><br>
</div>
<div>The computers running in B230 and B240—as well as the one you access when use "ssh" to remotely access ieng6-240.ucsd,edu are running an operating system called Linux. &nbsp;(Examples of other operating systems, or OSs, include Windows, MacOS, iOS, and Android.)&nbsp;</div>
<div><br>
</div>
<div>Linux is a part of a family of operating systems collectively known as Unix-based OSs, or the Unix family of OSs.</div>
<div><br>
</div>
<h3>What is a terminal session/shell prompt/unix prompt/linux prompt?</h3>
<div><br>
</div>
<div>When using a Linux or Unix based system, we make a lot of use of the so-called "terminal session". &nbsp;The place where you type commands into a terminal session goes by various names.</div>
<div><br>
</div>
<div>
<ul><li>Shell prompt &nbsp;</li>
<ul><li>Confusing, the Python Read-Eval-Print Loop (REPL) is also sometimes called the Python Shell Prompt. &nbsp;But that's something else entirely.</li>
<li>By itself, "shell prompt" usually means the terminal session shell prompt.</li></ul>
<li>Linux prompt</li>
<li>Unix prompt</li>
<li>Command prompt</li></ul>
<h2>Tips for Using your ACMS Account</h2>
</div>
<h3>How to diagnose a disk quota problem</h3>
<div><span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px">If you suddenly are finding that multiple things that usually work on your ACMS account are not working, e.g. IDLE locks up, web browser locks up, can't open new windows, commands fail with strange error messages, etc., it may be a sign that you are over disk quota.</span></div>
<div><span style="color:rgb(34,34,34);font-family:arial,sans-serif;font-size:12.8000001907349px"><br>
</span></div>
<div><font color="#222222" face="arial, sans-serif"><span style="font-size:12.8000001907349px">You can see whether disk quota is the problem by typing <code>quota -vs</code> at the Unix prompt. &nbsp;That looks like this:</span></font></div>

<pre><span style="background-color:rgb(238,238,238)">[spis15t7@ieng6-240]:~:501$ quota -vs
Disk quotas for user spis15t7 (uid 4091): 
     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
acsnfs4:/vol/home/linux/ieng6
                  57328    196M    196M            3214    4000    4000        
[spis15t7@ieng6-240]:~:502$ </span></pre>
<div>
<br>
</div>
<div>
<ul><li><span style="font-size:10pt;background-color:transparent">The number </span><code style="font-size:10pt;background-color:transparent">196M</code><span style="font-size:10pt;background-color:transparent"> in the output above indicates that your quota and your limit in terms of how much disk space you are allowed to consume on your ACMS account is 196 MB (Megabytes). &nbsp;&nbsp;<br>
<br>
</span></li>
<li><span style="font-size:10pt;background-color:transparent">The number 57328 in the output above indicates that you are using 57328 blocks of your quota. &nbsp; &nbsp; That's fine (a block is usually either 0.5KB or 1KB, and there are 1024KB in a MB.) &nbsp;So this output indicates a "good" situation.</span></li></ul>
<div>Here's what you DON'T want to see:</div>
</div>
<div><br>
</div>
<div>
<pre style="font-size:13.3333330154419px"><span style="background-color:rgb(238,238,238)">[spis15t7@ieng6-240]:~:501$ quota -vs
Disk quotas for user spis15t7 (uid 4091): 
     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
acsnfs4:/vol/home/linux/ieng6
                  196M    196M    196M            3214    4000    4000        
[spis15t7@ieng6-240]:~:502$ </span></pre>
</div>
<div><br>
</div>
<div>That's an example of a problem. &nbsp;The usage and the quota are the same, meaning that you've used up all of your available disk quota. &nbsp; If you try to write to any additional file, you'll end up having trouble. &nbsp;&nbsp;</div>
<h3>Do you have a "disk space" problem, or a "number of files" problem?</h3>
<div>The number 3214 in the output above is the "number of files". &nbsp;In this example, it is below the quota of 4000, so all is well. &nbsp;BUT, if it were above the 4000, we'd have a "<b>too many files</b>" problem. &nbsp; Those are investigated in different ways. &nbsp;Read on!</div>
<h3>What is causing this?</h3>
<div>The thing is, it's unlikely that you filled up your disk with ordinary Python files. &nbsp;The problem is more likely some kind of bug either in the system software, or in one of your own programs, that is making REALLY big files somewhere unexpected. &nbsp;You need to f<i>ind where the problem is</i> before you can fix it.</div>
<h3>How to solve a disk quota problem</h3>
<div>TEMPORARY VERSION OF INSTRUCTIONS:
</div>
<div><br>
</div>
<div>TODO: Make these nicer.</div>
<div><br>
</div>
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
<div>Unlike "disk space", there isn't a nice handy utility built into unix to count the number of files you have. &nbsp;Fortunately, one of my colleagues at UC Santa Barbara, wrote such a utility, and has put it up on his public github repo here:&nbsp;<a href="https://github.com/rkip/countfiles">https://github.com/rkip/countfiles</a></div>
<div><br>
</div>
<div>I've put that in my own directory on ACMS for SPIS 15, so you can run it with this command:</div>
<div><br>
</div>
<div><code>~spis15t7/bin/countfiles</code></div>
<div><br>
</div>
<div>If you run that, it will show you which directory has lots of files under it. &nbsp;You can cd into that directory, and repeat the command. &nbsp;Eventually you may find something you can delete to reduce your file count below your quota.</div>
<div><br>
</div>
<h2>Accessing your ACMS account from your own Mac/PC/Linux machine</h2>
<div>There are (at least) two ways to access your ACMS&nbsp;</div>
<div>
<ul><li>ssh connections</li>
<li><a href="http://acms.ucsd.edu/info/vncgnome.html">vncgnome</a> connections</li>
<li>Secure file transfer with scp (<b>s</b>ecure <b>c</b>o<b>p</b>y) or sftp (<b>s</b>ecure <b>f</b>ile <b>t</b>ransfer <b>p</b>rotocol)</li></ul>
<h3>Using ssh on Mac on Linux (for terminal commands only—for graphics, see below)</h3>
</div>
<div>From Mac or Linux, using ssh is easy, because it is likely already installed. &nbsp;Just go to a terminal prompt and type:</div>
<div><br>
</div>
<div></div>
<div class="sites-codeblock sites-codesnippet-block">

<div><code>ssh spis15xx@ieng6-240.ucsd.edu</code></div>

</div>
<div><br>
</div>
<div>This should bring up a terminal session on your SPIS ACMS account. &nbsp;This is fine as long as everything you are doing is at the command line. &nbsp;</div>
<div><br>
</div>
<div>
Use exit or logout when you are finished with your session:</div>
<div><br>
</div>
<div>
<div class="sites-codeblock sites-codesnippet-block">

<pre>[spis15t7@ieng6-240]:~:501$ <code>exit</code>
logout
Connection to ieng6-240.ucsd.edu closed.
Phills-MacBook-Pro: pconrad$ 
</pre>
</div>
</div>
<div><br>
</div>
<h3>Using ssh on Windows (terminal commands only—for graphics, see below)</h3>
<div>On Windows, you need a Secure Shell Client. &nbsp;One example of such a program is PuTTY. &nbsp;PuTTY has the advantage of being free, widely used.</div>
<div><br>
</div>
<div><a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html" style="font-size:10pt;background-color:transparent">http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html</a></div>
<div><br>
</div>
<div>
<div>When you try to connect, you'll see the following dialog box:</div>
<div><br>
</div>
<div>
<div style="font-size:13.3333330154419px">
<ul><li><span style="font-size:10pt;background-color:transparent">For the <b>Host Name (or IP address) field,</b> enter ieng6-240.ucsd.edu</span></li>
<li><span style="font-size:10pt;background-color:transparent">If you want to "save the session", you can enter a name such as "ACMS" in the "Saved Sessions" box and click save.</span></li>
<li>Click and "saved session" and click "Load" to connect then "Open" to connect.</li>
<li><span style="font-size:10pt;background-color:transparent">When prompted for the username, enter spis15xx (put in your letters instead of xx)</span></li></ul>
</div>
</div>
<div><br>
</div>
<div>
<div style="display:block;text-align:left"><a href="https://sites.cs.ucsb.edu/~pconrad/topics/CSILviaPutty/images/Picture%2018.png" imageanchor="1"><img border="0" src="https://sites.cs.ucsb.edu/~pconrad/topics/CSILviaPutty/images/Picture%2018.png"></a></div>
</div>
</div>
<div style="display:block;text-align:left"><br>
</div>
<div style="display:block;text-align:left"><br>
</div>
<h3 style="display:block;text-align:left">Using ssh with graphics—The no $DISPLAY environment variable problem</h3>
<div style="display:block;text-align:left"><br>
</div>
<div>If you try to access programs that brings up windows or graphics (such as idle), though, there will be a problem. &nbsp;You'll get a message like this one:</div>
<div><br>
</div>
<div>
<div class="sites-codeblock sites-codesnippet-block">
<pre>[spis15t7@ieng6-240]:~:501$ <code>idle</code>
Traceback (most recent call last):
  File "/software/common/python-2.7.10/bin/idle", line 5, in &lt;module&gt;
    main()
  File "/software/common/python-2.7.10/lib/python2.7/idlelib/PyShell.py", line 1542, in main
    root = Tk(className="Idle")
  File "/software/common/python-2.7.10/lib/python2.7/lib-tk/Tkinter.py", line 1814, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
[spis15t7@ieng6-240]:~:501$ 
</pre>
</div>
</div>
<div><br>
</div>
<div><br>
</div>
<h4>ssh with graphics on Linux</h4>
<div><br>
</div>
<div>On Linux, you can probably fix this by simply including the -X flag when you use SSH (you'll have to exit and login again):</div>
<div><br>
</div>
<div>
<div style="font-size:13.3333330154419px">&nbsp;type:</div>
<div style="font-size:13.3333330154419px"><br>
</div>
<div style="font-size:13.3333330154419px"></div>
<div class="sites-codeblock sites-codesnippet-block" style="font-size:13.3333330154419px"><code>ssh -X spis15xx@ieng6-240.ucsd.edu</code></div>
<div style="font-size:13.3333330154419px"><br>
</div>
<div style="font-size:13.3333330154419px">Then graphics programs should work.</div>
<div style="font-size:13.3333330154419px"><br>
</div>
<h3 style="font-size:13.3333330154419px">ssh with graphics on Mac</h3>
</div>
<div>On Mac, you'll need to install an X11 server on your Mac, such as XQuartz, (free download, here):&nbsp;<a href="http://xquartz.macosforge.org/landing/">http://xquartz.macosforge.org/landing/</a></div>
<div>Then, the Linux solution above should work for you.</div>
<div><br>
</div>
<h4>ssh with graphics on Windows</h4>
<div><br>
</div>
<div>For Windows, you'll need an X11 server on your Windows machine, such as XMing.</div>
<div><br>
</div>
<div>Installing and Configuring it to run with PuTTY is a bit technical. &nbsp;Here is one explanation:</div>
<div><br>
</div>
<div><a href="https://wiki.utdallas.edu/wiki/display/FAQ/X11+Forwarding+using+Xming+and+PuTTY">https://wiki.utdallas.edu/wiki/display/FAQ/X11+Forwarding+using+Xming+and+PuTTY</a></div>
<div><br>
</div>
<div><br>
</div>
<h2>
Some Unix Commands</h2>
<div>Note: that "directory" is the Unix word for what is more commonly called a "folder" these days on systems such as Windows and Mac OS.<br>
<br>
Stuff in <i>italics</i> is not literally part of the command—it's standing in for an example of what might go there.<br>
<br>
</div>
<div>
<table border="1" bordercolor="#888" cellspacing="0" style="border-collapse:collapse;border-color:rgb(136,136,136);border-width:1px">
<tbody>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;ls</td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;<b>l</b>i<b>s</b>t files</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;ls -al</td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;"<b>l</b>ong" list of "<b>a</b>ll" files, including hidden files&nbsp;</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:23.6666666269302px">&nbsp;pwd</td>
<td style="width:367.66666662693px;height:23.6666666269302px">&nbsp;<b>p</b>rint <b>w</b>orking <b>d</b>irectory (what directory am I in?)</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:44.6666666269302px">&nbsp;cd <i>someDir</i></td>
<td style="width:367.66666662693px;height:44.6666666269302px">&nbsp;change working directory into someDir<br>
(assumes someDir is name of a directory/folder inside my current working directory)</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;cd</td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;change working directory to my home directory</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;cat <i>filename</i></td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;list contents of file with name <i>filename &nbsp;<br>
(con<b>cat</b>ates file to standard output)</i></td>
</tr>
<tr>
<td style="width:233.66666662693px;height:29.6666666269302px">&nbsp;more <i>filename</i></td>
<td style="width:367.66666662693px;height:29.6666666269302px">&nbsp;list contents of file, but allow me to see one screen at a time, pressing enter or space bar to see "<b>more</b>".</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;rm <i>filename</i></td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;<b>r</b>e<b>m</b>ove (delete) filename</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:29.6666666269302px">&nbsp;mv <i>oldname</i> <i>newname</i></td>
<td style="width:367.66666662693px;height:29.6666666269302px">&nbsp;rename file from oldname to newname (in the current directory) &nbsp;(mv stands for <b>m</b>o<b>v</b>e, but also is the rename command in Linux)</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;mv filename ..</td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;mv (<b>m</b>o<b>v</b>e) file from current directory to one directory "up" (..)</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;mv filename dirname</td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;mv (<b>m</b>o<b>v</b>e) file down into dirname (assumes dirname names a directory under the current working directory)</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;cp filename1 filename2</td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;<b>c</b>o<b>p</b>y filename1 to a new file called filename2</td>
</tr>
<tr>
<td style="width:233.66666662693px;height:13.6666666269302px">&nbsp;cat &gt; filename<br>
&nbsp;<i>line of input<br>
&nbsp;more input<br>
&nbsp;...<br>
&nbsp;CTRL/D to end</i></td>
<td style="width:367.66666662693px;height:13.6666666269302px">&nbsp;create a new file called <i>filename<br>
&nbsp;</i>(con<b>cat</b>enate standard input into file)</td>
</tr>
<tr>
<td>&nbsp;quota -vs</td>
<td>&nbsp;show current file quota</td>
</tr>
<tr>
<td>&nbsp;du -sh *</td>
<td>&nbsp;show <b>s</b>ummary of current <b>d</b>isk <b>u</b>sage (in <b>h</b>uman readable units)&nbsp;for each file/folder in current directory (not including hidden files)</td>
</tr>
<tr>
<td>&nbsp;du -sh .[A-z]*</td>
<td>&nbsp;<span style="font-size:13.3333330154419px">&nbsp;show&nbsp;</span><b style="font-size:13.3333330154419px">s</b><span style="font-size:13.3333330154419px">ummary of current&nbsp;</span><b style="font-size:13.3333330154419px">d</b><span style="font-size:13.3333330154419px">isk&nbsp;</span><b style="font-size:13.3333330154419px">u</b><span style="font-size:13.3333330154419px">sage (in&nbsp;</span><b style="font-size:13.3333330154419px">h</b><span style="font-size:13.3333330154419px">uman readable units)&nbsp;</span><span style="font-size:13.3333330154419px">&nbsp;for each file/folder in current directory for hidden files that start with any character between capital A and lowercase z.)</span></td>
</tr>
</tbody>
</table>
<br>
</div>
<div>Links to learn more Unix commands</div>
<div><br>
</div>
<div>
<ul><li><span style="font-size:10pt;background-color:transparent">Job Control <a href="https://acms.ucsd.edu/info/jobctrl.html">https://acms.ucsd.edu/info/jobctrl.html</a></span></li>
<li>List of useful commands (links to other tutorials):<br>
<a href="http://www.tutorialspoint.com/unix/unix-useful-commands.htm">http://www.tutorialspoint.com/unix/unix-useful-commands.htm</a></li></ul>
</div>
<div><br>
</div>
