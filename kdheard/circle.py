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


def main():
    c1 = Circle(2)
    c2 = Circle(4)
    print(c2//c1)

"""Unit tests"""


def test_radius():
    c = Circle(4)
    assert c.the_radius == 4


def test_diameter():
    c = Circle(4)
    assert c.the_diameter == c.the_radius*2


def test_area():
    c = Circle(4)
    assert c.the_area == 50.26548245743669


def test_area_is_private():
    c = Circle(4)
    c._area = 100
    assert AssertionError


def test_diameter_is_settable():
    c = Circle(1)
    c.the_diameter = 8
    assert c.the_diameter == 8
    assert c.the_radius == 4


def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_math():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1+c2 == 6
    assert (c2 - c1) == 2
    assert(c2 * c1) == 8
    assert c2//c1 == 2


if __name__ == "__main__":
    main()
    test_radius()
    test_diameter()
    test_area()
    test_area_is_private()
    test_diameter_is_settable()
    test_repr()
    test_math()
    print("tests passed, all done")


