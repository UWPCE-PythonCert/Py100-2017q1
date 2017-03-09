from math import pi, sqrt


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @staticmethod
    def radius_to_area(radius):
        return pi * radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    @classmethod
    def from_area(cls, area):
        return cls(sqrt(area/pi))

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

#  print(Circle.radius_to_area(1))
c = Circle.from_diameter(8)
print(c.diameter)
print(c.radius)



