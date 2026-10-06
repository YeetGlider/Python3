def stringTest(word):
    if word.islower():
         return word.upper()
    else:
        return word.capitalize()
stringTest("test") #should return "TEST"
stringTest("NOW") #should return "Now"
stringTest("later") #should return "LATER"
stringTest("ToDay") #should return "Today"

#-------------------------------------------------------------------------------

def apCredit(credits):
    if credits < 24:
        return "Year 1"
    if credits >= 24:
        return "Year 2"

apCredit(24) #should return "Year 2"
apCredit(10) #should return "Year 1"
apCredit(26) #should return "Year 2"
apCredit(15) #should return "Year 1"

#-------------------------------------------------------------------------------

def proCredit(compsci, program):
    test1 = apCredit(compsci)
    if test1 == "Year 2":
        if program >= 12:
            return "CSE 116"
        else:
            return "CSE 115"
    else:
        return "No credit transfer."
    
proCredit(24, 12) #should return "CSE 116"
proCredit(24, 10)#should return "CSE 115"
proCredit(10, 15) #should return "No credit transfer.

#-----------------------------------------------------------------------------------
import math

def radCompare(radius):
    if radius >= 7:
        r = (radius ** 2)
        area = 3.14 * r
        area = round(area, 2)
        return area
    else:
        r = (radius ** 2)
        area = (math.pi) * r
        return round(area, 2)
        

radCompare(5) #should return 78.54.
radCompare(9) #should return 254.34.
radCompare(7) #should return 153.86.

#----------------------------------------------------------------------------------

def decideClothing(temp):
    if temp <= 32:
        return "Stay heated indoor"
    if 33 <= temp <= 54:
        return "Thermal layers for Winter"
    if 55 <= temp <= 67:
        return "Light sweaters for Spring"
    if 68 <= temp <= 70:
        return "Light vest for Fall"
    else:
        return "T-shirt for Summer"

decideClothing(79) #should return "T-shirt for Summer".
decideClothing(25) #should return "Stay heated indoor".
decideClothing(52) #should return "Thermal layers for Winter".
decideClothing(65) #should) return "Light sweaters for Spring".
decideClothing(68) #should) return "Light vest for Fall".
