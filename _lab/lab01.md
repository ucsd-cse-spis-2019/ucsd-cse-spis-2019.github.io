---
layout: lab
num: lab01
ready: true
desc: "Picobot"
assigned: 2019-08-06 08:30:00.00-7
due: 2019-08-08 17:00:00.00-7
---

## Learning Goals

* Reason about the behavior of a simulated robot in a simple state-machine language
* Methodically trace the execution of a simple state-machine program
* Work with a partner using pair programming
* Find and fix errors in a simple state-machine program
* Write a program to control a simulated robot so that it navigates through both an empty world and a maze environment
* Save and submit your files for feedback

The main goals for this part of the lab are (and remember, these are minimal goals, eager for extensions):

* Write a program that directs your robot, Picobot, to completely "cover" (i.e., visit all the non-wall spaces of) an empty room
* Write a program to do the same for a maze

## Pair Programming

During SPIS, most of your lab assignments will use *Pair Programming*. This is a system where two people collaborate on a single solution to a coding problem. When doing pair programming, you will work side-by-side with your partner, and share a single workstation. 

In this system, you have two different roles, and you will alternate between them. These roles are being the "driver" and being the "navigator". The "driver" is the one typing, and the "navigator" provides guidance to the driver as to what to do.

Please take a moment to visit this link and learn more about [Pair Programming](/topics/pair_programming/).

