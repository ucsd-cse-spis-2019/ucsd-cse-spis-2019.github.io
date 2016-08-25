

import urllib

def parseData(fname):
    for l in urllib.urlopen(fname):
        yield eval(l)

print "Reading Data..."
gen = parseData("http://cses.ucsd.edu/spis/reviews_Movies_and_TV_5.json")
data = []
for i in range(500):
  data.append(gen.next())
print "done"
