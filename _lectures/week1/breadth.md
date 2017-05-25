---
lecture_date: "2016-08-05 09:00:00.00-7:00"
topic: "Week 1: Breadth"
desc: "A second look at data mining and intro to list comprehension"
week: "1"
indent: true
link_topic_desc_only: true
ready: false
---

# Breadth lecture from 08/05: Miles

A second look at the Data Mining code from Julian McAuley's Facet's presentation.

* <http://jmcauley.ucsd.edu/data/spis.py>
* <http://jmcauley.ucsd.edu/data/amazon/>
* [Breadth Lecture slides (miles)](/_lectures/week1/Breadth week 1.pdf)

# Complete Code from Julian's lecture

```python
import numpy
import urllib
import scipy.optimize
import random

def parseData(fname):
  for l in urllib.urlopen(fname):
    yield eval(l)

print "Reading data..."
data = list(parseData("http://jmcauley.ucsd.edu/cse255/data/beer/beer_50000.json"))
print "done"

def feature(datum):
  feat = [1]
  return feat

X = [feature(d) for d in data]
y = [d['review/overall'] for d in data]
theta,residuals,rank,s = numpy.linalg.lstsq(X, y)

### Convince ourselves that basic linear algebra operations yield the same answer ###

X = numpy.matrix(X)
y = numpy.matrix(y)
numpy.linalg.inv(X.T * X) * X.T * y.T

### Do older people rate beer more highly? ###

data2 = [d for d in data if d.has_key('user/ageInSeconds')]

def feature(datum):
  feat = [1]
  feat.append(datum['user/ageInSeconds'])
  return feat

X = [feature(d) for d in data2]
y = [d['review/overall'] for d in data2]
theta,residuals,rank,s = numpy.linalg.lstsq(X, y)

### How much do women prefer beer over men? ###

data2 = [d for d in data if d.has_key('user/gender')]

def feature(datum):
  feat = [1]
  if datum['user/gender'] == "Male":
    feat.append(0)
  else:
    feat.append(1)
  return feat

X = [feature(d) for d in data2]
y = [d['review/overall'] for d in data2]
theta,residuals,rank,s = numpy.linalg.lstsq(X, y)

### Gradient descent ###

# Objective
def f(theta, X, y, lam):
  theta = numpy.matrix(theta).T
  X = numpy.matrix(X)
  y = numpy.matrix(y).T
  diff = X*theta - y
  diffSq = diff.T*diff
  diffSqReg = diffSq / len(X) + lam*(theta.T*theta)
  print "offset =", diffSqReg.flatten().tolist()
  return diffSqReg.flatten().tolist()[0]

# Derivative
def fprime(theta, X, y, lam):
  theta = numpy.matrix(theta).T
  X = numpy.matrix(X)
  y = numpy.matrix(y).T
  diff = X*theta - y
  res = 2*X.T*diff / len(X) + 2*lam*theta
  print "gradient =", numpy.array(res.flatten().tolist()[0])
  return numpy.array(res.flatten().tolist()[0])

scipy.optimize.fmin_l_bfgs_b(f, [0,0], fprime, args = (X, y, 0.1))

### Random features ###

def feature(datum):
  return [random.random() for x in range(30)]

X = [feature(d) for d in data2]
y = [d['review/overall'] for d in data2]
theta,residuals,rank,s = numpy.linalg.lstsq(X, y)
```

# Generators

This piece of Julian McAuley's code is called a Generator.  The Guttag textbook discusses generators in (insert section here.)

```python
def parseData(fname):
  for l in urllib.urlopen(fname):
    yield eval(l)
```
#Incomplete code from Miles's Lecture

