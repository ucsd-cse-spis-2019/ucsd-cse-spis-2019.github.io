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

To use ACMS computers over ssh, the best solution we have found is called [Mobaxterm](http://mobaxterm.mobatek.net/).

The "MobaXterm Home Edition (Installer edition)" is free and is the best choice (as of this writing, August 2016).

To use it: 
* Install it
* Open up a new "session", and choose "ssh"
* Fill in the host with `ieng6-240.ucsd.edu`, click the "enter username" box, and enter your `spis16xy` username (yours won't be `xy`, necessarily.  It will be whatever username you were assigned.
* Enter your password when prompted.

# Installing Python

The version of Python you want is the "latest Python 2 release" on this screen:

https://www.python.org/downloads/windows/

If you know you have a 64-bit machine and a 64-bit version of windows, choose the `Windows x86-64 MSI installer`.

Otherwise, choose the  `Windows x86 MSI installer`

## Getting Python to actually work at the command prompt

To get Python and the pip command to work at the command prompt, you may have to do one extra step.

To see whether you need to do this step, bring up a Windows command prompt, and type `python`

If you get the Python shell, just type `quit()`.     If you don't, then you'll need to do the step below to
add `C:\Python27\` to your `path` environment variable.    And while we are at it, we'll add `C:\Python27\Scripts`, since
we'll need that eventually as well.

(This is assuming that Python has been installed to `C:\Python27`; check that first.  If Python isn't on your computer at all, try installing it again.  If it is in another
place, use that instead of `C:\Python27 in the instructions below.)

Also, try typing `path` at the Windows command prompt.   You'll get back output with some long thing that looks like this (the exact value will vary from system to system, and it is often considerably longer)

```
%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\
```

What you want is to make a change so that `C:\Python27\` shows up at the end of this as well.

The way you add The way it looks is slightly different on each different version of Windows.  But typically, it invovles the following steps:

* Start the System Control Panel applet (Start - Settings - Control Panel - System).
* Select the Advanced tab.
* Click the Environment Variables button.
* Under System Variables, select Path, then click Edit.

There will be some way to add additional things into this so-called `path`.     You want to add two new things:

* `C:\Python27\`
* `C:\Python27\Scripts`

Be sure that after you add these, that you click "OK", or "Save", or whatever to back your way out of the various windows and dialogs and buttons you used to get to where you added the new values.  If you use "cancel" or "click the red x", it might not save your changes, and you'll just have to do it all over again.

To see whether it worked, *close and then reopen* any Windows Command Line windows you have open, and then type `path` again. See whether these two new directories appear at the end of the path:

```
%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Python27\;C:\Python27\Scripts\
```

If so, then try the `python` and `pip` commands again and see if they work.

Note that on Windows, instead of `pip install --user blah` you'll probably just use `pip install blah`

Try it with `pip install flask` to see if it works.

## What if Python works, but pip doesn't?

If the Python command works, but the pip command does not, then try this:

1.  Navigate to [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) and save that file to `get-pip.py` somewhere on your computer; perhaps your Windows home folder.
2.  In a Windows command line shell, navigate to the folder where you saved `get-pip.py`.  Run the command `python get-pip.py`
3.  Try the `pip` command again at the Windows Command Prompt.

If that still doesn't work, you may need to either:

1.   Ask a mentor or instructor for help
2.   Search the web for a solution

# Getting git for windows

To get git for Windows, visit:

[https://git-scm.com/download/win](https://git-scm.com/download/win)

Download and install.  We recommend taking all of the defaults for the various options you are presented with (i.e. just keep pressing enter).

If you have any command line windows open, close and reopen them before trying git commands.

# Setting up the git options and ssh key on your Windows machine

The steps for setting up an ssh key for your Windows machine are pretty much the same as the git steps we did
for our ACMS account, documented here: [ACMS: Github one time setup](topics/acms_git_one_time_setup/), with the difference
being that:

* You type all of the commands, including the `ssh-keygen` command in the *git bash shell* that was installed
    when you installed "Git for Windows", not in a terminal session on ACMS.
* When you save the contents of the `id_rsa.pub` you generate on your laptop, it will be an *additional* key that
    you add to your github.com account.  For the name of the key, use "My Windows Laptop" or something like that.

If you use your github.com account from multiple computers and/or ACMS accounts, you'll need to add an ssh key
for each one.



