import math
from PIL import Image

def find(theList, item):
    if theList == []:
        return False
    elif theList[0] == item:
        return True
    else:
        return find(theList[1:], item)

def deepFind(theList, item):
    if type(theList)!=type([]):
        return item==theList
    elif theList == []:
        return False
    else:
        return deepFind(theList[0], item) or deepFind(theList[1:], item)

def powerSet(theList):
    if theList == []:
        return [[]]
    else:
        restPSet = powerSet(theList[1:])
        return restPSet + addOneToEach(restPSet, theList[0])

def addOneToEach(listOfLists, item):
    if listOfLists == []:
        return []
    else:
        return [[item] + listOfLists[0]] + addOneToEach(listOfLists[1:], item)

def knapsack(limit, items):
    if limit < 0:  # illegal state --> big penalty
        return -math.inf
    if items == []: # No more items so no value
        return 0
    useFirst = items[0][1] + knapsack(limit-items[0][0], items[1:])
    loseFirst = knapsack(limit, items[1:])
    return max(useFirst, loseFirst)

def getPathCost(pic, x, y):
    ''' Get the cost of the minimum energy path from x, y to the
        top of the image pic '''
    w = pic.size[0]
    if y == 0:
        return getEnergy(pic, x, y)
    # explore 3 paths
    best = math.inf
    for xnew in [x-1, x, x+1]:
        if xnew >=0 and xnew < w:
            energy = getPathCost(pic, xnew, y-1)
            if energy < best:
                best = energy
    return best+getEnergy(pic, x, y)

def getPathCostTable(pic):
    table = []
    for y in range(pic.size[1]):
        nextRow = []
        for x in range(pic.size[0]):
            if y == 0:
                nextRow+=[getEnergy(pic, x, y)]
            else:
                lastRow = table[y-1]
                best = math.inf
                for xnew in [x-1, x, x+1]:
                    if xnew >= 0 and xnew < pic.size[0]:
                        if lastRow[xnew] < best:
                            best = lastRow[xnew]
                nextRow+=[getEnergy(pic, x, y)+best]
        table+=[nextRow]
    return table

def getPathCostDP(pic, x, y):
    table = getPathCostTable(pic)
    return table[y][x]
    
def getEnergy(pic, x, y):
    ''' get the energy of the pixel at x, y in pic.  The energy is defined as
        energy = abs(i(x+1), y)-i(x, y)) + abs(i(x, y+1)-i(x,y)) '''
    (w, h) = pic.size
    if x < w-1:
        xval = grayscale(pic.getpixel((x+1, y)))
    else:
        xval = grayscale(pic.getpixel((x-1, y)))
    if y < h-1:
        yval = grayscale(pic.getpixel((x, y+1)))
    else:
        yval = grayscale(pic.getpixel((x, y-1)))
    pixval = grayscale(pic.getpixel((x, y)))
    return abs(xval-pixval)+ abs(yval-pixval)

def grayscale(rgb):
    return (rgb[0]+rgb[1]+rgb[2])//3

def printGrayscale(pic):
    ret = ""
    for y in range(pic.size[1]):
        for x in range(pic.size[0]):
            ret += str(grayscale(pic.getpixel((x, y))))+" "
        ret+= "\n"
    print(ret)

def printEnergy(pic):
    ret = ""
    for y in range(pic.size[1]):
        for x in range(pic.size[0]):
            ret += str(getEnergy(pic, x, y))+" "
        ret += "\n"
    print(ret)
