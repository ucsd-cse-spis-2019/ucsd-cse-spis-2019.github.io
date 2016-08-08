---
topic: "Gradescope: autograder"
desc: "Creating autograded assignments"
---

# Gradescope's autograder

The website [gradescope.com](https://gradescope.com) provides the capability
to set up autograded assignments.

We have two courses set up in Gradescope for SPIS 2016:

* The ["real" SPIS 2016 Gradescope course](https://gradescope.com/courses/3559)
* A [SPIS-Autograder-Development test course](https://gradescope.com/courses/3670) for testing out new autograded assignments before they are released to students.


The private repo
<https://github.com/ucsd-cse-spis-2016/PRIVATE-autograder-try01>
contains an example of an autograded assignment.  This assignment is
likely *not* one that is suitable for SPIS&mdash;rather this assignment
is one that is set up using the exact example provided by Gradescope's
own documentation.   The "value added" is this:

* There is a makefile that when you type `make`, produces the file
    `autograder.zip` in the format needed by Gradescope.

* It is packaged in its own github repo, one that contains ONLY the
    Python code needed for a single assignment.  (Gradescope's own
    example contains Java examples also, and lots of other clutter.)

# To create your own assignment:

The [README.md
file](https://github.com/ucsd-cse-spis-2016/PRIVATE-autograder-try01/blob/master/README.md)
in the
[PRIVATE-autograder-try01](https://github.com/ucsd-cse-spis-2016/PRIVATE-autograder-try01)
repo contains a description of the contents of the repo, and some
advice on adapting it for your own assignment.

To get started:

1.  Create a new private repo called, for example,
    `PRIVATE-autograder-lab02` under the `ucsd-cse-spis-2016`
    organization

2.  Copy the Makefile from
    [PRIVATE-autograder-try01](https://github.com/ucsd-cse-spis-2016/PRIVATE-autograder-try01)
    into your repo.
    
3.  Create a subdirectory in that repo called `autograder`, and under
    that subdirectory, create one additional subdirectory called `tests`

4.  Into the `autograder` subdirectory, copy these files, with *exactly*
    these names:

    * `run_autograder`
    * `run_tests.py`
    * `setup.sh`

5.  Edit the `run_autograder` file.  In it, the name of the file you 
    expect the students to submit in their assignment, e.g. 
    `calculator.py` needs to be changed to what you expect the students
    to submit, e.g.
    `tempFuncs.py`, or `lab05.py`, or whatever.

    Fortunately, `run_tests.py` and `setup.sh` are pretty standard.
    Unless you need to `pip install ...` extra Python modules, 
    you can probably leave them alone.

6.  Into the tests subdirectory, add your tests.

    I suggest copying one of the test files from the example repo
    and then modifying it to fit your assignment.

    You might need an empty __init__.py as well,
    as this is present in the example.
    
7.  Use `make` in the top level to generate an `autograder.zip` file,
    and use that to create the assignment on Gradescope.
  
    It is good practice to have a separate "Test Course" in which to try
    the assignment first before uploading it to your real course,
    since Gradescope does not allow you to delete assignments once there
    is even a single submission, even if that submission is  a test 
    submission from an
    instructor.   


8.  optional, but helpful: add these lines to the .gitignore file in the main directory of the repo

    ```
    # for gradescope autograder
    autograder.zip

    # for emacs
    *~
    \#*\#

    # for mac os
    .DS_Store
    ```






# Once you have set up the repo

Once you have set up the repo, you can run `make clean; make` to generate
the autograder.zip file.  What do you do with this?  The text and images below
explain the process.

* The ["real" SPIS 2016 Gradescope course](https://gradescope.com/courses/3559)
* A [SPIS-Autograder-Development test course](https://gradescope.com/courses/3670) for testing out new autograded assignments before they are released to students.


First, navigate to either:
* the [SPIS 2016 autograder practice course](https://gradescope.com/courses/3670), OR
* the real [SPIS 2016 course](https://gradescope.com/courses/3670) page on Gradescope.  

(I strongly  recommend trying new assigments in the practice course first.)

Then, click the "Create Programming Assignment" button as shown in the image below.

It is near the bottom of the instructor UI, and is NOT the same as the regular
"Create Assignment" button (at least as of this writing, August 2016.  Note that
as a web app, Gradscope's UI is subject to change at any time.)

![Click create programming assignment](gradescope-click-create-programming-assignment-50.png)


----

<div style="display:none;" data-note="This element provides link to generated page from github.com web interface">
Generated page: https://ucsd-cse-spis-2016.github.io/instructors/gradescope-autograder
</div>
