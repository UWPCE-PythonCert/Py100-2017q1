from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self._diameter = self.radius * 2

    @property
    def the_radius(self):
        return self.radius

    @property
    def the_diameter(self):
        return self._diameter

    @the_diameter.setter
    def the_diameter(self, diameter):
        self._diameter = diameter
        self.radius = diameter/2

    @property
    def the_area(self):
        return pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        cls._diameter = diameter
        cls.radius = diameter/2
        print("area of the circle is: {}".format(pi * cls.radius**2))

    def __str__(self):
        return "Your circle's area: {}\nYour circle's diameter: {}" \
               "\nYour circle's radius: {}".format(self.the_area,self.the_diameter, self.the_radius)

    def __repr__(self):
        return 'Circle(%s)' % self.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __sub__(self, other):
        return self.radius - other.radius

    def __mul__(self, other):
        return self.radius * other.radius

    def __floordiv__(self, other):
        return self.radius // other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius


def main():
    print(Circle(4))

if __name__ == "__main__":
    main()


