def silly(x, y):
    """ returns x-y """
    return x-y


def greeting(personToGreet):
    """ prints a friendly greeting """
    print("Hello " + str(personToGreet))
    print("Welcome to SPIS!")

def greetingReturn(personToGreet):
    """ prints a friendly greeting """
    print("Hello " + str(personToGreet))
    return("Welcome to SPIS!")

def isHurricane(windSpeed):
   ''' Determine if the windSpeed is strong enough to make it a hurricane'''
   if windSpeed >= 74:
      hurricane = True
      print("There is a hurricane!")
   else:
      hurricane = False
      print("Don't panic.  It's not a hurricane")
   return hurricane

def isHurricane2(windSpeed):
   ''' Determine if the windSpeed is strong enough for a hurricane'''
   if windSpeed >= 74:
      hurricane = True
      print("There is a hurricane!")
   if windSpeed >= 157:
      hurricane = True
      print("It's a category 5!")
   else:
      hurricane = False
   return hurricane

def isHurricane3(windSpeed):
    ''' Determine if the windSpeed is strong enough to make it a hurricane'''
    if windSpeed >= 74 and windSpeed < 96:
        hurricane = True
        print("There is a category 1 hurricane")
    elif windSpeed >= 96 and windSpeed < 111:
        hurricane = True
        print("There is a category 2 hurricane")
    else:
        hurricane = False
    return hurricane
   


