---
topic: "Github: Google Drawing images in Markdown files"
desc: "e.g. for diagrams in your APS Solutions"
---

# Suppose I want a picture in a Markdown file

Suppose you are doing your APS homework, and you want to put a diagram
in your solution to illustrate your point.

If you have an image that is already on the web, it's easy.  Just 
paste the URL into your document, and the image will show up.

But if your image isn't already on the web, here's how to create one
with Google Drawings and publish it.

As an example, suppose you are solving an APS problem related to making change, and you want to include a diagram that shows two nickels (5 cent coins) and three pennies (1 cent coins).  You might create this picture:

<img src="https://docs.google.com/drawings/d/1ylTKc_xZq4Zq982vhqlbZ03vA3I-5rIcw5-SdCx43-w/pub?w=867&amp;h=278">

To create this with Google Drawings:

1. Open [drive.google.com](https://drive.google.com) in a web browser.  You may need to create a Google Account if you do     not already have one.    

2.  Select the option, as shown here, to create a new drawing:  ![Google Drive New Drawing](new-google-drawing-50.png)

3.  Edit the Google Drawing and give it a name.   This [Google Drawings Help Article](https://support.google.com/docs/topic/1360903?hl=en&ref_topic=1397170) has more information if you need help on using Google Drawings to create your picture.

4.  When the picture looks like you want it to, select "Publish to the web", as shown here: ![Publish Google Drawing to the web](google-drawings-publish-to-the-web-50.png)
5.  Adjust the size if needed, click to Publish, then select Embed, as shown here:
6.  Copy the entire `<img ... >` element and copy/paste it into your Markdown document (e.g. `README.md`, `Week1.md`, etc.)

You should then see the picture in your document.  If you don't like the size, go back and choose a different size, and publish it again.  You may need to recopy the `<img ... >` element.

<div style="display:none;">https://ucsd-cse-spis-2016.github.io/topics/github_google_drawings/</div>

