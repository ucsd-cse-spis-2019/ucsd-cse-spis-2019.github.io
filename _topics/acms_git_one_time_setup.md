---
topic: "ACMS Account: github one-time setup steps"
desc: "ssh-key generation, configure user.name, etc. "
---

# Using git from your ACMS account: one-time setup steps

There are two things you need to do to make your ACMS account work smoothly with git.  

* Setting your global `user.name` and `user.email` values
* Creating an ssh public/private key pair for your ACMS account
* Uploading the public key for your ACMS account to your github.com account.

Instructions for each of these steps appear below.

# Setting your global `user.name` and `user.email` values

You will need to type the following commands just once for each separate ACMS account you have.

You may also need to do these commands on your own Mac, Windows or Linux box if you use command line git there.   They configure some
options in a file, on a Linux account such as your ACMS account, is called `~/.gitconfig`.  It may have other names and locations on Mac or Windows.

Type in these commands, but change the name `Alex Triton` to your own real world first and last name.  If you prefer, for privacy reasons,
you may use your first name and last initial.     Also, change the email address `atriton@ucsd.edu` to your own `@ucsd.edu` email address.

```
git config --global user.name "Alex Triton"
git config --global user.email "atriton@ucsd.edu"
```

# Creating an ssh public/private key pair for your ACMS account

# 3. Creating an ssh public/private key pair

In this step, we will set up a public/private key pair on your CSIL account. 

The idea of a public/private key pair is that you give away your public key, and you keep your private key a secret. 
This allows anyone with your public key to know that you are you without you having to type in a password 
(as long as your private key stays secret).

To generate a public/private key pair: Open a terminal session, and type the `ssh-keygen` command.

You will be asked a series of questions. For each question, just press the enter/return key (to accept the default option.)

That will look like this:
```
bash-4.3 $ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/cs/student/jgaucho/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /cs/student/jgaucho/.ssh/id_rsa.
Your public key has been saved in /cs/student/jgaucho/.ssh/id_rsa.pub.
The key fingerprint is:
de:8f:c0:d8:69:bc:82:e9:06:e9:30:25:42:16:bc:1c spis15t7@ieng6-240
The key's randomart image is:
+--[ RSA 2048]----+
|...              |
| E               |
|+ o              |
|oo.              |
|.o .    S        |
|o o    * o       |
| + . o. O .      |
|  . + .. o o     |
|   o.  .. . .    |
+-----------------+
bash-4.3 $
```


The effect of that is to create two files in a hidden directory of your account called `.ssh` 

If you type `cd` to go to your home directory, and `ls` at your terminal prompt, you will not see this directory. Example:

But if you use `ls -a` you WILL see the `.ssh` directory along with many other hidden directories.

Next, type the command `cd ~/.ssh` at the Terminal prompt.   Then use `ls` to list your files.

You should see two files `id_rsa` and `id_rsa.pub` as follows. (If you see other files, don't worry)

```
bash-4.3 $ cd ~/.ssh
bash-4.3 $ ls
id_rsa  id_rsa.pub
bash-4.3 $  
```

You want to now look at the contents of `id_rsa.pub`.  This file is your public key. 
That is the one you are going to share with `github.com`. (The contents of `id_rsa` are your private key, which you do NOT share. )

To see the contents of `id_rsa.pub`, we use the cat command:

```
bash-4.3 $ cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA1yTFW/PkiZCebbR9EqkduGCApKwW7uy7CZ1ThomgG+xZs
VgWWIMirzkNJbahxwwEVIH0Hj+irID3ICkH8o60T3QiMk1v5VJSVFaKdqtiZXFQapYR2Rwln1wf2XXBCT/cdVW
if9usiS5vLqtno74/dpKCEiELjGSHdpFTyFoF3ZHR6plFYA2/iX4XWDrDJwG/Qwf+SBd0uzIy7CpFrQK+9kMWDr
K2jUGhd0goYPQu2LCgHxnu8R041M5ooSUE79seE+64gVcjoSfPJwdKhZdwy2zjYvKKz0CM4w3ysPbOpr1FkT
6MnlhN3dyJBFA+BjmtXGVDNl7a5yjtY9QzORILfQ== jgaucho@csil.cs.ucsb.edu
bash-4.3 $ 
```


Your public key will look different, but similar. You are now going to to do a "copy/paste" of that key into a page of github.com. 
Our next step is to navigate to the correct page of github.com to enter that key.




# Uploading the public key for your ACMS account to your github.com account.



To upload your ssh public key to github.com, start by opening a web browser to github.com.  

If you are not yet logged in, login to your github.com account.   

Go to the github.com settings menu.  It's on a pull down menu at the upper right hand corner of the page.

Once you are at the settings menu, choose  the SSH keys option. It's in the middle on the left.  

Then, click "Add SSH key".

Next, "copy" your SSH public key from your terminal window so that we can paste it into the github.com web browser window. Be careful to get the whole key, but nothing more than the key. Don't include the shell prompts or the cat command.

Paste it into the window on the github.com website that asks for the key.

Github may ask for your password to confirm this operation.

Then you should get a message that your key was added.

Congratulations! You've now added the public key associated with your ECI/CSIL account to github.com.

In the future, if you have a different CSIL account, you'll need to do this step again.

Optional: You may also want to repeat this step for the public key associated with your own personal laptop or desktop computer.

You'll have to generate a separate public/private ssh key pair for each computer that you use with github.com

On Mac and Linux, the ssh-keygen command should work.

The ssh-keygen command is also available in the "git shell" that comes with the Windows version of git.

