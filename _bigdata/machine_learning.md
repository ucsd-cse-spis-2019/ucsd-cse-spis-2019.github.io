---
topic: "Collaborative Filtering "
desc: " A Quick Look at Stalking People Online"
---

<h1> Topics Covered in this DOPE GUIDE </h1>
Manhattan distance<br>
Euclidean distance<br>
Minkowski distance<br>
Pearson Correlation Coefficient<br>
Cosine similarity<br>
Implementing k-nearest neighbors in Python<br>

<h1> Now to get into some real cool stuff, familia </h1>
<img src='http://static1.zipso.net/wp-content/uploads/2014/03/doge-mining.jpg' style="width: 400px">
<p> A Data Mining Expert </p>

<h1> So what is Collaborative Filtering, anyway, other than "just a data mining technique"? </h1>

<p> A recommendation system wherein I collaborate with friends to filter out your online information for pertinent data and then use it to stalk your movements online. JKJKJKJKJKJKJK LMAO!!! </p>

<p> Collaborative Filtering is a recommendation system where I use people with similar interests to recommend some sort of data, like a movie. In this way, the data points in your set "collaborate" to produce some sort of prediction. Suppose I need to recommend you an album to listen to on Spotify: I would go through the other users on Spotify to find one that is similar to you in music tastes. Once I find this person, I can look at music that they listen to that you don't and recommend you those artists.</p>

<p> The following guide will go over some of those oh-so-sweet details on how this process works. </p>

<h1> BUT HOW DO WE MEASURE SIMILARITY BASED-GOD MAXWELL? </h1>
<h2> Manhattan Distance </h2>

<p> Imagine yourself and Harambe the gorilla, rating your preferences on different movies. Harambe, of course, rates Free Willy a 10/10 and rates Pulp Fiction a solid 8/10. You, on the other hand, rate Pulp Fiction a solid 10/10, and Free Willy a 3/10. What is the simplest manner in which we can measure your similarity to this majestic primitive? Distance. We would plot your opinions on Free Willy on the x axis, and your opinions on Pulp Fiction on the y axis, and then calculate how many blocks a cab driver in matthattan would have to move in order to get from Harambe to You.</p>

<p>| x1 - x2| + | y1 - y2 |</p>

<p>| 10 - 3 | + | 8 - 10 | = 9 </p>

<p> And so your manhattan distance from dank memes is a 9. Now lets talk about Rare Pepe's. Pepe rates Free Will a 0/10, and feels meh about Pulp Fiction, rating it a 7/10. His manhattan distance from you is therefore</p>

<p>| 3 - 0 | + | 10 - 7 | = 6 </p>

<p> Thus you are closer to Pepe than you are to Harambe. This is the simplest form of measuring similarity </p>

<h2> Euclidean Distance and the Illuminati </h2>

<p> So, everyone knows that the Illuminati are watching our every move, and to perfect the measure of similarity, they forced Pythagoras to churn out the Famous  triangular theorem, creating the concept of Euclidean Distance. You will hopefully have learned this in high school and I will be killed if I tell you more, but it is pretty straight forward that measuring the exact distance between two points will give you a slightly more accurate representation of similarity. Here's the equation: </p>

<p> sqrt( (x1 - x2)^2 + (y1 - y2)^2 ) </p> 

<h2> WE NEED TO GO DEEPER. </h2>

<h1> DEEPER. </h1>

<h1> WE MUST GO DEEPER INTO HIGHER DIMENSIONS. </h1>

<p> Thinking of how the concepts of Manhattan Distance and Euclidean Distance apply when we have ratings of more than one movie is relatively straight-forward. Instead of just x and y coordinates, we have x, y, and z, coordinates, a 3-D distance, and with four movies, we have x, y, z, and theta coordinates, and so forth. The associated measures of distance change intuitively. </p>

<p> Manhattan Distance becomes | x1 - x2 | + | y1 - y2 | + | z1 - z2 | + ... </p>

<p> Euclidean Distance becomes sqrt( (x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2 + ... ) </p>

<p> And boom, you're a space explorer mathmatician extrodinate working in 5 dimensional space. E. Z. P. Z. MIND FREKING BLOWN GAME OVER SHOW DONE WE"RE OUT OF HERE. BEAUTIFUL. AMAZING. 10/10 BEST NEW MATHEMATICAL CONCEPT. </p>

<img src='https://pbs.twimg.com/media/CbSoeXOVAAAkASg.png' style="width: 600px">

<h1> BUT WHAT IS WRONG WITH THIS PICTURE? </h1>

<h1> WAIT, NO, NOT THE PICTURE ABOVE. WHAT IS WRONG WITH THE METHODS OF CALCULATING EUCLIDEAN AND MANHATTAN DISTANCE? </h1>

<p> This one is a little bit harder to explain without giving a specific example. Imagine trying to apply these measurements of similarity when there are a large number of ratings. Users will have incredibly different overlaps. I might have rated 5 movies, and Harambe has rated the same five, while Pepe has rated two of the ones that I've rated and 3 movies that I have never seen. Now, when we try to draw a comparison between me, harambe, and Pepe, there may be a large skew in the results. My distance to harambe may be larger simply because of the larger number of dimensions between us, even if in reality we are closer. This, as well as many other problems, can arise. Bad news, and it is actively being researched as we speak. We will talk more about this later, hopefully, and adress ways in which his bias may be corrected. For now, let us discuss the generalized distance measurement (its really freaking cool, though the math is a little less intuitive.)</p>

<h1> NEVER PANIC </h1>

<p> Math is not for geniuses. Everything is generally understandable given enough time and experience. So don't panic. Good Will Hunting is a lie. Still, we will take it slow, but I promise that nothing in the following sections, and the rest of this book, will go unexplained. </p>

<h2> Now let's get to the good stuff, the Minkowski Distance Metric, this big boy. </h2>

<img src='http://i.stack.imgur.com/U6qGk.png' style="width: 600px">

<p> Note: If you have not encountered the notation above for dealing with series, heres a quick and easy explanation: <a href='https://www.youtube.com/watch?v=haK3oC0L_a8'> YouTube. </a> .  </p>

<p> So let's break it down. When p = 1, we have the manhattan distance: </p>

<img src='http://angiogenesis.dkfz.de/oncoexpress/software/cs_clust/dist_004.gif' style="width: 600px">

<p> And when p = 2, we've got Euclidean: </p>

<img src='http://mines.humanoriented.com/classes/2010/fall/csci568/portfolio_exports/lguo/image/euclidean_distance.jpg' style="width: 600px">

<p> And so we get a rough idea of what this formula is communicating. It is a generalization of different ways to 