```python
Reading data...
done
>>> len(data)
50000
>>> data[0]
{'beer/style': 'Hefeweizen', 'beer/ABV': 5.0, 'beer/beerId': '47986', 'review/timeStruct': {'wday': 0, 'isdst': 0, 'mday': 16, 'hour': 20, 'min': 57, 'sec': 3, 'year': 2009, 'yday': 47, 'mon': 2}, 'review/aroma': 2.0, 'review/appearance': 2.5, 'review/timeUnix': 1234817823, 'review/palate': 1.5, 'review/taste': 1.5, 'beer/name': 'Sausa Weizen', 'beer/brewerId': '10325', 'review/overall': 1.5, 'review/text': 'A lot of foam. But a lot.\tIn the smell some banana, and then lactic and tart. Not a good start.\tQuite dark orange in color, with a lively carbonation (now visible, under the foam).\tAgain tending to lactic sourness.\tSame for the taste. With some yeast and banana.', 'user/profileName': 'stcules'}
>>> X=[[1] for i in data]
>>> len(X)
50000
>>> X[0]
[1]
>>> X[4000]
[1]
>>> y = [d['review/overall'] for d in data]
>>> len(y)
50000
>>> y[0]
1.5
>>> sum(y)/len(y)
3.88871
>>> def predictor(user):
	return 3.8871

>>> numpy.linalg.lstsq(X, y)
(array([ 3.88871]), array([ 24621.476795]), 1, array([ 223.60679775]))
>>> X = [38, 57, 56, 65, 45, 66, 58, 62, 64, 92, 73, 87, 59, 38, 39, 41]
>>> y = [11.5, 13.0, 13.0, 13.0, 14.0, 13.0, 13.5, 13.0, 14.0, 14.5, 15.0, 14.0, 14.0, 13.5, 13.0, 12.0]
>>> import matplotlib.pyplot as plt
>>> Xage = [[1,age] for age in X]
>>> Xage
[[1, 38], [1, 57], [1, 56], [1, 65], [1, 45], [1, 66], [1, 58], [1, 62], [1, 64], [1, 92], [1, 73], [1, 87], [1, 59], [1, 38], [1, 39], [1, 41]]
>>> numpy.linalg.lstsq(X, y)

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    numpy.linalg.lstsq(X, y)
  File "C:\Python27\lib\site-packages\numpy\linalg\linalg.py", line 1874, in lstsq
    _assertRank2(a, b)
  File "C:\Python27\lib\site-packages\numpy\linalg\linalg.py", line 196, in _assertRank2
    'two-dimensional' % len(a.shape))
LinAlgError: 1-dimensional array given. Array must be two-dimensional
>>> numpy.linalg.lstsq(Xage, y)
(array([ 11.37165876,   0.03409943]), array([ 7.09542843]), 2, array([ 243.39868301,    1.03976349]))
>>> plt.scatter(X,y)
<matplotlib.collections.PathCollection object at 0x000000002571EA58>
>>> plt.plot([0.03409943*i+11.37165876 for i in range(100)])
[<matplotlib.lines.Line2D object at 0x00000000253C5AC8>]
>>> plt.show()
>>> Xage2 = [[age] for age in X]
>>> Xage2
[[38], [57], [56], [65], [45], [66], [58], [62], [64], [92], [73], [87], [59], [38], [39], [41]]
>>> numpy.linalg.lstsq(Xage2, y)
(array([ 0.21457756]), array([ 146.93373067]), 1, array([ 243.36803406]))
>>> plt.scatter(X,y)
<matplotlib.collections.PathCollection object at 0x0000000025A3E080>
>>> plt.plot([0.03409943*i+11.37165876 for i in range(100)])
[<matplotlib.lines.Line2D object at 0x00000000257DB748>]
>>> plt.plot([0.21457756*i for i in range(100)])
[<matplotlib.lines.Line2D object at 0x0000000025A3EEF0>]
>>> plt.show()
>>> Xagequad = [[1,age,age**2] for age in X]
>>> Xagequad
[[1, 38, 1444], [1, 57, 3249], [1, 56, 3136], [1, 65, 4225], [1, 45, 2025], [1, 66, 4356], [1, 58, 3364], [1, 62, 3844], [1, 64, 4096], [1, 92, 8464], [1, 73, 5329], [1, 87, 7569], [1, 59, 3481], [1, 38, 1444], [1, 39, 1521], [1, 41, 1681]]
>>> numpy.linalg.lstsq(Xagequad, y)
(array([  1.09319699e+01,   4.92152494e-02,  -1.21122663e-04]), array([ 7.07563947]), 3, array([  1.68225040e+04,   5.71681893e+01,   3.05628422e-01]))
>>> plt.plot([-1.21122663e-04*i**2+4.92152494e-02*i+1.09319699e+01 for i in range(100)])
[<matplotlib.lines.Line2D object at 0x00000000285E9E48>]
>>> plt.scatter(X,y)
<matplotlib.collections.PathCollection object at 0x00000000285F7080>
>>> plt.show()
```
