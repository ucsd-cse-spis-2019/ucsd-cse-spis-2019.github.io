---
topic: "Github: APS Writeups"
desc: "Using Github to write solutions to your APS homework"
---

During SPIS, you'll be given four APS problem sets: [APS1](/hwk/aps1/), [APS2](/hwk/aps2/), [APS3](/hwk/aps3/), and [APS4](/hwk/aps4/).

You can use github to create and submit your solutions to these problems.

One of the most basic ways to get started with using git and github is to simply create and edit files and directories directly at the github.com web page.

We'll invite you to use github.com to create, edit and submit your solutions to the APS Homework assignments.

To get started, create a private github repo under the ucsd-cse-spis-2018 organization that has this name:

* spis18-aps-yourfirstname-yourlastinitial

Use the names and initials from the [pairs list](/info/pairs/), which we have updated with the preferred first name you gave us on the github survey.  For example:

* spis18-aps-Lavanya-S
* spis18-aps-Njambi-N
* spis18-aps-Andrew-T
* spis18-aps-Anthony-V
* etc.

This image shows how to set up the repo at the [github.com/new](https://github.com/new) page:

![new aps repo](create-github-repo-for-spis-aps-50pct.png)

In this repository, we'll invite you to create files called `Week1.md`,
`Week2.md`, `Week3.md` and `Week4.md` for each of the four APS homework
assignments you'll complete during the SPIS Program. &nbsp;We'll
explain how to create each of those below.

# Creating `Week1.md`

To create `Week1.md`, click on the + sign at the location shown in the image below.

(Note: these images are from last year, so it shows 2015 instead of 2016.
But I'm sure you won't let that confuse you. :-) ).

Then enter the name `Week1.md`, and type the first line of your solution (basically, an introduction).

Finally, scroll down the web page, and find the button for "Commit New File".

<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickHereToCreateANewFile.png?attredirects=0" imageanchor="1"><img border="0" height="200" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickHereToCreateANewFile.png" width="400"></a>

<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/CreatingWeek1.png?attredirects=0" imageanchor="1" style="font-size:10pt"><img alt="type Week1.md in box and type first line of file content" border="0" height="189" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/CreatingWeek1.png" width="400"></a>

<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/Screen%20Shot%202015-08-10%20at%204.13.10%20PM.png?attredirects=0" imageanchor="1"><img alt="click here to commit a new file" border="0" height="225" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/Screen%20Shot%202015-08-10%20at%204.13.10%20PM.png" width="320"></a>

## Editing the Week1.md file

You should then be able to click on your Week1.md file and see the content in the github.com webpage, as shown in the examples below.

You can click the pencil icon to make further edits.

<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickWeek1.md.to.see.the.file.you.created.png?attredirects=0" imageanchor="1"><img alt="click Week1.md to see the file you created" border="0" height="300" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickWeek1.md.to.see.the.file.you.created.png" width="400"></a>

<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickThePencilIconToMakeFurtherEdits.png?attredirects=0" imageanchor="1" style="font-size:10pt"><img border="0" height="186" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickThePencilIconToMakeFurtherEdits.png" width="400"></a>

## Editing a Markdown File

In the github.com interface, any filename that ends with .md is treated as a "Markdown" file. 

Markdown is a way of formatting text for web pages that is designed to be than HTML (HTML is a "Markup" language—"Markdown" is a pun on "Markup".)

For the most part, in a Markdown file, you just type normal text, leaving a blank line between paragraphs. &nbsp;

There are a few special characters though. &nbsp;This is not a complete list&mdash;these are just a few examples.


