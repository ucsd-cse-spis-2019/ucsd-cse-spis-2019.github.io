---
layout: lab
num: lab07
ready: false
desc: "Working With Data"
assigned: 2018-08-22 13:15:00.00-7
due: 2018-08-25 16:45:00.00-7
---

# Working with and learning from data

This lab will give you a taste of the very hot field of machine learning.  The basic idea of machine learning is to use data to build a program/model that can geneate or make predictions about new data.  In this lab, you will:
 * use basic Python libraries and functions to read date from a file and do basic processing of data
 * build models to generate or predict data

You will complete this entire lab using *pair programming*.  Of course, you are free to work on the extension by yourself, especially if you decide to do a machine learning project and your partner does not.  But, as usual, **do not leave your partner in the dust!**

# First, create a lab07 repo

Go to github.com and create a new empty repo called spis18-lab07-Name1-Name2. When creating the repo import the starter file from this git repo: `https://github.com/ucsd-cse-spis-2018/lab07starter.git`

Then use `git clone` to clone this into your `~/github` directory.

# Lab outline 
 * Part 1: Reading from files, working with dictionaries and building Markov chains to predict text
 * Part 2: Training and using a classifier using the `nltk` library
 
# Machine Learning: Very Basic Overview
The basic idea behind machine learning (ML) is to use data to build a "model".  You can think of a model as a computer program that "knows" something about the world. In our case, the model knows how to respond to data in some kind of a human-like way.  

There are three basic steps to any ML task:
1. Select an appropriate model and an appropriate data representation
2. Train the model on some examples
3. Use the model to perform some kind of human-like task

# Part 1: Markov chains and text generation

## The task: Writing text
In the first part of lab07, we will build a model that is capable of writing text.  It can write tweets, or your English essay.  And they will seem (almost) like a human could have written them.

## Step 1 (nothing to do, but do read): Model selection and data representation
In this part, we will use a model called a Markov Chain.  The basic idea behind the Markov Chain we will build is that the probability of a word in a sentence is based only on the word(s) that immediately precede(s) it.  The number of preceding words (or generally, data items) that we consider defines the "order" of the Markov chain.  A first-order Markov chain considers only the word immediately preceding the next, a second-order chain would use the two words immediately preceding, etc.  In this lab we will work with first-order Markov chains, which themselves can be quite powerful when applied to words.  For example, if I see the word "sunny" then there is a relatively high probability that the word "day," "disposition," or "side" (as in "sunny side up") will come next, but a much lower probability that I will next see the word "the", "down" or "shark".  So just by hearing the word "sunny", you have a pretty good idea of the words that might come next.  We will build a Markov chain that has this same knowldege.  Of course, if you heard "It's going to be a sunny..." you'd be almost certain that the next word is "day".  This certainty would require a higher-order Markov chain.

The data representation we will use here is simple: we will represent text as a sequence of words.

## Step 2: Train the model
The way the Markov chain actually works is by using what are called "transition probabilities".  In our specific application, the transition probabilities specify the probabilities of each word following next, given the current word you are looking at.  So in our example above, the transition probability for the word "sunny" might be P("day"|"sunny") = 0.6, P("side"|"sunny") = 0.3, P("disposition"|"sunny")=0.1, and P(*any other word*|"sunny")=0.  Each of these probabilities can be read as "The probability of the next word being "day" given that the word I'm on now is "sunny" is 0.6".  Notice that the transition probabilities given a single word (in this case the word is "sunny") will always sum to 1.  

Training our model  involves learning these transition probabilities for each word in our vocbulary.  We will do this using "training data", i.e. some sample pieces of text.  You will write a program to "read" the text and to keep track of the distribution of words that follow each word in the text.  For example, if you were given the following line of text:

"Yeah baby I like it like that
You gotta believe me when I tell you
I said I like it like that"

You would calculate that given the word "Yeah" the only word that can follow is "baby".  Given "baby" the only word that follows is "I".  Given "I" the words that might following are: "like", "tell" and "said".  "like" occurs twice after "I", while "tell" and "said" each occur once.  In other words, P("like"|"I")=0.5, P("tell"|"I")=0.25, and P("said"|"I")=0.25.  Another way we can represent these proportions is to use a list: `["like", "tell", "said", "like"]` where each word is represented in the relative proportion that it occurs.  Then we can associate it with the word we are transitioning from using a dictionary, like this:

