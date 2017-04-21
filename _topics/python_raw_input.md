---
topic: "Python: raw_input"
desc: "reading some input in a terminal session"
---

Python has a `raw_input("prompt goes here")` function that can be used to read input from the user in a terminal session.

The value that gets returned comes back in the form of a string.

The Guttag textbook uses this function in several of the early chapters.

# A hint for the finger exercise on p. 20

The finger exercise on p. 20 of Guttag asks you to read in 10 numbers from the user.

The following Python code shows a hint for how to use `raw_input()` to read in 10 numbers, and
what you might do with that input to solve the problem given.

```python
# A hint for the finger exercise on p. 20 of Guttag
# This shows one way to read 10 integers with a while loop and raw_input

how_many = 10

# some initialization code goes here
# You may need to set up some variables that keep track of things

while (how_many > 0):
    
    number= raw_input('Please enter a number:')
    print("Your number is: " + number)

    # Some code to look at each number goes here
    # You may need to look at the current value of number
    # decide whether it is odd, and if it is, update something
    # depending on whether it is bigger than any odd number you've seen before

    how_many = how_many - 1

    print "I'm going to do this", how_many, "more times"

# code to print the largest odd number goes here

```

