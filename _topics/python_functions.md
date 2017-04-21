---
topic: "Python: Functions"
desc: "reusable units of code"
---

Many scientific fields have a basic unit of study:

* Biology has the *cell*
* Chemistry has *atoms* and *molecules*

In Computer Science, our basic unit of study is the *function*.

No matter what programming language you work in&mdash;whether Python, Java, C, C++, C#, JavaScript, Haskell, Scala, PHP, etc.&mdash;
you will work with functions.  (In some contexts, functions are called *methods*, but they are still *functions*).

You are already familiar with functions from your high school math classes.
You probably first encountered them in Algebra&nbsp;I.

For example, in math class, we write: 

$$
 f(x) = x^2 
$$

This defines a function $$ f $$ that takes one parameter $$ x $$, and returns
the value of $$ x^2 $$.  For example, $$ f(3) $$ is 9, and if $$ a=5 $$, then
$$ f(a) $$ is 25.

In Python, we write the same function this way:

```python
def f(x):
   return x**2
```

Then we can evaluate `f` for various values of `x` at the Python prompt:

```
>>> def f(x):
...    return x**2
... 
>>> f(3)
9
>>> a=5
>>> f(a)
25
>>> 
```