`{"I" : ["like", "tell", "said", "like"]} `

This is the approach we will use.

### Write a method to train the model
Write a python function `train(s)` that takes a string, `s` and returns a dictionary representing the transition probabilities in the representation described above. That is, each word `w` in `s` should be a key in the dictionary.  `w`'s associated value should be a list containing all of the words that followed `w` in `s` in their relative proportions to what is in the string `s`.  For example, for the string above, the dictionary returned would be:
```
{
  'Yeah': ['baby'], 
  'baby': ['I'], 
  'I': ['like', 'tell', 'said', 'like'], 
  'like': ['it', 'that', 'it', 'that'], 
  'it': ['like', 'like'], 
  'that': ['You', 'Yeah'], 
  'You': ['gotta'], 
  'gotta': ['believe'], 
  'believe': ['me'], 
  'me': ['when'], 
  'when': ['I'], 
  'tell': ['you'], 
  'you': ['I'], 
  'said': ['I']
}
```

Note the following:
 * You can preserve capitalization, treating capitalized words as different from lowercase words.  Notice in the dictionary above "You" is different from "you".
 * You should imagine that your string wraps around, and that the last word is followed by the first word.  Notice that in the dictory above, "Yeah" (the last word) follows "that" (the first word).
 * You can keep punctuation attached to the word it is associated with, and treat a word with punctuation as different from a word without punctuation.  For example, if the text were:
 
 "Yeah baby I like it like that.
You gotta believe me when I tell you
I said I like it like that"

Then the word "that." (with a period) would be treated separately from the word "that" (with no period).

