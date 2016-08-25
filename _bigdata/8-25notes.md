
---
topic: "Notes from 8/25 "
desc: " Sentiment Analysis"
---

```python
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:/Users/mizej/Desktop/Movies_TV_50000.py =============
Reading Data...
done
>>> data[0]
{'reviewerID': 'ADZPIG9QOCDG5', 'asin': '0005019281', 'reviewerName': 'Alice L. Larson "alice-loves-books"', 'helpful': [0, 0], 'unixReviewTime': 1203984000, 'reviewText': 'This is a charming version of the classic Dicken\'s tale.  Henry Winkler makes a good showing as the "Scrooge" character.  Even though you know what will happen this version has enough of a change to make it better that average.  If you love A Christmas Carol in any version, then you will love this.', 'overall': 4.0, 'reviewTime': '02 26, 2008', 'summary': 'good version of a classic'}
>>> d = data[0]['reviewText']
>>> d
'This is a charming version of the classic Dicken\'s tale.  Henry Winkler makes a good showing as the "Scrooge" character.  Even though you know what will happen this version has enough of a change to make it better that average.  If you love A Christmas Carol in any version, then you will love this.'
>>> d.split()
['This', 'is', 'a', 'charming', 'version', 'of', 'the', 'classic', "Dicken's", 'tale.', 'Henry', 'Winkler', 'makes', 'a', 'good', 'showing', 'as', 'the', '"Scrooge"', 'character.', 'Even', 'though', 'you', 'know', 'what', 'will', 'happen', 'this', 'version', 'has', 'enough', 'of', 'a', 'change', 'to', 'make', 'it', 'better', 'that', 'average.', 'If', 'you', 'love', 'A', 'Christmas', 'Carol', 'in', 'any', 'version,', 'then', 'you', 'will', 'love', 'this.']
>>> d
'This is a charming version of the classic Dicken\'s tale.  Henry Winkler makes a good showing as the "Scrooge" character.  Even though you know what will happen this version has enough of a change to make it better that average.  If you love A Christmas Carol in any version, then you will love this.'
>>> import string
>>> string.puncuation

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    string.puncuation
AttributeError: 'module' object has no attribute 'puncuation'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> dchar = [c for c in d]
>>> dchar
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'c', 'h', 'a', 'r', 'm', 'i', 'n', 'g', ' ', 'v', 'e', 'r', 's', 'i', 'o', 'n', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'c', 'l', 'a', 's', 's', 'i', 'c', ' ', 'D', 'i', 'c', 'k', 'e', 'n', "'", 's', ' ', 't', 'a', 'l', 'e', '.', ' ', ' ', 'H', 'e', 'n', 'r', 'y', ' ', 'W', 'i', 'n', 'k', 'l', 'e', 'r', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'a', ' ', 'g', 'o', 'o', 'd', ' ', 's', 'h', 'o', 'w', 'i', 'n', 'g', ' ', 'a', 's', ' ', 't', 'h', 'e', ' ', '"', 'S', 'c', 'r', 'o', 'o', 'g', 'e', '"', ' ', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', '.', ' ', ' ', 'E', 'v', 'e', 'n', ' ', 't', 'h', 'o', 'u', 'g', 'h', ' ', 'y', 'o', 'u', ' ', 'k', 'n', 'o', 'w', ' ', 'w', 'h', 'a', 't', ' ', 'w', 'i', 'l', 'l', ' ', 'h', 'a', 'p', 'p', 'e', 'n', ' ', 't', 'h', 'i', 's', ' ', 'v', 'e', 'r', 's', 'i', 'o', 'n', ' ', 'h', 'a', 's', ' ', 'e', 'n', 'o', 'u', 'g', 'h', ' ', 'o', 'f', ' ', 'a', ' ', 'c', 'h', 'a', 'n', 'g', 'e', ' ', 't', 'o', ' ', 'm', 'a', 'k', 'e', ' ', 'i', 't', ' ', 'b', 'e', 't', 't', 'e', 'r', ' ', 't', 'h', 'a', 't', ' ', 'a', 'v', 'e', 'r', 'a', 'g', 'e', '.', ' ', ' ', 'I', 'f', ' ', 'y', 'o', 'u', ' ', 'l', 'o', 'v', 'e', ' ', 'A', ' ', 'C', 'h', 'r', 'i', 's', 't', 'm', 'a', 's', ' ', 'C', 'a', 'r', 'o', 'l', ' ', 'i', 'n', ' ', 'a', 'n', 'y', ' ', 'v', 'e', 'r', 's', 'i', 'o', 'n', ',', ' ', 't', 'h', 'e', 'n', ' ', 'y', 'o', 'u', ' ', 'w', 'i', 'l', 'l', ' ', 'l', 'o', 'v', 'e', ' ', 't', 'h', 'i', 's', '.']
>>> dchar = [c in dchar if c not in string.punctuation]
SyntaxError: invalid syntax
>>> dchar = [c for c in dchar if c not in string.punctuation]
>>> dchar
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'c', 'h', 'a', 'r', 'm', 'i', 'n', 'g', ' ', 'v', 'e', 'r', 's', 'i', 'o', 'n', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'c', 'l', 'a', 's', 's', 'i', 'c', ' ', 'D', 'i', 'c', 'k', 'e', 'n', 's', ' ', 't', 'a', 'l', 'e', ' ', ' ', 'H', 'e', 'n', 'r', 'y', ' ', 'W', 'i', 'n', 'k', 'l', 'e', 'r', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'a', ' ', 'g', 'o', 'o', 'd', ' ', 's', 'h', 'o', 'w', 'i', 'n', 'g', ' ', 'a', 's', ' ', 't', 'h', 'e', ' ', 'S', 'c', 'r', 'o', 'o', 'g', 'e', ' ', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', ' ', ' ', 'E', 'v', 'e', 'n', ' ', 't', 'h', 'o', 'u', 'g', 'h', ' ', 'y', 'o', 'u', ' ', 'k', 'n', 'o', 'w', ' ', 'w', 'h', 'a', 't', ' ', 'w', 'i', 'l', 'l', ' ', 'h', 'a', 'p', 'p', 'e', 'n', ' ', 't', 'h', 'i', 's', ' ', 'v', 'e', 'r', 's', 'i', 'o', 'n', ' ', 'h', 'a', 's', ' ', 'e', 'n', 'o', 'u', 'g', 'h', ' ', 'o', 'f', ' ', 'a', ' ', 'c', 'h', 'a', 'n', 'g', 'e', ' ', 't', 'o', ' ', 'm', 'a', 'k', 'e', ' ', 'i', 't', ' ', 'b', 'e', 't', 't', 'e', 'r', ' ', 't', 'h', 'a', 't', ' ', 'a', 'v', 'e', 'r', 'a', 'g', 'e', ' ', ' ', 'I', 'f', ' ', 'y', 'o', 'u', ' ', 'l', 'o', 'v', 'e', ' ', 'A', ' ', 'C', 'h', 'r', 'i', 's', 't', 'm', 'a', 's', ' ', 'C', 'a', 'r', 'o', 'l', ' ', 'i', 'n', ' ', 'a', 'n', 'y', ' ', 'v', 'e', 'r', 's', 'i', 'o', 'n', ' ', 't', 'h', 'e', 'n', ' ', 'y', 'o', 'u', ' ', 'w', 'i', 'l', 'l', ' ', 'l', 'o', 'v', 'e', ' ', 't', 'h', 'i', 's']
>>> dnopunct = ''.join(dchar)
>>> dnopunct
'This is a charming version of the classic Dickens tale  Henry Winkler makes a good showing as the Scrooge character  Even though you know what will happen this version has enough of a change to make it better that average  If you love A Christmas Carol in any version then you will love this'
>>> dnopunct.lower()
'this is a charming version of the classic dickens tale  henry winkler makes a good showing as the scrooge character  even though you know what will happen this version has enough of a change to make it better that average  if you love a christmas carol in any version then you will love this'
>>> dlower = dnopunct.lower()
>>> dlower.split()
['this', 'is', 'a', 'charming', 'version', 'of', 'the', 'classic', 'dickens', 'tale', 'henry', 'winkler', 'makes', 'a', 'good', 'showing', 'as', 'the', 'scrooge', 'character', 'even', 'though', 'you', 'know', 'what', 'will', 'happen', 'this', 'version', 'has', 'enough', 'of', 'a', 'change', 'to', 'make', 'it', 'better', 'that', 'average', 'if', 'you', 'love', 'a', 'christmas', 'carol', 'in', 'any', 'version', 'then', 'you', 'will', 'love', 'this']
>>> def text_to_wordlist(text):
    r = [c for c in text if c not in set(string.punctuation)]
    rs = ''.join(r)
    rs = rs.lower()
    rs = rs.split()
    return rs

>>> d
'This is a charming version of the classic Dicken\'s tale.  Henry Winkler makes a good showing as the "Scrooge" character.  Even though you know what will happen this version has enough of a change to make it better that average.  If you love A Christmas Carol in any version, then you will love this.'
>>> text_to_wordlist(d)
['this', 'is', 'a', 'charming', 'version', 'of', 'the', 'classic', 'dickens', 'tale', 'henry', 'winkler', 'makes', 'a', 'good', 'showing', 'as', 'the', 'scrooge', 'character', 'even', 'though', 'you', 'know', 'what', 'will', 'happen', 'this', 'version', 'has', 'enough', 'of', 'a', 'change', 'to', 'make', 'it', 'better', 'that', 'average', 'if', 'you', 'love', 'a', 'christmas', 'carol', 'in', 'any', 'version', 'then', 'you', 'will', 'love', 'this']
>>> from collections import defaultdict
>>> wordCountDict = defaultdict(int)
>>> for d in data:
	for w in text_to_wordlist(d['reviewText']):
		wordCountDict[w]+=1

		

>>> len(wordCountDict)
202026
>>> wordCounts = [[wordCountDict[w],w] for w in wordCountDict]
>>> wordCounts[:5]
[[1, 'unsupportable'], [6, 'nunnery'], [1, 'woodi'], [3, 'sowell'], [182, 'woods']]
>>> wordCounts.sort()
>>> wordCounts[:5]
[[1, '00'], [1, '000315'], [1, '000602'], [1, '000614'], [1, '000825']]
>>> wordCounts.reverse()
>>> wordCounts[:5]
[[496867, 'the'], [254009, 'and'], [235885, 'a'], [224679, 'of'], [192257, 'to']]
>>> words = [w[1] for w in wordCounts[:1000]]
>>> words[:10]
['the', 'and', 'a', 'of', 'to', 'is', 'in', 'this', 'it', 'i']
>>> wordId = dict(zip(words,range(1000)))
>>> A = [1,2,3]
>>> B = [5,6,7]
>>> zip(A,B)
[(1, 5), (2, 6), (3, 7)]
>>> def feature(datum):
  feat = [0]*len(words)
  r = text_to_wordlist(datum)
  for w in r:
    if w in words:
      feat[wordId[w]] += 1
  feat.append(1) #offset
  return feat

>>> X = [feature(d['reviewText']) for d in data]
>>> y = [d['overall'] for d in data]
>>> import numpy
>>> theta,_,_,_ = numpy.linalg.lstsq(X,y)
>>> wordweights[[theta[i],words[i] for i in range(1000)]
	    
SyntaxError: invalid syntax
>>> wordweights=[[theta[i],words[i]] for i in range(1000)]
>>> wordweights.sort()
>>> wordweights.reverse()
>>> wordweights[:10]
[[0.17936618556966349, 'awesome'], [0.17645190435105107, 'outstanding'], [0.17405696524999012, 'loved'], [0.17350444320438663, 'superb'], [0.16999763840852897, 'amazing'], [0.16323958122094959, 'excellent'], [0.14129910179357458, 'glad'], [0.13803331270677463, 'favorite'], [0.13714608399282527, 'critics'], [0.13484471290859981, 'fantastic']]
>>> wordweights[-10:]
[[-0.19856690945920391, 'disappointed'], [-0.21230646260597483, 'decent'], [-0.21991702923490369, 'unfortunately'], [-0.24764425637082099, 'ok'], [-0.26099105302122694, 'poor'], [-0.28511346652585789, 'worse'], [-0.35994954704270427, 'terrible'], [-0.40532995585999865, 'stupid'], [-0.63523389403412811, 'worst'], [-0.64042258728037915, 'boring']]
>>> def dot(v,w):
	return sum(v_i*w_i for v_i,w_i in zip(v,w))

>>> testdata = data[189]
>>> testdatafeat = feature(text_to_wordlist(testdata['reviewText']))
>>> testdata
{'reviewerID': 'A1W584W9UW3XEU', 'asin': '0005119367', 'reviewerName': 'strega2 "strega2"', 'helpful': [13, 13], 'unixReviewTime': 906768000, 'reviewText': "TNT has put together a surprisingly good account of the Biblical story of  Joseph, betrayed into slavery in Egypt by his jealous brothers.  Martin  Landau as Jacob and Ben Kingsley as Potiphar give their usual first-rate  performances, with the role of Joseph also well-acted.  Leslie-Anne Warren is  the lustful wife of Potiphar, who unsuccessfully tries to seduce Joseph,  and lands him in the Pharoah's prison.  This film offers a very credible  depiction of life in the ancient Near East, from the desert tents of the  Hebrews, to the claustrophobic walled towns like Sichem, to the lushness of  civilized Egypt and the Pharoah's court. The film is faithful to the  Biblical account, and succeeds in making it come alive on the screen.  A  well-acted, well-scripted, and entertaining film.  END", 'overall': 5.0, 'reviewTime': '09 26, 1998', 'summary': 'A very entertaining Bible epic'}
>>> testdata['reviewText']
"TNT has put together a surprisingly good account of the Biblical story of  Joseph, betrayed into slavery in Egypt by his jealous brothers.  Martin  Landau as Jacob and Ben Kingsley as Potiphar give their usual first-rate  performances, with the role of Joseph also well-acted.  Leslie-Anne Warren is  the lustful wife of Potiphar, who unsuccessfully tries to seduce Joseph,  and lands him in the Pharoah's prison.  This film offers a very credible  depiction of life in the ancient Near East, from the desert tents of the  Hebrews, to the claustrophobic walled towns like Sichem, to the lushness of  civilized Egypt and the Pharoah's court. The film is faithful to the  Biblical account, and succeeds in making it come alive on the screen.  A  well-acted, well-scripted, and entertaining film.  END"
>>> testdatafeat
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
>>> testdatafeat = feature(testdata['reviewText'])
>>> testdatafeat
[13, 5, 3, 7, 4, 2, 4, 1, 1, 0, 0, 2, 0, 0, 1, 0, 3, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
>>> dot(testdatafeat,theta)
4.1524419522788083
>>> testdata['overall']
5.0
>>> testdata
{'reviewerID': 'A1W584W9UW3XEU', 'asin': '0005119367', 'reviewerName': 'strega2 "strega2"', 'helpful': [13, 13], 'unixReviewTime': 906768000, 'reviewText': "TNT has put together a surprisingly good account of the Biblical story of  Joseph, betrayed into slavery in Egypt by his jealous brothers.  Martin  Landau as Jacob and Ben Kingsley as Potiphar give their usual first-rate  performances, with the role of Joseph also well-acted.  Leslie-Anne Warren is  the lustful wife of Potiphar, who unsuccessfully tries to seduce Joseph,  and lands him in the Pharoah's prison.  This film offers a very credible  depiction of life in the ancient Near East, from the desert tents of the  Hebrews, to the claustrophobic walled towns like Sichem, to the lushness of  civilized Egypt and the Pharoah's court. The film is faithful to the  Biblical account, and succeeds in making it come alive on the screen.  A  well-acted, well-scripted, and entertaining film.  END", 'overall': 5.0, 'reviewTime': '09 26, 1998', 'summary': 'A very entertaining Bible epic'}
>>> testdata = data[10009]
>>> tdfeature = feature(testdata['reviewText'])
>>> dot(tdfeature,theta)
4.5767911886114323
>>> testdata['overall']
4.0
>>> testdata['asin']
'0767809688'
>>> 
```
