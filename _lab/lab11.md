---
layout: lab
num: lab11
ready: false
desc: "Project Planning"
assigned: 2016-08-24 10:15:00.00-7
due: 2016-08-24 15:00:00.00-7
---

# Planning your Project

This lab should be completed during the Open Lab time on Wednesday of Spis Week 4, together with your [New Pair Partner for the Project Phase](/info/pairs/).

In this lab, you'll create a github repo called <br>
`spis16-project-planning-`<em>areaname</em>`-`<em>Name</em>`-`<em>Name</em>. In the `README.md` of that repo,
you'll start writing some plans for your project.

# About the due date of 3pm Wednesday of Week 4

We'd like you to have at least an "initial" version of this by 3pm on the Wednesday of Week 4. 

* But, that doesn't mean it will be a "finished product" at that point that you never come back to.  
* On the contraryYou may well find that we come back to the README.md of this repo again and again throughout the rest
of SPIS.
* It fact, it may well form the basis of activities you do on Thursday and Friday of Week 4, and throughout Week 4.

But for today, at least try to complete all of the steps listed below.


# Goals

This lab has one main goal:

* To help you start the planning process of what you want to do for your SPIS final project

In the case where you have a new pair partner, it also serves as a way for you to get to know each other.

# What you'll be doing

This lab has three steps:

1.  Create a *public* repo (this time, we are going open source) with one of the naming conventions below.  Use just your 
    first names, as they appear in the new pairs list, and with the first names in the order they appear their (alphabetical, i.e. `Alex_Chris`, not `Chris_Alex`.   Capitalize only the names; everything else should be lowercase.

    * For Robotics/Hardware: `spis16-project-planning-robotics-Name-Name`
    * For Data Mining: `spis16-project-planning-datamining-Name-Name`
    * For Web Apps: `spis16-project-planning-webapps-Name-Name`
    
2.  Whoever creates the repo, be sure to add the second pair as a collaborator with Admin access, as explained here.

3.  Edit the README.md file, and into it, put a description of your thoughts about the project you want to undertake.

    For the details of what to write, see the section "Creating your project plan in the README.md file"

    *If you don't yet have a clear idea about what that will look like*&mdash;if you are literally thinking "what? We have
    absolutely no idea what what we want to do in this area!?!", *don't worry*.  Part of this exercise is about (a) identifying which pairs are at that stage, and (b) helping them get past it.   So, if that's where you are,
    this lab is the right thing to be working on to get you past that point.   There is more informatio below.
    
4.  Once you have something that feels like a coherent description of where you and your partner are: either a 
    coherent description of your project, OR a description of where you are (perhaps completely "blank" and in need
    of some suggestions or guidance, ask one of the mentors or instructors for your area to take a look at it and
    offer you some feedback.      This step may continue into Thursday if we run out of time for it Wednesday.

    *Mentors/Instructors*: Please [create a private feedback repo for this pair](/mentor/feedback-repo/) (or use the existing one if its an
    already existing pair, and put some written feedback in that repo.  You can and should *also*, if possible,
    offer in-person verbal feedback.  But please also create a feedback repo and put in at least a brief summary
    of your feedback, even if that is just "This plan looks good.  You are off to a good start.  Let the
    mentors and instructors know if you have questions about how to proceed"
    
# Creating your project plan in the README.md file

Please add the following information to your README.md file.  For each section, you can use the following 
markdown syntax to indicate a section headings.  Here is an example of what that would look like:

```markdown

# Names, Area, Mentor

Alex T. Chris L., Robotics, Mentor: Ashley

# Brief Description

We plan to build a doomsday clock.   It will be a Raspberry Pi connected to seven 7-segment 
number displays: three for the hours, two for the minutes and two for the seconds.  It will indicate a countdown 
timer in hours, minutes, seconds to the next event from some  schedule.    The events will initially 
be hard coded in a Python dictionary, and might represent, for example a weekly Fall Course 
schedule, or the deadline for some assignment.     If we have time, we might also add green, 
yellow and red LEDS that will light up as the time gets closer (green is still more than three 
or more days away, yellow two or more days away, red is one day of less away.   The intervals for
the red, yellow and green should be customizable in the Python code (maybe 3 minutes, 2 minutes,
1 minute---otherwise we won't be able to test it or demo it during SPIS!).   With three 
displays for the hour, and two for the minutes, we can handle events up to 40 days in the future.

etc...
```

Here's what to put in the file:

1.  *Names*: Your names (first name plus last initial is sufficient.)

2.  *Brief Description*: A brief description of your initial stage for planning the project.  
    If you have a clear, or even a vague idea,
    about what you want to do, write about that.  

    If you have no idea at all what you want to do; write "We need help and guidance in choosing a
    project topic."
  
3.  If you do have a project topic in mind, think though the steps you'd need to take to go from a starting
    point, to a finished product.  Try to identify at least three separate stages.   Having more stages is good, 
    to certain point.  (Rule of thumb: five is about right.  Seven to eight is ok. More than twelve, and you are probably getting too detailed in the planning, too soon.)

    Put this in a section called `# Stages`.    Stages should be identifiable steps where you have something
    that works.  For example, for the doomsday clock listed above, here are four initial stages.
    
    ```
    Stage 1: Get a single seven segment display to count down from 9 to 0, one second at a time, then repeat that sequence.
    
    Stage 2: Get two seven segment displays to count down from 59 to 0, one second at a time, then repeat that sequence.
    
    Stage 3: Get two seven segment displays to count down from the first number in a list of integers in our Python
    code, instead of always starting at 59.
    
    Stage 4: Get some same displays to countdown from the first number in the list, then when they reach zero, count down from the next number in the list, and so on, until the list is done.
    
    etc...
    ```
    
    There is more detail about how to come up with good stages below.
    
    
    
# About your stages

The short version: 
* Make the early ones easy to acheive
* Realize that you might not get all the way to the final stage during SPIS
* So, to the extent possible, make each stage something you could demo independently

The longer version:

A key thing about these stages: if possible, they should start from scratch, and lead all the way to the project
you want to build.   But, given that the time is short, a really GOOD feature of your list of stages would be this,
especially for the later stages in the list:  that if you reached *that* stage, but fell short of completing every
stage on your list, you could still show SOMETHING in the Project Showcase.
    
That is, you could say: "Our goal is to build this doomsday clock.  When finished, it would ... blah blah blah.  We
didn't get all the way there, but we did get this far.  See how cool this is!"
    
For a data mining project, you might have wanted to get data about some particular topic you are interested in, say,
the most common words in reviews of Ukulele's, and how they are correlated with the reviewer's age.  In the end, you might not be able to locate data on Ukulele's, but perhaps you are able to produce similar data about some other 
product.  Or, you are able to at least get the five most common words in Ukulele reviews, that are NOT common in 
reviews of Guitars.  
    
