---
layout: lab
num: lab08
ready: false
desc: "Basics of electronics with Rapsberry Pi, by Diba"
assigned: 2016-08-17 09:30:00.00-7
due: 2016-08-19 15:45:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza

# Learning objectives

In this lab you will be introduced to the basics of electronics using a a credit-card sized computer called the Raspberry Pi (yummy!). You will build simple electronic circuits and write programs to control them. 

# Getting started

## Create a git repo
Use your laptop to create a new repo called `spis16-lab07-part1-Name-Name`. 
Note that you must keep your git repo updated with your latest code because your code will be erased from the Pi at the end of the lab to ensure that the hardware is ready for use by the next group.

## Observe your Raspberry Pi
Take a look at the Raspberry Pi on your workbench. You are looking at the insides of a computer. The Pi is not shy about exposing its true self. You would see a similar circuit if you cracked open the shiny shell of your laptop (which is probably not a great idea to quench your curiosity). As you stare down at your Pi, you see an all-encompassing circuit. Your gut feeling may be that it all looks very complex. Your premonitions are not misplaced. The circuit that you are looking at is not called the motherboard for nothing! 

The green base on which all the electronic components (which you see as bulgy entities) are laid out is a non-conductive substrate. This means that the green parts of the board don’t conduct electricity. However, to connect the various electrical components, conductive tracks made of copper are etched on the green base. At the very center of your Pi sits a prominent black square block. This is the brain of your Pi – the processor. But the processor is not the only thing on the black square. It is clubbed with some Random Access Memory (RAM).  For now, just know that the RAM is a form of non-persistent memory. There are other components on the Pi. To identify them orient your Pi to match the circuit below.

<p align="center">
![RPi-1-modelB](/lab/images/RPi/RPi1_modelB.png){:height="200px"} 
</p>

A corresponding functional diagram of the Pi is also shown below:


<p align="center">
![RPi-1-labeled](/lab/images/RPi/RPi-diagram.png){:height="200px"} 
</p>


Observe the components marked in the diagram (above) on your Pi. 
We will focus on a few important components on the diagram:

1. Ethernet port: The Pi can get Internet connectivity through the Ethernet port, marked as LAN or through a WiFi dongle connected to one of its USB ports. In our setup, we will use the WiFi.

2. High Definition Multimedia Interface (HDMI): This is an interface that connects your Pi to a monitor.

3. SD card slot: All the software that runs on the Pi, which includes the Operating System (more on the OS later) as well as your programs, will be stored on the SD card that goes into the SD card slot. The Pi without the SD card is all hardware.

4. GPIO pins: These pins can be configured to send/receive signals through your python programs. You will control and sense the world around you through these pins!!

5.	Power Input: Using this input you can power up your Pi using a charger or a batteries. 

In the setup provided to you, the Pi has been wired to work as a desktop computer!
Next week we will operate it in a untethered fashion (as a robot) but for now observe the following three wired connections from the Pi to other peripherals:

* The Pi is connected to a monitor via the HDMI port.
* The keyboard and mouse are connected to the in-built USB hub of your monitor. A single USB cable from the monitor connects the keyboard and mouse to the Pi.
* The Pi is powered up using a charger that is plugged into the wall.

## Getting to know your desktop environment

<p align="center">
![RPi-desktop](/lab/images/RPi/RPi-desktop.png){:height="400px"} 
</p>

The operating system on the Pi is a version of the linux known as Raspbian. The picture above shows the Raspbian desktop environment. Like Windows, or OS X (for Apple), you can run programs by double clicking them. Feel free to poke around and see what all of these icons mean! We will use two main programs on your desktop: the Wifi config tool and the LXTerminal.


### The WiFi config tool
This tool shows the status of your Wifi connection and internet connectivity.
Use the mouse navigate to the WiFi Config Tool on your desktop. Double click on it to view the status of your network connection. Take note of the IP address in the GUI of that tool. Your IP address is of the form: 137.110.XX.XX. If you see such a number then you have internet connectivity. You can use the IP to remotely access your Pi from any other computer using ssh (just like how you log into the ieng6 machines, more on this later)

### LXTerminal
LXTerminal is the command line interpreter. Double click on the icon to open it.
When you open LXTerminal notice the prompt says `pi@spispi-XX`. This means that you are user `pi` and the name of your machine is `spispi-XX`.
All the unix commands that you have learned so far can be used to navigate through the file system on your Pi. You can also use command line git just like how you would on the ieng6 machines!





