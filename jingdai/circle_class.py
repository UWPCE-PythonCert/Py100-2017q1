from math import pi

class Circle (object):

    def __init__(self, radius=0):
        self._radius=radius

    @property
    def radius(self):
        self._radius
        print("Radius is: {}".format(self._radius))

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Negative radius is not possible")
        print("Setting value")
        self._radius = value

    @property
    def diameter(self):
        self._radius*2
        print("Diameter is: {}".format(self._radius*2))

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError("Negative diameter is not possible")
        print("Setting value")
        self._diameter = value
        self._radius=value/2

    @property
    def area(self):
        area=pi*self._radius**2
        print("Area is: {:.2f}".format(area))

    #Add an “alternate constructor” that lets the user create a Circle directly with the diameter
    @classmethod
    def from_diameter(cls,value):
        return cls(value/2)

    def __str__(self):
        str(self._radius)
        return "Circle with radius: {}".format(str(self._radius))

    #not sure
    def __repr__(self):
         return repr("Circle({})".format(str(self._radius)))

    def __add__(self, other):
        total_radius=self._radius +other._radius
        return Circle(total_radius)

    def __mul__(self, other):
        total_radius=self._radius *other._radius
        return Circle(total_radius)

    def __eq__(self, other):
        return self._radius== other._radius

    def __lt__(self, other):
        return self._radius < other._radius



#SmallCircle is to test inheitance
# try use super() , does not necessarily need __init__, also use **kwargs
class SmallCircle(Circle):
    def __init__(self, radius):
        self._radius=radius
        print("SmallCircle radius is {}".format(self._radius))


if __name__ == "__main__":
    c=Circle(90)
    c1=Circle(50)
    print(c<c1)
    circles=[Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    print(circles)



    #s=SmallCircle(99)
    #s.radius
    #s.diameter



