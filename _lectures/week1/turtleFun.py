import turtle

def simpleTurtleFun():
    turtle.forward(100)
    turtle.right(90)
    turtle.backward(200)
    #print(turtle.position())

def twoTurtleFun():
    ''' Doc string '''
    firstTurtle = turtle.Turtle()
    secondTurtle = turtle.Turtle()
    firstTurtle.forward(100)
    secondTurtle.right(90)
    secondTurtle.backward(200)

def assignmentChallenge():
    maria = turtle.Turtle()
    jose = turtle.Turtle()
    maria.penup()
    jose.penup()
    maria.setpos(-100, 0)
    jose.setpos(-100, -50)
    maria.pendown()
    jose.pendown()
    maria = jose
    dist1 = 100
    dist2 = 200
    dist1 = dist2
    dist2 += 150
    maria.forward(dist1)
    jose.forward(dist2)

def drawShape(theTurtle):
    ''' Draw a simple shape with the turtle passed in '''
    theTurtle.forward(100)
    theTurtle.right(90)
    theTurtle.forward(100)
    theTurtle.right(90)
    theTurtle.forward(100)
    theTurtle.right(90)
    theTurtle.forward(100)
    theTurtle.right(90)

def drawShapeWithLists(theTurtle):
    sideLengths = [100, 200, 50, 200]
    angles = [90, 120, 40, 60]
    index = 0
    theTurtle.forward(sideLengths[index])
    theTurtle.right(angles[index])
    index += 1
    theTurtle.forward(sideLengths[index])
    theTurtle.right(angles[index])
    index += 1
    theTurtle.forward(sideLengths[index])
    theTurtle.right(angles[index])
    index += 1
    theTurtle.forward(sideLengths[index])
    theTurtle.right(angles[index])

def drawShapeWithATuple(theTurtle):
    len_angle = (100, 90)
    theTurtle.forward(len_angle[0])
    theTurtle.right(len_angle[1])
    theTurtle.forward(len_angle[0])
    theTurtle.right(len_angle[1])
    theTurtle.forward(len_angle[0])
    theTurtle.right(len_angle[1])
    theTurtle.forward(len_angle[0])
    theTurtle.right(len_angle[1])

def drawShapeWithListAndTuple(theTurtle):
    sides = [(100, 60), (200, 120), (100, 60), (200, 120)]
    side = sides[0]
    theTurtle.forward(side[0])
    theTurtle.right(side[1])
    side = sides[1]
    theTurtle.forward(side[0])
    theTurtle.right(side[1])
    side = sides[2]
    theTurtle.forward(side[0])
    theTurtle.right(side[1])
    side = sides[3]
    theTurtle.forward(side[0])
    theTurtle.right(side[1])

def drawShapeWithLoop(theTurtle):
    sides = [(100, 60), (200, 120), (100, 60), (200, 120)]
    for side in sides:
        theTurtle.forward(side[0])
        theTurtle.right(side[1])
        
  
#assignmentChallenge()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.penup()
turtle1.setpos(200, 200)
turtle1.pendown()
#drawShape(turtle1)
#drawShape(turtle2)
drawShapeWithListAndTuple(turtle1)
drawShapeWithLoop(turtle2)
