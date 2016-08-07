---
topic: "ACMS Account: github one-time setup steps"
desc: "ssh-key generation, configure user.name, etc. "
---

# One time configuration commands

You will need to type the following commands just once for each separate ACMS account you have.

You may also need to do these commands on your own Mac, Windows or Linux box if you use command line git there.   They configure some
options in a file, on a Linux account such as your ACMS account, is called `~/.gitconfig`.  It may have other names and locations on Mac or Windows.

Type in these commands, but change the name `Alex Triton` to your own real world first and last name.  If you prefer, for privacy reasons,
you may use your first name and last initial.     Also, change the email address `atriton@ucsd.edu` to your own `@ucsd.edu` email address.

```
git config --global user.name "Alex Triton"
git config --global user.email "atriton@ucsd.edu"
```
