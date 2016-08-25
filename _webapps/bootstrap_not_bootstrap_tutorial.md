---
topic: "Anything but Bootstrap Tutorial"
desc: "Learning front end design from the ground up, and making
websites that have personality."
indent: true
---

<!--- css written in the file cuz im a bad programmer --->
<style>
   p{
      max-width: 800px; 
   }

   .highlighter-rouge{
      background-color: lightgray;
   }
</style>


# Building the navbar from scratch
Setting up the navbar is quick and dirty when copy pasting code from the
Bootsrap termplates. However, here we will take a little more time to dig deep
into the how the navbar is created. 

The navbar used on this
[website](http://webapps-flask-bootstrap-demo.herokuapp.com) from the
Flask-Bootrap tutorial uses code directly from
[bootstrap](http://getbootstrap.com/components/#navbar). If we were to inspect
the code on the example site, or view the docs on bootstrap, this is the first
line that we would see:

```html
<nav class="navbar navbar-default">
```

From this line we can gather that there's a "<nav>" tag in HTML. The bootstrap
nav tag uses classes `navbar` and `navbar-default`. We have neither of these
written for us so instead, we'll write them later oursleves. 

Within the nav tags, we can insert <a> elements, which are hyper links to other
pages. We will also give them the class "button" and write it later.

```html
<nav class="navbar navbar-default">
   <a class="button" href="/">Home</a> 
   <a class="button" href="/page1">Page 1</a> |
   <a class="button" href="/page2">Page 2</a> 
</nav> 
```

By inserting the code above between our <body> tags we can retain the same
functionality as the the bootstrap navbar we implemented in the Flask-Bootstrap 
demo, and you can see it in action [here](https://basic-navbar.herokuapp.com).

~~~
In the demo site, as well as the basic navbar site, the html code above is
actually written in the navbar.html in the templates folder
~~~

And with just a few more lines of CSS, we'll be able to make our navbar much
more presentable. But what is CSS? To put it simply: CSS describes properties
for HTML elements; telling the browser details of how something should be
displayed. Although, this could be accomplished within the HTML file itself, the
implementation of the style sheets allows the user to implement the rules
without repeating herself/himself. 

#### How to include a CSS file
Inserting a CSS file is done using the link attribute. In the <head> section of HTML
file, insert the following code:

```html
<link rel="stylesheet" href="{_{ url_for('static', filename='navbar.css') }}">
```

Once the CSS code is added, this is what the final result will be a [slightly
better navbar](https://slightly-better-navbar.herokuapp.com)

Note: href may change based on where the css is placed. Format of href link may
also vary. Oh and ignore the underscore between the two brackets. Temporary fix
to keep the link from disappearing because I'm too tired for a clever solution.

#### Writing the CSS file
Now, there's wasn't really any point in giving the nav bar two classes for out
intent and purposes. So, in the static folder (because that's where our link is
pointing, we're going to create navbar.css. To properly define a class we
write its properties in the squigly brackets following its name, which is
written with a period "." in *....and I'm asleep*

OKAY IM AWAKE. There's a great explanation of class vs ID in you starter files.

#####What are the properties of the navbar that will make it look better?

There's many ways to approach this. And different property settings may result
in the same navbar.

# The Rest is Under Construction :)
![under construction](http://www.animatedgif.net/underconstruction/5consbar2_e0.gif)

# What is BootStrap?

   [BootStrap](http://getbootstrap.com) is comprised of HTML, CSS
   and JavaScript presets used to create responsive websites that work
   seamlessly on mobile devices. ~~"However, cliched, unoriginal, symbolic
   of everything wrong with society and capitalism" -M. Bland.~~ BootStrap
   should be used as a library, and you should refrain from using bootstrap
   templates, especially if your purpose is to learn how to build a website from
   the ground up, and remove all the magic behind from the scenes. Once you
   understand the magic: how HTML, CSS, and JS come together to form a fluid and
   responsive website, templates become more maleable in your hands, and
   BootStrap code becomes more clear.  

# Where To Start with HTML
   HTML is found here, there, and everywhere on the internet, and you can look
   at the code that makes up any site by opening up web inspector (the shortcut
         for which is ctrl+shift+i; cmd+opt+i on macs). 


## divs within divs within divs within divs within divs within divs...
   Go on any website, and use the web inspector, and you will see many divs
   enclosed within others. For our purposes, we'll use YouTube as our example.
   If you were to use the web inspector to find one of the images in the
   recommended tab, you would find it enclosed in a dozen divs. These divs have
   IDs and classes, both of which can be modified using CSS, but each element
   can only have one ID, and 


## height? width? percentages? vh? em? px? 
Ipsum volutpat, donec ipsum praesent. Nec nulla odio in congue penatibus donec,
porttitor vehicula, est lectus wisi est justo et. In eget maecenas viverra
mauris eget id, ullamco volutpat in, sit tincidunt, illum arcu quis
consectetuer id aliquam. Lacus tortor cras purus velit egestas. Wisi
integer vestibulum, vitae sed ac etiam quisque netus, tincidunt in
maecenas, egestas morbi voluptas turpis quam consequat quam, vel odio
convallis vitae sed mauris turpis. Neque leo quisque eros maecenas,
vulputate euismod tellus, sit nam sapien eu sapien, in felis arcu
voluptatem.



## location: fixed, static, floating, relative
Lorem ipsum dolor sit amet, sed a, blandit volutpat autem a lorem non. Tortor
ipsum et sed sodales integer, ut mi mi purus sapien egestas cum, nibh pretium
est, molestie vestibulum vestibulum metus phasellus, conubia tellus rerum. Nam
vitae, massa wisi vel maecenas. Enim sed, interdum justo pede id nisl ut. A eget
ipsum orci etiam.



<!--- happy comments for myself 


--->
