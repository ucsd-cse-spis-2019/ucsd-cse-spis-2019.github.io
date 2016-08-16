---
topic: "Python: Dictionaries"
desc: "Mappings from keys to values"
---

In Python, we can use a *dictionary* to associate keys with values.

This code creates a simple dictionary called `en_to_es` (short for "English to Español), that
maps the words `one`, `two` and `three` (as Python strings) to their Spanish counterparts (as
Python strings):

```python
en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
```

Once you create a dictionary, you can access the values by looking up their key.
Here, we show trying some Python dictionary code at the interactive Python shell:

```python
>>> en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
>>> en_to_es['one']
'uno'
>>> en_to_es['three']
'tres'
>>> 
```

If a particular key is not in the dictionary, and you try to look it up, you get a 
`KeyError`, like this:

``` python
>>> en_to_es['ten']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'ten'
>>> 
```

# Handling `KeyError` with `try`/`except`

You can use a so-called `try`/`except` block to write custom code that looks for the
`KeyError` and instead of printing a scary looking error message, does whatever you
would prefer:

Suppose we run this file:

```python
def translate(myDictionary,wordToLookup):
    ''' lookup word.  return NoneType value if word not found '''
    try:
        return myDictionary[wordToLookup]
    except KeyError:
        print "The word ",wordToLookup," was not in the dictionary"
        return


en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
```
    
Then, we can use the function `translate` to do translation with a "nicer" error message.

```
=============== RESTART: /Users/pconrad/Documents/translate.py ===============
>>> en_to_es
{'three': 'tres', 'two': 'dos', 'one': 'uno'}
>>> en_to_es['one']
'uno'
>>> en_to_es['ten']

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    en_to_es['ten']
KeyError: 'ten'
>>> translate(en_to_es,'one')
'uno'
>>> translate(en_to_es,'ten')
The word  ten  was not in the dictionary
>>> 
```

# Dictionaries of Dictionaries

Two letter language codes for various human spoken languages have
been standardized by the International Standards Organization, ISO, and can be looked up
[at this web page](https://www.loc.gov/standards/iso639-2/php/code_list.php))

Here are just a few.   The third column explains why, for example, 
German is `de` and Chinese is `zh`.

|code| Language (in English) | Language (in that language,<br>using latin alphabet)|
|----|-----------------------|-----------------------------------------------------|
|de  | German                | Deutsch |
|en  | English               | English |
|es  | Spanish               | Español  |
|fr  | French                | Français |
|fa  | Persian               | Farsi  |
|zh  | Chinese               | Zhongwen |

We could construct a dictionary of these codes like this:

```python
codeToLanguage = {
  'de' : 'German',
  'en' : 'English',
  'es' : 'Spanish',
  'fr' : 'French',
  'fa' : 'Persian',
  'zh' : 'Chinese',
}
```

If we wanted to translate the number 'one','two','three' into each of these languages, we
could create six different dictionaries, like this:

```python

```

