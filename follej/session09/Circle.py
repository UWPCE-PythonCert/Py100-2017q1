from math import pi, sqrt


class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @staticmethod
    def radius_to_area(radius):
        return pi * radius ** 2

    @staticmethod
    def radius_to_perimeter(radius):
        return pi * radius * 2

    @property
    def area(self):
        return Circle.radius_to_area(self.radius)

    @property
    def perimeter(self):
        return pi * Circle.radius_to_perimeter(self.radius)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @classmethod
    def from_area(cls, area):
        return cls(sqrt(area / pi))

    def __str__(self):
        return "Circle with radius {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        if (self.radius - other.radius) > 0:
            return Circle(self.radius - other.radius)
        else:
            raise AttributeError('Circle radius total must be greater than zero')

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other

    def __le__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other

    def __ge__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other

    def __ne__(self, other):
        return self.radius != other

    def __iadd__(self, other):
        return Circle.__add__(self, other)

    def __imul__(self, other):
        return Circle.__mul__(self, other)

# my_circle = Circle(5)
# my_circle.area = 42
# print(my_circle)
# # print(my_circle.radius)
# # my_circle.radius=5
# print(my_circle.radius)
# my_circle.from_diameter(20)
# print(my_circle.radius)
# print(my_circle.diameter)