*Hint: You will find the python string function `split` to be useful in breaking the string `s` into a list of words.  You can find documentation for the [`split` function here](https://docs.python.org/3/library/stdtypes.html#string-methods)*

## Step 3: The Human-like task: Generating Text
Write a python function `generate(model, firstWord, numWords)`.  This method takes the following parameters:
* `model` -- a dictionary representing the trained model as output from the `train` method.
* `firstWord` -- the word to use as the first word in the generated text.  This word *must* be a key in the model.
* `numWords` -- the number of words in the returned generated string.
The function returns a string generated randomly from the model, starting with `firstWord` and containing `numWords`.  To generate the next word in the returned string, the funciton should randomly pick one of the words in the model that has non-zero probability of occurring next.  That is, randomly pick one of the words from the list associated with the current word!

For our model above, here are the results of several calls to `generate`:

```python
>>> cardiB = train("Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that")
>>> generate(cardiB, "I", 10)
'I said I tell you I like it like it'
>>> generate(cardiB, "I", 10)
'I said I tell you I said I tell you'
>>> generate(cardiB, "I", 10)
'I said I like it like that Yeah baby I'
>>> generate(cardiB, "Yeah", 15)
'Yeah baby I like it like that You gotta believe me when I like that'
```

Notice that it will generate different strings with the same input.  You will need to use the `random.randrange` function to select your next word (make sure to 'import random' in order to use random.randrange).  We will go over some examples in class, or you can look at the [documentation here](https://docs.python.org/3/library/random.html).

### How do you test code with randomness?
It can be tough to test your code when it relies on randomness to function.  There are ways to do it, but for now, just try running your code several times, and make sure you eventually get different strings, and that all of the words that should be represented seem to be represented.

## Have fun!
Now that you can train a model and generate text, play around with generating text using different training data.  We've provided some song lyrics and some tweets for you to use.  Have fun and see what you get!

Song Files: Each file is titled after the artist whose songs are in that file. Each line in the file contains all the lyrics to one of their songs. You can train one song at a time or all the songs at once and generate your own lyrics. Play around with the songs, artists, and maybe even try to mash some files together!  

## Add, Commit and Push
Once you have tested your code and you think it is working, you are done with the first part of the lab.  Make sure you have added all of your files to your repo, committed them, and pushed them to github.


# Part 2: Classification of text sentiment
The second half of this lab will introduce you to another major task in Machine Learning: classification.  In the previous section we built a model to *generate* new data.  In this section we will build models to *classify* data that already exists.  In particular, we will be building our own version of Rotten Tomatoes by automatically classifying the sentiment of movie reviews.  

## Step 1: Choose the model and data representation
This time we will be using a model called the "Naive Bayes" model.  Like the Markov chain we used in Part 1, the Naive Bayes model is again based on probabilities.  

First, let's talk about how we will represent the data in this part.  Our data set will consist of a number of documents, each labeled as either positive or negative.  For example, we might have the following documents in our data set:

| Document text | Sentiment |
| ------------- |-----------|
| "One of the most highly-praised disappointments I 've had the misfortune to watch in quite some time ." | negative |
| "The movie resolutely avoids all the comic possibilities of its situation , and becomes one more dumb high school comedy about sex gags and prom dates ." | negative |
| "Very well written and directed with brutal honesty and respect for its audience ." | positive |
| "Leguizamo and Jones are both excellent and the rest of the cast is uniformly superb ." | positive |

Because we have labels for our training examples, we are performing what is called "supervised learning".  We are going to teach our model to distinguish between documents that have a positive sentiment and those that have a negative sentiment.

We are not going to represent our documents as plain text, however, because this approach won't work with our model.  Instead we are going to use a very simple version of a representation called a *bag of words*.  Instead of words in order, we will simply record the presence of each word in the document with a boolean variable set to True.  It will be implied that all the other words in our vocabulary will be False.  [This page](https://machinelearningmastery.com/gentle-introduction-bag-words-model/) has more about the bag of words representation if you are interested in learning more (e.g. for the project).

Once we have our documents represented in this bag of words representation, we will train a model known as a Naive Bayes model.  I won't go into the details here about how this model works, but the basic idea is that the model will represent the probability of each word in our vocabulary occurring in a positive document and the probability of each word in our vocabulary appearing in a negative review.  The model also needs to know the overall proportion of positive to negative reviews.  From this information, you can use the model to compare the probability of a given (new) review is positive with the probability that this review is negative.  Classification just selects the class (positive or negative) with the higher probability according to the model.  

If you want to know more details, there is a pretty nice, simple overview of the Naive Bayes model for text classification on [this site](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/).

## Step 2: Transform the data and train the model
Now we will get to the coding. Open the file `classifyReviews.py`. 
### Format the training and testing data
In the file `classifyReviews.py` you will see that some code is provided for you.  Look at the `classifyReviews` function, which is the main method where the program will start.  You will see code that extracts the reviews from the file.  If you open the `movieReviews.csv` file you will see that the reviews are rated from negative to positive on a 5 point scale (0-4).  However, for the purpose of this assignmetn, we will use only very positive and very negative reviews in our classification, so the next two lines extract the text of only the very positive and very negative reviews using a function we have provided for you.

Your first task is to **complete the function `splitTrainTest(data, trainProp)`.**  You will find the skeleton code for this method at the top of the file.  This function should take a list of strings and a number between 0 and 1.  It returns a tuple of two lists where the first list has trainProp proportion of the strings in it, while the second has 1-trainProp proportion of the strings.  Here are a few examples:
```python
>>> splitTrainTest(["A", "B", "C", "D"], 0.25)
(["A"], ["B", "C", "D"])
>>> splitTrainTest(["A", "B", "C", "D"], 0.1)
([], ["A", "B", "C", "D"])
>>> splitTrainTest(["A", "B", "C", "D"], 0.6)
(["A", "B"], ["C", "D"])
```

*Hint: The casting function `int()` and list slicing can make this function just one line!*

**Make sure you test this function well before moving on!**

Next, **complete the function formatForClassifier(dataList, label)**.  This function takes a list of text string reviews and a label for these reviews (they must all have the same label) and it returns a list of lists, where the first element in each sublist is the result of calling the provided `format_sentence` function on the text review, and the second element in the sublist is the text label.  Here is one example:

```python
>>> formatForClassifier(["A good one", "The best!"], "pos")
[[{'A': True, 'good': True, 'one': True}, "pos"], [{'The': True, 'best': True, '!': True}, "pos]]
```
Remember that the first element in each sublist (the dictionary) is just the result of calling the provided `format_sentence` function on the text of the review.

**Again, test your code on SIMPLE examples before moving on.  DO NOT attempt to look at the results on the full set of reviews!  Use simple examples at the prompt such as the one above.**

Once you are sure you have the two functions above working, you can uncomment the line:

```classifier = NaiveBayesClassifier.train(training)```

And you will have a trained classifier.

## Step 3: Use the classifier to perform classification
The library we are using, `nltk`, provides some built-in support for understanding how and how well our classifier is working.  Uncomment the next two lines in the file:
```python
print("Accuracy of the classifier is: " + str(accuracy(classifier, test)))
classifier.show_most_informative_features()
```
The first of these lines will show you the overall accuracy of the classifier (the percentage reviews in the *test* set (NOT the training set!) that it classifies correctly.   Are you surprised by this accuracy?  Discuss with your partner.

The second line will show you the features (words) that are most helpful in distinguishing between the positive and negative reviews.  For example:

```
neg : pos    =     33.8 : 1.0
```
means that the word in question is 33.8 times more likely to appear in a negative document than a positive one.

Look at the most useful features.  Again, discuss these with your partner.  Do they make sense?

### (If you have time) Explore more about how the classifier performs 
Finally, you will write your own code to help you understand more about how the classifier is performing.  

Near the bottom of the `classifyReviews` function, **write code that will display the accuracy of your classifier on positive examples
and on negative examples, separately.**  There are some hints in the comments of the starter code about how you can do this.  You will need to count the number of misclassified examples and divide it by the total number of examples of that class.  

Compare these numbers to the overall classification accuracy.  Is your classifier better at classifying positive or negative documents?  Why do you think this is?

Finally, again next the bottom of the `classifyReviews` function, **write code that displays the misclassified reviews**.  This can help you understand how your classifier is performing and give you some hints about what it might be getting wrong and how to improve it. 
Once you have done this look at the misclassified examples.  Does it make sense why these were misclassified?  Discuss this with your partner.

# Add, commit, push
You've made it to the end of lab07.  Congratulations!  Make sure you push your code to github.  I hope you are excited about ML and are interested in exploring a machine learning project.  If you are, we've got some ideas for you below.

# Possible project ideas!
You are done with lab07, but if you're interested in completing a machine learning project (or you just want to explore more), here are some ideas!  They are labeled with what we think will be the relative difficulty of each.

* (*low to medium difficulty*) Explore small extensions to the review classification code you wrote in this lab.  These extensions could include: removing stop words, including more reviews in the positive and negative sets (e.g. the 3s and the 1s), or exploring sentiment classification on other datasets that you find online, or anything else you want to explore.

* (*medium difficulty*) Write a Markov chain to generate text where you represent each "basic unit" as a character instead of a full word.  That is, build a model that predicts the next character, given one (or more) preceding characters.  If you do this with a first-order Markov model, you are likely to get garbarge, so you'll need to figure out how to increase the order of your model.  Once you can build a model of order 8 or so, you'll be surprised at how realistic the text sounds!  And it will be much more original than the order-one word-based model.

* (*medium to high difficulty*) Explore other text classification algorithms included in the `nltk` library.  Compare their performance to the Naive Bayes clasifier.

* (*high difficulty*) The `nltk` library is fairly limited in what it can support.  But it is just a wrapper on top of the much more powerful `scikit.learn` library.  Use the `scikit.learn` library to build more flexible or powerful classification models.  You might use a different feature set (e.g. Bag of Words with counts instead of binary), or try a different classification task entirely (e.g. using linear regression to predict the actual rating score of the reviews).  

* (*high difficulty*) Find a completely new dataset and do any kind of classification task using `nltk`, `scikit.learn` or just coding a classification algorithm by hand.  (A good one to code by hand is K-Nearest-Neighbors). 

Alright! You're finished with lab 07!

