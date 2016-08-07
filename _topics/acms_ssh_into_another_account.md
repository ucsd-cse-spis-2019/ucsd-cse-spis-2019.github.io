---
topic: ACMS: ssh'ing into another account
desc: "A is logged in, but B needs to get into their account for just a moment..."
---

Suppose your pair partner (or anyone else that you trust) is logged into a computer in the B230/B240 labs.   You need
 to do something in yourown ACMS account for just a moment.

But asking your pair partner to log all the way out is *really* inconvenient.   They will lose their place in all the work they have open.  And, it takes a long time to go through the whole logout/login process.

There is an easier and quicker way, as long as you trust one another.

Here's what to do:

* Ask your pair partner/friend that is logged in to open a new terminal window, and pass you the keyboard.
* In this new terminal window,  type this (where `spis16xy` is replaced by your own ACMS SPIS username.)

`ssh spis16xy@localhost`

The terminal session below shows an example of what that might look like.   But first, a few notes about this output:

*    Note that the `RSA key fingerprint...` notice is normal the
     first time you use the `ssh` command from any particular acccount to any particular machine.   
    *    Typically,
         you just type the word `yes`, and you'll never see that message again.    
    *    The only time you would *not* do that is
         if you have some particular reason to beleive you are being malicously attacked by evildoers that are spoofing IP addresses.   This is pretty rare.)
*   You'll be asked for your password.  It might not echo on the screen as you type it, but it is going in.
*   Once you are successful in logging in, there may be a long series of announcements.  In the middle, you might
    see the message:
    ```
    --More--(99%)[Press space to continue, 'q' to quit.]
    ```
   Just press space or `q`, and after a bit more yada, yada, yada, you'll get your prompt.


```
[spis16t3@ieng6-240]:~:79$ ssh spis16t4@localhost
The authenticity of host 'localhost (127.0.0.1)' can't be established.
RSA key fingerprint is 2c:07:da:be:44:8d:67:70:7f:4b:5e:51:88:d0:18:ce.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'localhost' (RSA) to the list of known hosts.
spis16t3@localhost's password: 
Last login: Sun Aug  7 13:27:29 2016 from cpe-76-88-3-252.san.res.rr.com
============================ NOTICE =================================
Authorized use of this system is limited to password-authenticated
...

Sun Aug 07, 2016  1:27pm - Prepping spis16
[spis16t4@ieng6-240]:~:79$ 
```

You can see that the prompt has changed from `spis16t3` to `spis16t4`.

When you are finished, type `exit` to leave the `spis16t4` session and return to the `spis16t3` session.


