from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def the_radius(self):
        return self.radius

    @property
    def the_diameter(self):
        self._diameter = self.radius*2
        return self._diameter

    @property
    def the_area(self):
        self._area = pi * (self.radius**2)
        return self._area

    @classmethod
    def from_diameter(cls, diameter):
        cls._diameter = diameter
        cls._radius = diameter/2


def main():
    c = Circle(4)
    print(c.the_radius)
    print(c.the_diameter)
    print(c.the_area)
    c._the_area = 100
    print(c.the_area)


def test1():
    c = Circle(4)
    assert c.the_radius == 4
def test2():
    c = Circle(4)
    assert c.the_diameter == c.the_radius*2
def test_area_is_private():
    c = Circle(4)
    c._area = 100
    print(c._area)
    assert c._area == 50.26548245743669

if __name__ == "__main__":
    main()
    test1()
    test2()
    test_area_is_private()
    print("tests passed, all done")


