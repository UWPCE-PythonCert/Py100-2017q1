from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = self.radius * 2

    @property
    def radius(self):
        return self.radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self.radius = diamter/2

    @property
    def area(self):
        return pi * (self.radius**2)

    @staticmethod
    def radius_to_area(radius):
        return pi * (radius**2)

    @classmethod
    def my_class_method(cls):
        pass


circle1 = Circle.radius_to_area(1)
circle2 = Circle.radius_to_area(10)
circle3 = Circle.radius_to_area(25)
circle4 = Circle.radius_to_area(15)
circle5 = Circle.radius_to_area(1)

circles = [circle1, circle2, circle3, circle4, circle5]

i = 1
for circle in circles:
    print("Circle #" + str(i) + "'s area: " + str(circle))
    i+= 1

circle_combo = circle1 + circle2
print(circle_combo)


try:
    circle_biggest = max(circles)
    print("Biggest circle's area: " + str(circle_biggest))
except:
    ValueError
    print('List of circles is empty!')

circles_sorted = sorted(circles)
print("Circles sorted: " + str(circles_sorted))

seen = set()
for circle in circles:
    if circle in seen:
        print("Duplicate found! : " + str(circle))
    else:
        seen.add(circle)
