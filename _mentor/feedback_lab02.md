---
topic: "Feedback lab02 -- TODO"
desc: "Feedback on lab02"
---

# Feedback on lab02

Here's what to look for when giving feedback on lab02 (a pair lab.)

## Does the repo they created have the correct name?

They should have created a repo with the name listed in this spreadsheet (private to mentors only):

Use the tabs at the bottom of the sheets to select "lab02 repos"

<https://docs.google.com/spreadsheets/d/1YPx3YtYVFCgCFAZU7wqZBAS7n2UUHhbc2J8odHyoQZk/edit?usp=sharing>

If the name is not correct, you won't be able to find it by clicking on the link.

Instead, go to the organization page: <https://github.com/ucsd-cse-spis-2017>, type "lab02" in the search box,
and look through to see if you can find the repo. 

## Does the repo contain the right files?

The files should be:

* `.gitignore`	
* `README.md`	
* `tempFuncs.py`	
* `test_tempFuncs.py`

If they dont have the right files, or the file names are wrong, provide some feedback on that.

##  tempFuncs.py: two function definitions

Check that tempFuncs.py has function definitions for both `ftoc` and `ctof`

These are pretty straightforward, so there probably isn't much you can say, unless you see something that jumps out at you.

## test_tempFuncs.py

They were supposed to add four tests for ctof that were NOT in the starter code so that there are nine tests in all.  

Check whether they did.

One common error is to have the same name repeated.  You may want to try cloning the repo and running the tests yourself.

It is not necessary to fire up IDLE to do so.   The easiest way is just to type this at the unix shell prompt:

```
python test_tempFuncs.py
```

Ideally, you should see that it ran nine tests and they all passed:

```
$ python test_tempFuncs.py 
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
$
```

