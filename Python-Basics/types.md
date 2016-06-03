# Types in Python

In Python, every piece of data we deal with has a type.

Some of the most basic types are:

* `int` for integers (e.g. `-42`, `0`, `3`, `4567`)
* `float` for numbers that have decimal points, (e.g. `3.14159`, `0.5`, `-67.0`,`1.0`, `6.0221409e+23`)
* `bool` for the special values `True` and `False`

Some commonly used types that involve collections of things are:

* `str` for sequence of characters (e.g. `'Chris'`, `'UCSD'`, `'Computer Science & Engineering'`, `'6th College'`)
* `list` for lists of items, where the items can be of any type, or a mix of types.  Examples:
 - `[6, 10, 4, 17]`
 - `['Revelle', 'Muir', 'Marshall', 'Warren', 'Roosevelt', 'Sixth']`
 - `['Chris','Diaz',9876544,True]`

There are additional types that are less commonly discussed in "introductory programming", but that may end up being useful.

* `Unicode` for sequences of a [larger set of characters](http://www.unicode.org) (e.g. `u'四'`, `u'piñata'`).
 - A python file that contains these characters may need to have a [special comment at the top](https://www.python.org/dev/peps/pep-0263/) to avoid errors when compiling. 
 - Example special comment for unicode: `# -*- coding: utf-8 -*-` 
