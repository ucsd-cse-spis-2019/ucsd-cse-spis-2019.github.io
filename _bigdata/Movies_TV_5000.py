
import urllib

def parseData(fname):
    for l in urllib.urlopen(fname):
        yield eval(l)

print "Reading Data..."
gen = parseData("http://cses.ucsd.edu/spis/reviews_CDs_and_Vinyl_5.json")
data = []
for i in range(5000):
  data.append(gen.next())
print "done"
