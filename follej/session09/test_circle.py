import random
from math import pi

import pytest

from Circle import Circle


@pytest.fixture(scope='function')
def test_circle(request):
    radius = request.param
    return Circle(radius)


@pytest.fixture(scope='function')
def test_circle2(request):
    radius = request.param
    return Circle(radius)


# Step 1:  Circle class from a radius input
@pytest.mark.parametrize('test_circle, radius', [(5, 5), (10, 10)], indirect=['test_circle'])
def test_circle_create(test_circle, radius):
    assert test_circle.radius == radius


# Step 2:  Return the diameter property
@pytest.mark.parametrize('test_circle, expected_diameter', [(5, 10), (10, 20)], indirect=['test_circle'])
def test_set_circle_diameter(test_circle, expected_diameter):
    assert test_circle.diameter == expected_diameter


# Step 3:  Set the diameter of the circle.  Check radius attribute is updated.
@pytest.mark.parametrize('test_circle, new_diameter, expected_radius', [(10, 10, 5), (20, 20, 10)],
                         indirect=['test_circle'])
def test_get_circle_diameter(test_circle, new_diameter, expected_radius):
    test_circle.diameter = new_diameter
    assert test_circle.radius == expected_radius


# Step 4: Add an area property so the user can get the area of the circle.
@pytest.mark.parametrize('test_circle, expected_area', [(5, pi * 5 ** 2), (10, pi * 10 ** 2)], indirect=['test_circle'])
def test_circle_area(test_circle, expected_area):
    assert test_circle.area == expected_area


# AttributeError if circle area attempts to set
@pytest.mark.parametrize('test_circle', [5, 10], indirect=['test_circle'])
def test_assign_area(test_circle):
    with pytest.raises(AttributeError):
        test_circle.area = 42


# Step 5:  Add an “alternate constructor” that lets the user create a Circle directly with the diameter:
@pytest.mark.parametrize('test_diameter, expected_radius', [(10, 5), (20, 10)])
def test_circle_from_diameter(test_diameter, expected_radius):
    assert Circle.from_diameter(test_diameter).radius == expected_radius


# Step 6:  __str__ methods to your Circle class.
@pytest.mark.parametrize('test_circle, expected_print_statement',
                         [(5, 'Circle with radius 5\n'), (10, 'Circle with radius 10\n')],
                         indirect=['test_circle'])
def test_circle_print(test_circle, expected_print_statement, capsys):
    print(test_circle)
    out, err = capsys.readouterr()
    assert out == expected_print_statement


# __repr__  methods to your Circle class.
@pytest.mark.parametrize('test_circle', [5, 10], indirect=['test_circle'])
def test_circle_repr(test_circle):
    assert isinstance(eval(repr(test_circle)), Circle)


# Step 7:
@pytest.mark.parametrize('test_circle, test_circle2, expected_radius', [(5, 5, 10), (10, 5, 15)],
                         indirect=['test_circle', 'test_circle2'])
def test_add_circles(test_circle, test_circle2, expected_radius):
    assert (test_circle2 + test_circle).radius == expected_radius


@pytest.mark.parametrize('test_circle, test_circle2, expected_radius', [(5, 15, 10), (10, 15, 5)],
                         indirect=['test_circle', 'test_circle2'])
def test_subtract_circles(test_circle, test_circle2, expected_radius):
    assert (test_circle2 - test_circle).radius == expected_radius


@pytest.mark.parametrize('test_circle, test_circle2', [(15, 15), (25, 15)],
                         indirect=['test_circle', 'test_circle2'])
def test_subtract_error_circles(test_circle, test_circle2):
    with pytest.raises(AttributeError):
        test_circle2 - test_circle


@pytest.mark.parametrize('test_circle, multiplier, expected_radius', [(5, 3, 15), (10, 5, 50)],
                         indirect=['test_circle'])
def test_multiply_circle(test_circle, multiplier, expected_radius):
    assert (test_circle * multiplier).radius == expected_radius
    assert (multiplier * test_circle).radius == expected_radius


# Step 8:  Comparing and Sorting

@pytest.mark.parametrize('test_circle, test_circle2, expected_results', [(25, 15, True), (15, 25, False)],
                         indirect=['test_circle', 'test_circle2'])
def test_compare_circles(test_circle, test_circle2, expected_results):
    assert (test_circle > test_circle2) is expected_results
    assert (test_circle < test_circle2) is not expected_results
    assert (test_circle == test_circle2) is False
    assert (Circle(test_circle.radius) == test_circle)


def test_sort_circles():
    circles = []
    [circles.append(Circle(i)) for i in range(1, 10)]
    print(circles)
    circles_random = random.sample(circles, len(circles))
    print(sorted(circles_random))
    assert sorted(circles_random) == circles


# Step 8 Optional:
@pytest.mark.parametrize('test_circle, test_circle2, expected_radius', [(5, 5, 10), (10, 5, 15)],
                         indirect=['test_circle', 'test_circle2'])
def test_iadd_circles(test_circle, test_circle2, expected_radius):
    test_circle += test_circle2
    assert test_circle.radius == expected_radius
