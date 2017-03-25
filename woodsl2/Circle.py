'''
The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter, and the user
can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

        Compute the circle’s area
        Print the circle and get something nice
        Be able to add two circles together
        Be able to compare two circles to see which is bigger
        Be able to compare to see if there are equal
        (follows from above) be able to put them in a list and sort them



'''

import math

def main():
Radius = 0
Diameter = 0
Circumference = 0
Area = 0


Radius = GetRadius(Radius)
Diameter = SetDiameter(Radius, Diameter)
Circumference = SetCircumference(Radius, Circumference)
Area = SetArea(Radius, Area)
ShowResults(Radius, Diameter, Circumference, Area)


def GetRadius(radius):
radius = float(str(input("Enter your radius: ")))
return radius

def SetDiameter(radius, diameter):
diameter = radius * 2
return diameter

def SetCircumference(radius, circumference):
PIE = 3.14159
circumference = 2 * PIE * radius
return circumference

def SetArea(radius, area):
PIE = 3.14159
myarea = PIE * radius * radius
return area

def ShowResults(Radius, Diameter, Circumference, Area):
print("The Diameter is",mydiameter)
print("The Circumference is",circumference)
print("The Area is",myarea)

main()
