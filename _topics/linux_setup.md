---
topic: "Linux: Python and git setup "
desc: "Getting your personal linux environment setup to do Python and git"
---


This article describes setting up your Linux laptop for SPIS.

* For Mac OS, visit: [Mac OS: Python and git setup](/topics/mac_setup/).  
* For Windows, visit [Windows: Python and git setup](/topics/windows_setup/).


# Setting up your own Linux laptop computer

You don't really need a laptop to participate in SPIS.  Most of the work for SPIS will be done on the ACMS machines in B230.

But if you have your own linux laptop, it may come in handy.  This article describes how to set things up to make
it more convenient to use that laptop to do the things are are doing in SPIS.

# Using the ACMS computers

You can use these machines:
* directly by physically coming to B230 and logging in, in which case you aren't using your laptop at all.
* over the network via either an ssh or VNC connection.

## Using ACMS over ssh

To use ACMS computers over ssh, you can just bring up a command line on your machine and type the following
at the command prompt.  This assumes that your spis username is `spis16xy`.  Put your own username in instead:

```
ssh spis16xy@ieng6-240.ucsd.edu
```

However, this method will NOT work for bringing up graphics programs such as `idle`.  You will ONLY have access to command line programs (including the command line Python prompt `python`).

For that, you'll need to enable X11 forwarding with the -X or -Y flags:

```
ssh -X spis16xy@ieng6-240.ucsd.edu
```

OR 

```
ssh -Y spis16xy@ieng6-240.ucsd.edu
```

Use the `-X` version if it works for you.  If it gives you problems, sometimes the -Y version works better.
* Don't ask why&mdash;I don't know.

Also: you may get a warning: 

```
Warning: No xauth data; using fake authentication data for X11 forwarding.
```

It's always a little dicey to ignore messages like this one.  But it turns out that *most everyone does ignore this one*.
Getting things configured to make it go away turns out to be very tricky, and system dependent.  And probably not worth it.


# Installing Python, pip, git

For installing software on on a Linux machine, you should follow whatever guidelines apply to your own distribution of Linux, be that Fedora, Ubuntu, CentOS, Debian, etc.

Therefore, for Linux, we are only going to tell you "what" to install, and leave the details of "how" to you.  As you probaby already know, when you chose Linux as your OS (in contradistiction to Windows or Mac OS), you took on the job of being your own tech support. 

* The version of Python you want is the "latest Python 2 release" available for your distribution of Linux.
* You also need to make sure you have pip, which may be a separate install.
* git is probably already installed, but if not, install that too.
   