<table border="1" bordercolor="#888" cellspacing="0" style="border-collapse:collapse;border-color:rgb(136,136,136);border-width:1px">
<tbody>
<tr>
<td>&nbsp;<b>What you want to do<span>&nbsp;&nbsp; &nbsp;<span>&nbsp;&nbsp; &nbsp;</span></span></b></td>
<td><b>&nbsp;How you type it</b><span><b>&nbsp;&nbsp; &nbsp;</b><span>&nbsp; &nbsp;</span></span></td>
</tr>
<tr>
<td>&nbsp;Headings
</td>
<td><code># This is a heading</code></td>
</tr>
<tr>
<td>&nbsp;Make some <b>bold</b> text</td>
<td>&nbsp;<code>Make some **bold** text</code></td>
</tr>
<tr>
<td>&nbsp;Make some italic text</td>
<td>&nbsp;<code>Make some *italic* text</code></td>
</tr>
<tr>
<td>&nbsp;Insert the lowercase greek letter α</td>
<td>&nbsp;<code>Insert the greek letter &amp;alpha;</code></td>
</tr>
<tr>
<td>&nbsp;Insert the capital greek letter Φ</td>
<td>&nbsp;<code>Insert the capital greek letter &amp;Phi;</code></td>
</tr>
<tr>
<td>&nbsp;Use superscript to show x<sup>2</sup></td>
<td>&nbsp;<code>Use superscript to show x&lt;sup&gt;2&lt;/sup&gt;</code></td>
</tr>
<tr>
<td>&nbsp;Use subscript for x<sub>i</sub></td>
<td>&nbsp;<code>Use subscript to show x&lt;sub&gt;i&lt;/sub&gt;</code></td>
</tr>
</tbody>
</table>

To see if your text is being formatted the way you want before you save, you can switch back and forth between: <b>Edit</b> and <b>Preview Changes:</b>

<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/switchBetweenEditAndPreviewChanges.png?attredirects=0" imageanchor="1"><img alt="edit and preview changes" border="0" height="145" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/switchBetweenEditAndPreviewChanges.png" width="400"></a>


<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickPreviewChanges.png?attredirects=0" imageanchor="1"><img alt="click preview changes to see how changes will look" border="0" height="166" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickPreviewChanges.png" width="400"></a>

To save those changes, click Commit:

<a href="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickCommitChangesToSaveYourWork.png?attredirects=0" imageanchor="1"><img alt="click commit to save your work" border="0" height="352" src="https://sites.google.com/a/eng.ucsd.edu/spis/home/2015_academicprogram/foundations/git-resources/git-aps-writeups/clickCommitChangesToSaveYourWork.png" width="400"></a>


## What can you do in a Markdown file?


Suppose you want a bullet list such as this one:


* First you do this.
* Then you do that.
* Then, finally you do something else.

You can make that by formatting it with stars in place of the bullets. &nbsp; (Don't leave blank spaces at the start of a line though, or it will look like code; the star followed by a space should be the first thing on the line.)

```
* First you do this.
* Then you do that.
* Then, finally you do something else.
```

You can learn a lot more about the things you can do in Markdown here
at this guide:

[https://help.github.com/articles/markdown-basics/](https://help.github.com/articles/markdown-basics/)


## Suppose I want a picture

If you want an image, as long as it is already on the web, its
easy. Just paste in the URL of the image, and it will appear in the
Markdown file as an image.

As an example, suppose you are solving an APS problem related to making change, and you want to include a diagram that shows two nickels (5 cent coins) and three pennies (1 cent coins).  You might want this picture to be in your Markdown file:

<img src="https://docs.google.com/drawings/d/1ylTKc_xZq4Zq982vhqlbZ03vA3I-5rIcw5-SdCx43-w/pub?w=867&amp;h=278">

Maybe you already have that picture on the web somewhere. Or maybe you draw it on paper, take a picture with your phone, and upload that .jpg or .png file into your github repo.  Then linking to it works just like the way we linked to your photo in [lab00](/lab/lab00/).

But, if you don't already have a picture, one easy way to create one is with Google Drawings, as explained here: [Github: Google Drawings in Markdown files](/topics/github_google_drawings/).

<div style="display:none;">https://ucsd-cse-spis-2018.github.io/topics/github_aps_writeups/</div>
