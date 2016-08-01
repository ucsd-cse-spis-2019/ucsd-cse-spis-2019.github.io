---
topic: Picobot
desc: "A web-based robot simulator"
---

The learning goals associated with this lab and milestone project are the following:

* Reason about the behavior of a simulated robot in a simple state-machine language
* Methodically trace the execution of a simple state-machine program
* Find and fix errors in a simple state-machine program
* Write a program to control a simulated robot so that it navigates through both an empty world and a maze environment
* Save and submit your files for feedback

The basic end-goals for this part of the lab are (and remember, these are minimal goals, eager for extensions):

* Write a program that directs your robot, Picobot, to completely "cover" (i.e., visit all the non-wall spaces) first an empty room, and then a maze.  

# Picobot Simulator: Feel free to jump right in...

Once you have logged on to your account on a terminal in the computer lab and managed to open a web browser (which we assume you have done if you are reading this), you are ready to dive into Picobot. You may already feel comfortable with Picobot from the exercises we did in the interactive portion of this lab.  If that's the case and you're ready to start writing your code, you can jump right to the Picobot simulator and start writing programs:

[Click here for the Picobot simulator and GET STARTED](https://www.cs.hmc.edu/picobot/)!

Again, your goals are to write a program to cover the empty room and the maze.  Feel free to play around for a while--playing around is often the best way to get going.  But many people eventually find this frustrating and crave a deeper understanding of what's going on.  Furthermore,  it is an important skill not only to solve the problems, but to understand exactly why your solution works.  So once you've gotten your feet wet playing around, please move on to the next section.


Here are some steps we suggest to help you get the most out of your Picobot experience.  Even if you've solved the two main goals, you should at least skim the section below to make sure your understanding is as deep as it can be.  Also there are some fun challenge problems in step 5.

Read [Chapter 1.2 of the book CS for All](https://www.cs.hmc.edu/csforall/Introduction/Introduction.html#picobot).  You are welcome to read the first part of the book as well, but it won't help you that much with Picobot, at least not directly. 

As you read, make sure you can answer the following questions.  Discuss the answers with your partner.  Ask a tutor if you're stuck or want to check your answers:

Sections 1.2.1-1.2.3: 

* Draw the environments for the following descriptions: xxWx, NxWS

Sections 1.2.4-1.2.6:

* Describe the following rules in English:

```
	0 N*x* --> W 0
	1 x**x --> N 2
```
* What is the difference between the "*" and the "x" in the description of Picobot's surroundings?

* Write a Picobot rule that would cause Picobot to crash into a wall (Picobot will report an error if you try this)
* In the Picobot simulator, modify the starting rules so that Picobot moves from East to West instead of from North to South.
* In the Picobot simulator, what will happen if we replace the "X"s in the second and fourth starting rule with a W.  First try to predict, and then run the simulation to see what happens.
* When you are finished reading (or even before you finish), solve the empty room problem.  That is, write a Picobot program to make Picobot visit every cell in the empty room, no matter where it starts.  Here are some hints to get you started:
As you saw if you answered the last question above, simply changing the X's to W's gets you a good part of the way there.  But there are some problems.  The first is that Picobot crashes into walls.  Picbobot should only be allowed to move West if there is no wall to the West.  Modify the existing rules so that Picobot moves West whenever it is against a N or S wall and there is no wall to the west.
Now Picobot successfully covers the room to the West of where it started, but it gets stuck when it reaches either the NW or SW corner, because it doesn't have a rule that applies to this surrounding.  You'll need to add one.  However, before you do, you should think carefully about your algorithm.  What is it that you want Picobot to do when it reaches the NW or SW corner?  One option is to immediately head all the way east, and then start moving N, S and W again as it was doing before.  Another option is to begin a N, S, and E sweep back the other way.  Either way you are going to need at least one new state.  We encourage you to think carefully about what this state or states will mean before you start implementing rules. 
Before continuing, save your code for the empty room solution. 

Finally, once you have successfully covered the use the empty room, use the MAP "-->" button to find the maze, and implement the maze covering program using the "right hand rule" as described in the book in Section 1.2.8.  Again, we provide some hints to get you started:

Think carefully about your states.  You will likely want to use 4 where each state represents a different direction that you are currently moving.  

Consider carefully which wall your hand will be on if you are heading in each direction, and this will help you figure out which direction to move, and when to change states.  For example, if you are heading north, your hand is on the east wall.  So as long as there is a wall to your east, and no wall to the north, you keep going north,  dragging your hand on the wall.  If the wall to the east suddenly disappears, then you turn in that direction to follow the wall.  If you suddenly hit a wall to the north, then your hand sweeps around the corner between the eastern and northern walls and you turn in the process so that you are facing west and your hand is now on the northern wall.  Make sure you understand ALL of the possible turns and transitions before you start writing rules.  If anything is unclear, ask a tutor.  We repeat: do not write rules until you have a firm understanding of what each state means, and how different environments affect your direction and forward progress.  It's all about keeping your right hand on the wall...
Before continuing, save your code for the maze solution.  You can use the same file you started below to save solutions for multiple rooms. 

When you've mastered the maze and you're ready for more, try these SUPER-challenge problems:
* for the empty room, see if you can use only 6 rules 
* for the empty room, can you build a machine that covers each cell in the room exactly once? 
* for the maze, see if you can use only 8 rules 

Scroll through the different maps and see if you can write Picobot programs to solve these other rooms.  Can you write a single program that works for ALL provided mazes?
Continuing with the Roomba vacuum cleaner analogy, you might know that the edges of a room get dirtier than the middle of the room (dust kicked up accumulates near the walls).  Can you program Picobot to cover the cells that are adjacent to walls at least twice and cover interior cells exactly once?  Can you formulate other criteria you might want to solve?  Are there unsolvable requirements?

Submit your code using the following table

```
# Filename: PicobotMaze
# Name 1  :
# PID 1   :
# Name 2  :
# PID 2   :
# Date    : 08/xx/2016

==========Room 1==========
#Put your code below for Room 1


==========Room 2 (The Maze) ==========
#Put your code below for Room 2

# Add headers for any additional code you want to add to this file
```

Fill in the template with your information (names/PIDs/Date)

You can include solutions to multiple problems in the same file, as shown in the template you copied.  Each solution should be labelled with a description of the room it is solving and have empty space above and below it (to separate it from other solutions).

