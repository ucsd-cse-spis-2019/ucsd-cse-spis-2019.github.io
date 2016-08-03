---
topic: "Github: Introduction"
desc: "What is git? What is github?"
---

# What is git?

Git is a version control system that allows you to keep a historical
record of all the changes you make to your code and have access to
your programs on any computer.

Git works with containers called *repositories*, or *repos* for short.

# What is github.com?


A git repository can be local, on your file system, or it can be
remote on a server somewhere on the Internet. 


The github.com company is a commercial enterprise that runs a website
called github.com. Github.com provides a service for hosting github
repositories "in the cloud". The github.com company hosts open source
projects for free (via free public repositories) and makes money by
charging uses for hosting closed source projects in private
repositories.

# What does "in the cloud" mean?

We say that something is "in the cloud" if we are being given access
to an internet service in such a way that we *don't need to know the
details* of exactly how that service is being provided to us.

In the cloud means that "someone else" is worrying about all the
system management issues like keeping that server up and running,
keeping it free of malware and defending from Denial of Service
attacks, managing backups, etc.

# What is "version control"?

The software package "git" is an example of a "version control
system". (Others include SVN, Mercurial, and in a previous
generations, CVS, RCS, and SCCS).

A git repo (short for repository) is nothing more than a collection of
files and directories (folders), along with a special subdirectory
called .git (stored only once in the top level directory of the repo)
that keeps track of the complete history of the files and directories
contained in the repo. 

To some extent, the ".git" directory stays out
of your way, and you use the files and directories in the repository
exactly the same way you'd use files and directories in a regular
directory.

On the other hand, keeping files in a git repository has many advantages over just keeping files in an ordinary directory (e.g. a hard drive, or USB stick):

-  it is easier to collaborate with others on a project (whether that's an open source or closed source project)
-  it is easier to recover from screwups (like deleting important files, messing up code that was previously working, complete failure of your hard drive)
-  it is easier to share "works in progress" with TAs and instructors and fellow students to get help during lab, office hours, or by email
-  it is easier to share "open source" projects with others on the internet.

