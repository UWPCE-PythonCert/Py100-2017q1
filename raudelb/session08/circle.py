import math

# NOTE: Testing is in circleTest.py


class Circle():
    radius = 0
    _diameter = 0

    def __init__(self, r=0):
        self.radius = r

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value/2

    @property
    def area(self):
        return math.pi*self.radius**2

    @classmethod
    def from_diameter(cls, value):
        cls.diameter = value
        cls.radius = cls.diameter/2
        return cls

    def __str__(self):
        return 'Circle with radius: %s' % self.radius

    def __repr__(self):
        return '%s(%d)' % (self.__class__.__name__, self.radius)

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, other):
        return self.radius * other

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

if __name__ == '__main__':

    c = Circle(4)
    print('Radius: ', c.radius)

    # Add a “diameter” property, so the user can get the diameter of the circle:

    print('Diameter: ', c.diameter)

    # Set up the diameter property so that the user can set the diameter of the circle:

    c = Circle(4)

    c.diameter = 2

    print('Diameter: ', c.diameter)
    print('Radius: ', c.radius)

    # Add an area property so the user can get the area of the circle:

    c = Circle(2)

    print('Area: ', c.area)

    # c.area = 42 # AttributeError: can't set attribute


    # Add an “alternate constructor” that lets the user create a Circle directly with the diameter:

    c = Circle.from_diameter(8)

    print('Diameter: ', c.diameter)
    print('Radius: ', c.radius)

    # Add __str__ and __repr__ methods to your Circle class.

    c = Circle(4)

    print(c)

    print(repr(c))

    d = eval(repr(c))

    print(d)

    # Add some of the numeric protocol to your Circle:

    c1 = Circle(2)
    c2 = Circle(4)

    print(c1 + c2)  # Circle(6)

    print(c2 * 3)

    # print(3 * c2)  # unsolved

    # add the ability to compare two circles:

    print(c1 > c2)

    print(c1 < c2)

    print(c1 == c2)

    c3 = Circle(4)

    print(c2 == c3)

    # Once the comparing is done, you should be able to sort a list of circles:

    circle = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3),
              Circle(5), Circle(9), Circle(1)]

    circle.sort()

    print(circle)

