---
layout: lab
num: lab05
ready: false
desc: "lab05 covering Guttag Ch5, by Diba"
assigned: 2016-08-10 09:30:00.00-7
due: 2016-08-12 15:45:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza

# Learning Goals
In this lab you will practice the use of lists and other mutable data structures following Chapter 5 of Guttag. We will also review concepts from Chapter 4 of Guttag: recursion, interacting with text files and media files (pictures). 
Note that while media files are not covered in Guttag, working with media requires many of the concepts covered in lecture and in the book. To top it all you will manipulate and transform images.

Your learning goals are:

* Solidify your understanding of recursion.
* Learn to work with larger data sets using lists and files
* Import and export media (picture) files in PIL
* Use your programming knowledge so far to manipulate pixels in picture files
* Invent and implement algorithms to transform pictures 

# Work Flow

* Step 1: Review Chapters 4 and Chapter 5 of Guttag

* Step 2: Get the starter code by cloning the github repo called spis16-lab05-Pair_Name1_Name2 (where Name1 and Name2 are the first names of the pair partners.) Keep your github repo up to date by committing and pushing your changes frequently.  
If you don't recall how to do this, refer to the instructions on using git to complete the labs: TO DO: Add link

* Step 3: For each of the programming exercises in this lab come up with a solution outline by discussing with your partner. Don't be in a hurry to start coding unless you have a fairly clear idea of a solution strategy and your first steps.

* Step 4: Unit test your code as you write new code using the pytest framework

* Step 5: Once you feel you have sufficiently tested your code, submit it to gradescope (remember you can submit multiple times). Only certain exercises require submitting your code to gradescope Refer to this link for instructions on how to submit your code using git: TO DO: Add link

Remember: Developing code is an iterative process. Your code will probably not work as expected on the very first try. Don't be dismayed. Work through your code to identify bugs, test new code frequently and seek help if you feel you are stuck!

We will start with an exercise that reviews recursion and introduces lists for maintaining a dictionary.

## Scrabble Score

Recursive functions can be very useful when we're reading, writing, and processing strings. Strings are lists of symbols, like words or sentences. For a review of strings, check out Section 2.3 of the Guttag Python textbook. If you have not worked with strings in Python you should read this section of the book before you proceed.

This exercise is about speeding up your Scrabble scoring with Python and it meant to give you practice with recursion, files and lists. If you've ever played Scrabble, you know that each word is assigned a point value given by the sum (adding together) of the points for each of the letters in the word.  For now, we'll ignore special cases like "double word" and "triple letter" that can increase the point value of a word.  Write a Python function letterScore(let) to take as input a single-character string and produce as output the value of that character on a scrabble tile. If the input is not one of the letters from 'a' to 'z', the function should return 0. 

To write this function you will need to use this mapping of letters to scores

![](/lab/images/alphaScrabble.gif)


This function will not involve recursion, but will involve an if-statement (with several elif's and and else).  For example, imagine that your parameter is named letter. You could start with something like:

```
if letter == 'a':
    return 1
elif letter == 'b':
    return 3
# more here
```

What!? Do I have to write 25 or 26 if elif or else statements? Well, you can, but you don't have to! Instead, use the in keyword to combine multiple cases together:

```
>>> 'a' in 'this is a string including a'
True

>>> 'q' in 'this string does not have the the letter before r'
False
```

Phew!
Here are some examples of letterScore in action:

```
>>> letterScore('w')
4
>>> letterScore('%')
0
```

Next, write the function `scrabbleScore(s)` which should take as input a string s, 
which will have only lowercase letters, and should return as output the Scrabble score of that string. For now, ignore the fact that, in reality, the availability of each letter tile is limited. Also ignore the fact that in a real Scrabble game the words played have to be from the Official Scrabble Dictionary and must use only valid letters. You take this into account later in this exercise. If the user inputs a word with capital letters or punctuation, scrabbleScore still outputs a score: the "bad" letters don't contribute any value to the total word score.   Hint: use the above letterScore function and recursion.

Here are some examples:

```
>>> scrabbleScore('quetzal')
25

>>> scrabbleScore('jonquil')
23

>>> scrabbleScore('syzygy')
25
```

Hints:
As with any recursive problem, your first step is to break this problem down into a base case and a recursive step.  For this problem, your recursive step will probably involve pulling off the first letter in the string and processing it, and then using recursion to calculate the scrabble score for the rest of the string.  
Use string indexing (e.g. `word[0]`) to get the first character, and string slicing (e.g. `word[1:]`) to get the rest of the string.
Think about what happens with the empty string.

## Testing your code

To test your code create a new file named `test_scrabble.py` and implement your test cases in this file. to help you with the testing we have provided you with a file named 'reference.txt'. This file contains a list of words and the scrabble score for each word as computed by our reference implementation. Your test code should read this file, extract each word and its corresponding scrabble score. Then check that the output of your scrabbleScore() implementation matches that provided to you in the reference file. Create your own test files and do some more testing. Once you have your scabbleScore() tested, submit your code to gradescope. You may submit it as many times as you like. Then go on to make the following enhancements.

As a second part to this exercise we ask that you additionally check for valid words before computing the scrabble score of that word. Specifically, implement the function `scrabbleScoreDict(word, dictionary)` that takes as input a dictionary parameter and returns the appropriate score. The parameter 'dictionary' is a list of valid scrabble words and not the dictionary data type that Guttag talks about in Chapter 5. The function should return a score of 0 if the dictionary is empty or if 'word' is not a word in the given dictionary. Other than checking for these two conditions `scrabbleScoreDict()` should behave exactly as the function `scrabbleScore()`. Remember that reusing functions that you have already tested is good coding practice. So, we recommend that you use your `scrabbleScore()` function in your implementation of `scrabbleScoreDict()`, without duplicating the code. If you are wondering where the 'dictionary' parameter is going to come from, worry not. As a final piece of this exercise, you will write the code to read and store a dictionary in your Python program.

To build your own dictionary we have given you a file named dictionary.txt in the starter code. This file contains 235,886 words, one on each line of the file. You are required to read each word in dictionary.txt and store it in a list of words.
The function that does this has the following outline:

``` 

def buildDictionary(filename):

    # Creates a dictionary as a list of words by reading the words in the given file. 
    # Assumes the file contains one word per line

    dict =[]    # Creates an empty list that represents a dictionary
    
    # Your code goes here
    
    return dict
``` 

In the file `scrabble_score.py` create a dictionary list by calling the function `buildDictionary('dictionary.txt')`.

A correct implementation of `buildDictionary()` would populate the 'dict' variable with all the words in the dictionary.txt file and return this large list to the caller of the function. Now think on the following questions:

* Is the 'dict' variable visible/accessible to the caller of `buildDictionary()`? Reason about your answer. 

* Do you think that the caller receives a copy of this large list of words? Why or why not?

* Can you comment on the efficiency of using lists in your Python programs?


## Testing your code with the latest additions
Its time to test the two new functions that you just wrote. Add your test cases to the file `test_scrabble_score.py`. You can reuse the reference.txt file provided to you as before. You should also add additional test cases, for example, checking for invalid words that are not in the 'dictionary.txt' file provided to you.

To test your implementation against our test cases, submit your code to gradescope.
As always, make sure you commit and push your code to github frequently. 

You have gained experience with text files and lists. We will now progress to working with media files (specifically pictures). Just like lists, images are represented in your program as mutable types, which means you can change them in place. Look for this common trait in the following exercises on image manipulation





