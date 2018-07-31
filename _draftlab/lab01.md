---
layout: lab
num: lab01
ready: true
desc: "Picobot"
assigned: 2017-08-08 08:30:00.00-7
due: 2017-08-10 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza



# Learning Goals

* Reason about the behavior of a simulated robot in a simple state-machine language
* Methodically trace the execution of a simple state-machine program
* Find and fix errors in a simple state-machine program
* Write a program to control a simulated robot so that it navigates through both an empty world and a maze environment
* Save and submit your files for feedback

The main goals for this part of the lab are (and remember, these are minimal goals, eager for extensions):

* Write a program that directs your robot, Picobot, to completely "cover" (i.e., visit all the non-wall spaces) an empty room
* Write a program to do the same for a maze

## First steps

* Create a new github repo under the "ucsd-cse-spis-2017" organization. Your github repo should be called spis17-lab01-Name1_Name2 (where Name1 and Name2 are the pair names). 

* Create three text files in your git repo: `answers.txt`, `emptyroom.txt` and `maze.txt`. The file `answers.txt` should contain your answers to all the questions in the following section. `emptyroom.txt` and `maze.txt` should contain your Picobot code for the empty room and maze exercises. See additional instructions in the subsequent sections.


## Picobot Simulator: Feel free to jump right in...

Once you have logged on to your account on a terminal in the computer lab and managed to open a web browser (which we assume you have done if you are reading this), you are ready to dive into Picobot. You may already feel comfortable with Picobot from the exercises we did in the interactive portion of this lab.  If that's the case and you're ready to start writing your code, you can jump right to the Picobot simulator and start writing programs:

[Right click here for the Picobot simulator and GET STARTED](https://www.cs.hmc.edu/picobot/)!

Again, your goals are to write a program to cover the empty room and the maze.  Feel free to play around for a while--playing around is often the best way to get going.  But many people eventually find this frustrating and crave a deeper understanding of what's going on.  Furthermore,  it is an important skill not only to solve the problems, but to understand exactly why your solution works.  So once you've gotten your feet wet playing around, please move on to the next section.


Here are some steps we suggest to help you get the most out of your Picobot experience.  Even if you've solved the two main goals, you should at least skim the section below to make sure your understanding is as deep as it can be.  Also there are some fun challenge problems in step 5.

**Read [Chapter 1.2 of the book CS for All](https://www.cs.hmc.edu/csforall/Introduction/Introduction.html#picobot).**  You are welcome to read the first part of the book as well, but it won't help you that much with Picobot, at least not directly. 

As you read, make sure you can answer the following questions.  Discuss the answers with your partner.  Ask a tutor if you're stuck or want to check your answers. Put your answers to the following questions in the `answers.txt` file in your git repo. Commit your file to submit your answers.


1. Describe the following rules in English:

	```
	0 N*x* --> W 0
	1 x**x --> N 2
	```
2. What is the difference between the "*" and the "x" in the description of Picobot's surroundings?

3. Write a Picobot rule that would cause Picobot to crash into a wall (Picobot will report an error if you try this)

4. In the Picobot simulator, what will happen if we replace the "X" in the fourth (i.e., last) starting rule with a W.  First try to predict, and then run the simulation to see what happens.

5. In the Picobot simulator, modify the starting rules so that Picobot moves from East to West instead of from North to South.



## Program Picobot to solve the empty room

Write a Picobot program to make Picobot visit every cell in the empty room, no matter where it starts.  Hints to get you started:
As you saw if you answered question 4 above, a simple change gets you a good part of the way there, covering half the room.
But you'll probably notice picobot gets stuck when it reaches the NW or SW corner, because it doesn't have a rule that applies to this surrounding.  You'll need to add one.  However, before you do, you should think carefully about your algorithm.  What is it that you want Picobot to do when it reaches one of those corners?  One option is to immediately head to the east wall, and then start moving N, S and W as it was doing before.  Another option is to begin a N, S, and E sweep back the other way.  Either way you are going to need **at least one** new state.  We encourage you to think carefully about what this state or states will mean before you start implementing rules. 
Once you are finished with this problem, save your code for the empty room solution in the file `emptyroom.txt` in your git repo, before moving on to the next problem. 

## Program Picobot to solve the maze

Finally, once you have successfully covered the empty room, use the MAP "-->" button to find the maze, and implement the maze covering program using the "right hand rule" as described in the **book in Section 1.2.8**.  Again, we provide some hints to get you started:

Think carefully about your states.  You will likely want to use 4 states where each state represents a different direction that you are currently moving.  

Consider carefully which wall your hand will be on if you are heading in each direction, and this will help you figure out which direction to move, and when to change states.  For example, if you are heading north, your hand is on the east wall.  So as long as there is a wall to your east, and no wall to the north, you keep going north,  dragging your hand on the wall.  If the wall to the east suddenly disappears, then you turn in that direction to follow the wall. If you suddenly hit a wall to the north, then your hand sweeps around the corner between the eastern and northern walls and you turn in the process so that you are facing west and your hand is now on the northern wall.  Make sure you understand ALL of the possible turns and transitions before you start writing rules.  If anything is unclear, ask a tutor.  We repeat: do not write rules until you have a firm understanding of what each state means, and how different environments affect your direction and forward progress.  It's all about keeping your right hand on the wall...
Before continuing, save your code for the maze solution in the file `maze.txt` in your github repo.  You can use the same file to solve the maze for multiple rooms. 

## SUPER-challenge problems

When you've mastered the maze and you're ready for more, try some optional SUPER-challenge problems. You don't need to submit these. For example, you could challenge yourself with the following problems:

* for the empty room, see if you can use only 6 rules 

* for the empty room, can you build a machine that covers each cell in the room exactly once? 

* for the maze, see if you can use only 8 rules 

Scroll through the different maps and see if you can write Picobot programs to solve these other rooms. Can you write a single program that works for ALL provided mazes?
Continuing with the Roomba vacuum cleaner analogy, you might know that the edges of a room get dirtier than the middle of the room (dust kicked up accumulates near the walls). Can you program Picobot to cover the cells that are adjacent to walls at least twice and cover interior cells exactly once?  Can you formulate other criteria you might want to solve? Are there unsolvable requirements?

## Submitting your code

As stated before, please create a private github repo with the name spis17-lab01-pair1name-pair2name.

In the repo, create three files called answers.txt, emptyroom.txt and maze.txt

In each of these files, put your solution to the lab.

If you want to put in solutions to additional mazes:

* Create additional files with .txt endings

* Put explanation for each of those files in your README.md


