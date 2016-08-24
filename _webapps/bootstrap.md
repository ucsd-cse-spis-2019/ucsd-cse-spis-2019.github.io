---
topic: "Bootstrap Navigation Bar Demo"
desc: "A quick and dirty way to get a navigation bar"
---

# So, you want common navigation for your web app

Most real world web apps have some kind of "common navigation".  That is, there are some elements of each page of the 
application that stay the same from page to page, and give the user a way to get from one part of the app to another.

These can be buttons, menus, etc.

For example, the website you are now looking at has common navigation at the top of each page, with buttons that link to various
part of the SPIS website, and/or to other useful resources for SPIS participants.

Maybe you want that for your webapp.

One way to do it is with a library called Bootstrap.  Bootstrap has its pros and cons.  Among them are these:

* Pro: it is fairly easy, if you just follow a simple template (provided below) to get up and running with something useful pretty quickly,
    and you only need a minimal understanding of HTML and CSS.
* Con: the solution has a bit of "mystery code" in it that can be unnerving.
* Biggest Con: Sim and Max will laugh at you and mock your website.   They will be "so disappointed". 

Later on this page, we'll explain what Sim and Max have against Bootstrap, and what you might do instead.

But for now, here's a link to a repo that has a simple example of using Bootstrap in the context of a the kinds of Flask
web apps we've been looking at in SPIS.

* Repo: [https://github.com/ucsd-cse-spis-2016/webapps-flask-bootstrap-demo1](https://github.com/ucsd-cse-spis-2016/webapps-flask-bootstrap-demo1)
* Running code on Heroku: [http://webapps-flask-bootstrap-demo.herokuapp.com/](http://webapps-flask-bootstrap-demo.herokuapp.com/)


# Why no love for Bootstrap?  

Bootstrap has a bad reputation among web design hipsters, because it tends to be overused by folks with questionable design skills and or taste.

It enables user to use a simple template, which is both good and bad.   The good is that you get working quickly.  The bad is that your
site looks just like every other site in the whole world.   

The biggest pitfall is "Bootstrap Templates" that first time users may not know how to modify in order to properly personalize.   They might
end up with "non-working buttons" and menus still hanging around that should have been eliminated, or color, font and other design choices
that the template designers never intended for them to keep around forever.

# What could I do instead?

Sim has been working on a tutorial called [Anything but Bootstrap](/topics/bootstrap_not_bootstrap_tutorial/).   It is possible to acheive common navigation very similar to, or
perhaps even superior to, the common navigation in the Bootstrap example explained above.

One advantage of using Sim's tutorial (vs. the Bootstrap method above) is that you'll have a much deeper understanding of HTML, CSS, etc.

That will put you in a position where, whether you ultimately decide to roll your own custom designs, or use systems such as Bootstrap,
you'll be much better able to customize and tailor them to your needs and preferences.

So, it is entirely up to you.   Phill is happy either way.  Sim, however, has definite preferences. :-)
