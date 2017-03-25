#!/usr/bin/env python3

"""Circle class module."""

from math import pi, sqrt


class Circle(object):
    """Circle class."""

    def __init__(self, radius):
        """Init for class."""

        self._radius = radius

    def __repr__(self):
        """
        __repr__ method to return a printable representation of the object.
        """

        return "{}({})".format(self.__class__.__name__, self._radius)

    def __str__(self):
        """
        __str__ method to return a description of the basic circle.
        """

        return "Circle with radius: {}".format(self.radius)

    def __add__(self, circle2):
        """
        __add__ method to add two circles together and return a new object.
        """

        return Circle(self._radius + circle2.radius)

    def __mul__(self, number):
        """__mul__ method to multiply circle by a number."""

        return Circle(self._radius * number)

    def __rmul__(self, number):
        """__rmul__ method to multiply a number by a circle."""

        return Circle(number * self._radius)

    def __lt__(self, circle2):

        return self._radius < circle2.radius

    def __eq__(self, circle2):

        return self._radius == circle2.radius

    def __gt__(self, circle2):

        return self._radius > circle2.radius

    @property
    def radius(self):
        """Getter method to return radius."""

        return self._radius

    @radius.setter
    def radius(self, radius):
        """Setter method for radius."""

        self._radius = radius

    @property
    def diameter(self):
        """Getter method to return diameter."""

        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Setter method for setting radius from diameter."""

        self._radius = diameter / 2

    @property
    def area(self):
        """Method to calculate area from radius."""

        return pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """Factory method constructor to init from diameter."""

        return cls(diameter / 2)

    @classmethod
    def from_area(cls, area):
        """Factory method constructor to init from area."""

        return cls(sqrt(area/pi))
