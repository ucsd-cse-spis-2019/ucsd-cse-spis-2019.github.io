---
topic: "Problems: Fizzbuzz"
desc: "A sample toy problem"
---

# The fizzbuzz problem

The fizzbuzz problem takes it name from a game where the players take turns, going clockwise in a circle, counting
upwards from 1: that is, 1, 2, 3, etc.

Except that there are three rules:
* If the number is divisble by 3, you say "fizz" instead of the number.  
    * For example, 1, 2, fizz, 4, ...
* If the number is divisible by 5, you say "buzz" instead of the number.  
    * For example, 1, 2, fizz, 4, buzz, fizz, 7...
* If the number is divisible by both 3 and 5, you say "fizzbuzz" instead of the number.
    * For example, ... 13, 14, fizzbuzz, 16, ...
    
Recast as a programming problem, fizzbuzz goes like this:

> Write a function that takes an single integer parameter, and returns a string.
> The parameter x is an integer greater than or equal to 1.
> The return value should be either the number x formatted as a string, or the word "fizz", "buzz", or "fizzbuzz" as appropriate.

For example: 

* `fizzbuzz(1)` should return `"1"`
* `fizzbuzz(2)` should return `"2"`
* `fizzbuzz(3)` should return `"fizz"`
* `fizzbuzz(4)` should return `"4"`
* `fizzbuzz(5)` should return `"buzz"`
* `fizzbuzz(6)` should return `"fizz"`
* `fizzbuzz(7)` should return `"7"`
* ...
* `fizzbuzz(15)` should return `"fizzbuzz"`
