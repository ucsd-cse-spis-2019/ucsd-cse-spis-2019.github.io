---
topic: "MacOS: Python and git setup "
desc: "Getting your Mac OS laptop setup to do Python and git"
---

This article describes setting up your Mac OS laptop for SPIS.

* For Windows, visit: [Windows: Python and git setup](/topics/windows_setup/).  
* For Linux, visit [Linux: Python and git setup](/topics/linux_setup/).

# Setting up your Mac OS Computer

You don't really need a laptop to participate in SPIS.  Most of the work for SPIS will be done on the ACMS machines in B230.

But if you have a Mac OS laptop, it may come in handy.  This article describes how to set things up to make
it more convenient to use that laptop to do the things are are doing in SPIS.



# Using the ACMS computers

You can use these machines:
* directly by physically coming to B230 and logging in, in which case you aren't using your laptop at all.
* over the network via either an ssh or VNC connection.

## Using ACMS over ssh

To use ACMS computers over ssh, you can just bring up the Terminal application on your Mac, and type the following
at the command prompt.  This assumes that your spis username is `spis16xy`.  Put your own username in instead:

```
ssh spis16xy@ieng6-240.ucsd.edu
```

However, this method will NOT work for bringing up graphics programs such as `idle`.  You will ONLY have access to command line programs (including the command line Python prompt `python`).

If you want to access IDLE, you'll need to take an additional one time step of installing XQuartz.  XQuartz provides access to the `X11 Windowing System`, which enables programs running on remote systems (e.g. the ACMS Linux systems) to get access to the screen, mouse and keyboard of another system (e.g. your Mac.)

You can install XQuartz by visiting this link: [https://www.xquartz.org/](https://www.xquartz.org/)

(If that installer tells you that *a reboot is required*, they aren't kidding.  It's pretty unusual for Mac OS software to require that, but in this case, it if they say it, its likely to be true.)

Once you've installed XQuartz, and rebooted if necessary, you should be able to use these commands to access the ACMS systems with access to idle and other graphical tools:

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


# Installing Python

The version of Python you want is the "latest Python 2 release" on this screen:

https://www.python.org/downloads/mac-osx/

* Use the `Mac OS X 64-bit/32-bit installer` if you have Mac OS X 10.6 and later
* Use the `Mac OS X 32-bit installer` *only* if you have Mac OS X 10.5
* If you have Mac OS X 10.4 or earlier, you'll need to upgrade your Mac OS X install to a later version.


## Getting pip to actually work at the command prompt

Python typically works immediately for Mac OS users after doing the install above. If that's not the case. 

But pip sometimes doesn't. 

To get pip, you can try  `sudo easy_install pip`.

Try closing all open terminals, then opening one again, and seeing if `pip` works now.

If that works, great.  If not, here's a slightly more involved way that does seem to work:

1.  Navigate to [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) and save that file to `get-pip.py` somewhere on your computer; perhaps your home direcory or `~/Desktop`.
2.  At command line, navigate to the folder where you saved `get-pip.py`.  Run the command `python get-pip.py`
3.  Close your terminal, open it again and try the pip command again.
 
If that still doesn't work, you may need to either:

1.   Ask a mentor or instructor for help
2.   Search the web for a solution

# Getting git for Mac

Most version of Mac OS come with git preinstalled, so you won't have to do anything.

But if you don't have git on your system for some reason, you can install it from here:

[https://git-scm.com/download/mac](https://git-scm.com/download/mac)

Download and install.  We recommend taking all of the defaults for the various options you are presented with (i.e. just keep pressing enter).

If you have any command line windows open, close and reopen them before trying git commands.

# Setting up the git options and ssh key on your Windows machine

The steps for setting up an ssh key for your Mac  are pretty much the same as the git steps we did
for our ACMS account, documented here: [ACMS: Github one time setup](topics/acms_git_one_time_setup/), with the difference
being that:

* You type all of the commands, including the `ssh-keygen` command in a Mac terminal session, NOT on ACMS.
* When you save the contents of the `id_rsa.pub` you generate on your laptop, it will be an *additional* key that
    you add to your github.com account.  For the name of the key, use "My Mac" or something like that.

If you use your github.com account from multiple computers and/or ACMS accounts, you'll need to add an ssh key
for each one.



