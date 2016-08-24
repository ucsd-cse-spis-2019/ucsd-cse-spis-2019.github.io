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


# Under Construction :)
![under construction](http://www.animatedgif.net/underconstruction/5consbar2_e0.gif)

```html
<h1> <blink> What is BootStrap? </blink></h1>

```

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

```html
<nav class="navbar navbar-default">
   <a href="/page1">Page 1</a> |
   <a href="/page2">Page 2</a> 
</nav> 
```

Insert that code between your <body> tags. Now if you were to run this, you
would essentially have the same functionality as the bootstrap navbar we have
implemented in the Flask-Bootstrap demo, and you can see it in action
[here](https://basic-navbar.herokuapp.com).

<!--- happy comments for myself 


--->
