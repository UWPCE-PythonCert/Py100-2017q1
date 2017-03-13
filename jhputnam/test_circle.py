"""
Circle class testing.
"""

from circle_class import Circle
import pytest


def test_radius():
    """Test basic radius."""

    test_circle = Circle(22)

    assert test_circle.radius == 22


def test_diameter():
    """Test basic calculation of diameter from radius."""

    test_circle = Circle(5)

    assert test_circle.diameter == 10


def test_area():
    """Test basic calculation of area from radius."""

    test_circle = Circle(8)

    assert test_circle.area == 201.06192982974676


def test_set_diameter():
    """Test to ensure diameter is settable."""

    test_circle = Circle(10)
    test_circle.diameter = 16

    assert test_circle.diameter == 16
    assert test_circle.radius == 8


def test_from_diameter():
    """Test from_diameter constructor."""

    test_circle = Circle.from_diameter(25)

    assert test_circle.diameter == 25
    assert test_circle.radius == 12.5


def test_from_area():
    """Test from_area constructor."""

    test_circle = Circle.from_area(201.06192982974676)

    assert test_circle.diameter == 16
    assert test_circle.radius == 8


def test_set_area_error():
    """Test to ensure AttributeError when trying to set area."""

    test_circle = Circle(20)

    with pytest.raises(AttributeError) as execinfo:
        test_circle.area = 50

    assert "can't set attribute" in str(execinfo.value)


def test_str_method(capsys):
    """Test to confirm that the __str__ method is doing what it should."""

    test_circle = Circle(35)
    print(test_circle)

    # Grab stdout, ignoring stderr.
    out, _ = capsys.readouterr()

    assert out == "Circle with radius: 35\n"


def test_repr_method():
    """Test to confirm that the __repr__ method is doing what it should."""

    test_circle = Circle(40)

    assert repr(test_circle) == "Circle(40)"


def test_add_and_mul():
    """Test if two circiels can be added and multipled properly."""

    test_circ1 = Circle(25)
    test_circ2 = Circle(5)

    # Test add.
    result = test_circ1 + test_circ2

    assert repr(result) == "Circle(30)"

    # Test multiply both directions.
    result = test_circ1 * 25

    assert repr(result) == "Circle(625)"

    result = 10 * test_circ1

    assert repr(result) == "Circle(250)"


def test_reflected_numerics():
    """Specifically test relfected numerics."""

    test_circle = Circle(99)

    assert test_circle * 5 == 5 * test_circle


def test_comparisons():
    """Test comparisons of circles."""

    test_circ1, test_circ2 = Circle(22), Circle(5)

    assert test_circ1 > test_circ2
    assert test_circ2 < test_circ1

    test_circ1, test_circ2 = Circle(123), Circle(123)

    assert test_circ1 == test_circ2


def test_circle_sorting():
    """Test whether or not we can sort a list of circles."""

    circles = [
        Circle(123),
        Circle(555),
        Circle(1),
        Circle(90),
        Circle(44),
        Circle(2),
        Circle(75)
    ]

    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(44), Circle(75),
                       Circle(90), Circle(123), Circle(555)]
