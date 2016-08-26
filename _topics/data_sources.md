---
topic: "Data Sources"
desc: "sources of interesting data to use in your projects"
---

# Data Sources

This page describes several places where you might look for interesting data to use in your SPIS projects.

Here is an overview, followed by more specific information about each one.

* Julian McAuley's Amazon Data sets: [http://jmcauley.ucsd.edu/data/amazon/](http://jmcauley.ucsd.edu/data/amazon/)
* The CORGIS datasets for Python: [https://think.cs.vt.edu/corgis/python/index.html](https://think.cs.vt.edu/corgis/python/index.html) 
    * CORGIS is a <b>C</b>ollection <b>o</b>f <b>R</b>eally <b>G</b>reat, <b>I</b>nteresting, <b>S</b>ituated Datasets, collected by Austin Cory Bart, a Ph.D. student in Computer Science Education at Virginia Tech (along with several other collaborators.)
    * The datasets are updated periodically, and cover many topics from Art, Economics, Geography, History, Literature, Music, Politics, and Travel among others.   There are over 40 datasets that come with Python code to access them.  
    * Many of these datasets are of sufficient size to be considered "big data", but only if you are careful about setting
       the `test=False` parameter.  Read the documentation for each data set carefully.  More info below.
* New York Times Data Journalism: [http://www.nytimes.com/section/upshot](http://www.nytimes.com/section/upshot)
* Nate Silver's Election analysis and more: [http://fivethirtyeight.com/](http://fivethirtyeight.com/)
* JavaScript Library for Data Manipulation: [https://d3js.org](https://d3js.org)


# Working with Reddit Data

* Reddit Data Visualization: [https://www.reddit.com/r/dataisbeautiful/](https://www.reddit.com/r/dataisbeautiful/)
* Articles from SPIS 2016 website that relate to getting Reddit Data:
    * [Python: JSON](https://ucsd-cse-spis-2016.github.io/topics/python_JSON/)  About JSON in Python in general, but uses
        data from Reddit as an example.
    * [Python: Requests: User-Agent](/topics/python-requests-user-agent.md) A general article about setting the `User-Agent` to
        avoid problems when accessing web content from Python, but uses Reddit as an example.

# Corgis datasets for Python

When working with the Corgis datasets for Python, be sure to read the part about the `test=False` parameter.


For many of these datasets, you only get a small sample of the data when you use this code:

```Python
import cars
list_of_car = cars.get_cars()
list_of_car = cars.get_cars_by_year("2001")
list_of_car = cars.get_cars_by_make("'Pontiac'")
```

If instead, you set the `test` parameter to `False`, you get a much larger data set that could be considered "big data":

```Python
import cars
# These may be slow!
import cars
# These may be slow!
list_of_car = cars.get_cars(test=False)
list_of_car = cars.get_cars_by_year("2001", test=False)
list_of_car = cars.get_cars_by_make("'Pontiac'", test=False)
```