To "learn the do’s and don’ts" of pair programming and to see pairs in action, you may also want to check out this entertaining (if a bit corny/cheesey) video about pair programming from North Carolina State University: [An Introduction to Pair Programming for Students](https://www.youtube.com/watch?v=rG_U12uqRhE).

In this lab, you will first do some coding **individually**. But just as in the previous lab, work next to your partner and help each other. Then, after you have each become familiar with the basics of picobot and have finished the first introductory assignment, you will switch to **pair programming** for the remainder of the lab.


# Individual: Picobot bouncing off the walls

This first part of the lab is individual, so you need your own workstation. However, work next to your partner, and support each other. Make sure you are both finished with this individual part and comfortable with picobot before moving on to the pair programming portion of the lab. Don't rush each other. It is okay to take your time. If you help each other, don't share answers, but explain principles and clear up misconceptions. 


## Getting started: the Picobot simulator

Now, let's get going with Picobot. Fist, log into a computer, and open a web browser. 

For a resource on Picobot, check out **[Chapter 1.2 of the book CS for All](https://www.cs.hmc.edu/twiki/bin/view/CSforAll/)** or its [pdf version](http://www.cs.bc.edu/~muller/teaching/cs101/s13/dist/docs/HMCS5book.pdf).  BTW, this is just one of the chapters of the online textbook we recommend as your go-to resource for your journey throughout SPIS. But if you are eager to get started, and we hope you are, you can focus on this chapter on picobot first.

Based on the information in this *CS for All* chapter or what you learned in class, try to answer the following questions for yourself. If you are not sure, feel free to discuss with your partner or a mentor. You don't need to submit these answers, but make sure you are able to formulate an answer for yourself. Confer with your partner to see if they are thinking the same.


1. Describe the following rule in English:

	```
	1 x**x --> N 2
	```
2. What is the difference between the "*" and the "x" in the description of Picobot's surroundings?

3. Write a single Picobot rule that would cause Picobot to go W and crash into a wall (Picobot will report an error if you try this)


Now, let's start writing a simple Picobot program.
[Right click here for the Picobot simulator and GET STARTED](https://www.cs.hmc.edu/picobot/)!


Start out by looking at the starting rules that are given to you when you first get to the simulator site. Can you figure out what Picobot will do when you enter these default rules? 
Run the code and verify your answer. Is it doing what you expect it to do? If not, make sure you understand why before moving on. It is an important skill not only to solve problems, but to understand exactly why your solution works (or not).

Also, feel free to play around a bit and modify the starter code. This is a great way to get going. BTW, whenever you change the code, **make sure to click the *Enter rules for Picobot* button**. Otherwise, the changes are not registered and Picobot will simply execute the previous code, confusing you to no end most likely (as it did for us, when we forgot to do this :-) 


## Let's get coding

As a final task before moving on to the pair-programming parts of this lab, try to create the following program. Again, you can ask your partner or the mentors for advice and help, but make an effort to solve this alone. Of course. don't stay stuck and don't be afraid to ask for guidance, but don't ask for the answer. Ask for help in clearing up any concepts that trouble you, and get to the point where you can solve this problem yourself. We realize Picobot programs are not immediately intuitive, so don't worry if it takes you some time. This is natural.

The task is to have the picobot bounce off the walls going east-to-west and back. It should move west first until it hits the wall, then turn around and follow the same track east until it hits the wall, and then turn around and do the same thing again (always staying in the same row). Basically, Picobot should end up pinging back and forth, west to east and back, always using the same row.

Once **both you and your partner** are done with this and you both feel comfortable with Picobot, move on to the next section where you will work on problems together.



# Pair Programming: Solving the empty room and maze

For the remainder of the lab, you will be doing Pair Programmming. First, decide on who will be the inital "navigator" and who will be the initial "driver". Make sure you switch roles frequently, however, throughout this lab. 


## First steps

Create a new github repo under the "ucsd-cse-spis-2019" organization. Your github repo should be called spis19-lab01-Name1_Name2 (where Name1 and Name2 are the pair names). This was explained in lab00. Feel free to refer back to this lab if you forgot how to do this.

Then create two text files in your git repo: `emptyroom.txt` and `maze.txt`. These files will be used to submit your Picobot code for the empty room and maze exercises. See additional instructions in the subsequent sections. Ask for the mentors' help if you have any questions.



## Program Picobot to solve the empty room

Write a program to make Picobot visit every cell in the empty room, no matter where it starts.  This is the Picobot problem you see when you get to the Picobot landing page.

Hints to get you started: You both have a program to sweep the room left to right. Can you come up with a simple change to not always cover the same area, but also move north once you hit a wall. This will will get you a good part of the way there, covering (on average) half the room. But you will probably get stuck in a corner at the end. You'll need to add a rule to get you out of this situation and move you to the yet-uncovered part of the room. What would you do next? We encourage you to think carefully about what your states mean before you start implementing rules. This is true in general: think first, then code. Or as the meme goes "2 weeks of coding saved me 2 hours of planning".

Once you are finished with this problem, save your code for the empty room solution in the file `emptyroom.txt` in your git repo, before moving on to the next problem.


## Program Picobot to solve the maze

Once you have successfully covered the empty room, use the MAP "-->" button to find the maze, and implement the maze covering algorithm. Think carefully about your states.  You will likely want to use 4 states where each state represents a different direction that you are currently moving in.  

A good way to solve this kind of maze is by using the "right hand rule". Basically, the idea is best explained if you imagine you are Picobot and you have to go through this maze with your eyes closed (so you can only feel what is directly around you). If you would keep your right hand always to a wall on your right, and keep following that wall as it twists and turns through the maze, you will eventually cover the entire maze. Convince yourself that this is indeed true. Does this algorithm make sense? In what kind of maze would this break down? (Fortunately, we are given a maze where this idea will work).

Now, how can you implement this in Picobot? If you want, here are some hints to get your started: Consider carefully which wall your hand will be on if you are heading in each direction, and this will help you figure out which direction to move, and when to change states.  For example, if you are heading north, your hand is on the east wall.  So as long as there is a wall to your east, and no wall to the north, you keep going north,  dragging your hand along the wall.  If the wall to the east suddenly disappears, then you turn in that direction to follow the wall. If you suddenly hit a wall to the north, then your hand sweeps around the corner between the eastern and northern walls and you turn in the process so that you are facing west and your hand is now on the northern wall.  Make sure you understand all of the possible turns and transitions before you start writing rules.  If anything is unclear, ask a tutor.  We repeat: do not write rules until you have a firm understanding of what each state means, and how different environments affect your direction and forward progress.  It's all about keeping your right hand on the wall ...

When you are done and have tested your solution thoroughly, save your code fin the file `maze.txt` in your github repo. 

Are you up for more? There are some fun challenge problems in the next section. You are highly encouraged to try these, but they are not required. 

BTW, the style of coding that Picobot uses is an example of finite state machines. We will explore it further later on in SPIS. The concept of state machines is particularly useful if you are interested in robotics, for example. However, many other applications use this style as well.


## Challenge problems

When you've mastered the maze and you're ready for more, try some optional challenge problems (some of these are super challenging). You don't need to submit these, but you could if you wanted to; just create additional files in your github repo with .txt endings, and put an explanation for each of those files in your README.md. 

For example, you could challenge yourself with some of the following problems:

* For the empty room, see if you can use only 6 rules. 

* For the maze, see if you can use only 8 rules. 

* Scroll through the different maps and see if you can write Picobot programs to solve these other rooms. 

* For the empty room, can you build a machine that covers each cell in the room exactly once? 

* In the Roomba vacuum cleaner analogy, you might know that the edges of a room get dirtier than the middle of the room (dust kicked up accumulates near the walls). Can you program Picobot to cover the cells that are adjacent to walls at least twice and cover interior cells exactly once? 

* Can you write a single program that works for ALL provided mazes?

* Can you formulate other criteria you might want to solve? Are there unsolvable requirements?

We hope you enjoyed these Picobot puzzels ...


