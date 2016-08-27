---
topic: "Paper.js"
desc: "A client-side library for working with the Canvas element"
---

# What is `paper.js`

Paper.js, which is online at [paperjs.org](http://paperjs.org), is a client client-side library for working with the Canvas element.

If you want to draw graphics on a web page "on the fly", and/or allow manipulation of graphics right in the browser,
paperjs may be the tool you want.

# Example of `paper.js` with Flask

Here is an running example on Heroku: <https://spis16-webapps-paperjs.herokuapp.com/>

And here is the repository of code that makes that example work: <https://github.com/ucsd-cse-spis-2016/spis16-webapps-paperjs>

# Alternatives to `paper.js`

Another option is [processingjs](http://processing.js), which is a browser-based  implementation of a programming language known as *Processing* (online at [processing.org](http://processing.org))

* The chief advantages of [processingjs](http://processing.js) over `paper.js` is that more people know Processing, and you are
    more likely to use it in future CS, CSE, or Cognitive Science courses.
* One key advantage of `paper.js` over Processing is that with `paper.js`, it is easy to save/restore the things you draw
    to and from SVG, a plain text representation of your drawing as vector graphics.   
    * With processing, all you have is pixels (digital ink on paper.)  
    * With paper.js, you can save and retrieve what you have drawn, and do computations on it.
    
  


 https://spis16-webapps-paperjs.herokuapp.com/
