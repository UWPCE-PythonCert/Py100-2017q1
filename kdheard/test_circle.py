from circle import Circle


def test_calculations():
    c = Circle(4)
    assert c.the_radius == 4
    assert c.the_diameter == 8
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


def test_comparisons():
    c1 = Circle(2)
    c2 = Circle(4)
    c2 > c1 is True
    c2 >= c1 is True
    c1 >= c2 is False
    c1 != c2 is True
    c1 == c2 is False
    c1 < c2 is True
    c1 <= c2 is True
    c1 <= c2 is False


def test_circle_sort():
    circles = [
        Circle(11),
        Circle(13),
        Circle(7),
        Circle(1),
        Circle(3),
        Circle(5),
        Circle(9)
    ]

    assert circles == [Circle(11), Circle(13), Circle(7), Circle(1), Circle(3), Circle(5), Circle(9)]
    circles.sort()
    assert circles == [Circle(1), Circle(3), Circle(5), Circle(7), Circle(9), Circle(11), Circle(13)]
