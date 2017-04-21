---
topic: "Python: defaultdict"
desc: "A special kind of dictionary"
---

# `defaultdict`: A special kind of python dictionary

The following page assumes that you are already comfortable with the basics of *dictionaries* in Python (i.e. the `dict` datatype,
such as `enEs={'one':'uno','two':'dos','three':'tres'}`.  If that is not the case, please read this page first:

* [Python: Dictionaries](/topics/python_dictionaries)

# What is a `defaultdict`

A `defaultdict` is a special kind of Python dictionary where you can define a "default" value for keys to map to.



That is, if you look up a key in that dictionary, and the key is not found, instead of getting a `KeyError`, you get
the default value.

One useful trick you can do with a `defaultdict` is counting occurences of things.

For example, suppose you had some text, such as the Declaration of Independence, a Shakespeare play, or a speech by 
a political candidate.  Suppose you wanted to count how many times each word occurs, for example how many times the word
"America" or "People" appears in some piece of text.

When you use a default dict, you choose the type that the values are going to have, for example:

```
   from collections import defaultdict
   words_dict = defaultdict(int)
```

Now, words_dict is a dictionary where, if I look up any key, the value I get back will be `0`, unless I've set some
other value.

What I can then do, it each time I see a word, I can increment the value for that word, like this:

```
   words_dict[word] = words_dict[word] + 1
```

With this code, if I've never seen `word` before, then its default value is `0`.  But, if I *have* seen `word` before,
then its value might be, say, 7, represnting the fact that I've seen the word seven times&mdash;I add one, and now the value is `8`.

I can also so something similar by making a `defaultdict(list)`, where the default value is an empty list, or `defaultdict(str)` where the default value is an empty string.

For a list, I can use this code to lookup some key in the dictionary, and add some `newThing` to the list for that key:

```
  someDict[key].append(newThing)
```

For more information, see the [Python documentation for `defaultdict`](https://docs.python.org/2/library/collections.html#defaultdict-examples)
