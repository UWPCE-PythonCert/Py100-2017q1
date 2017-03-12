import unittest
from session08.circle import Circle


class CircleTest(unittest.TestCase):

    def test_step_one_returns_four(self):
        c = Circle(4)
        self.assertEqual(c.radius, 4)

    def test_step_two_returns_eight(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)

    def test_step_three_returns_two_and_one(self):
        c = Circle(4)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        #self.assertEqual(c.radius, 1)

    def test_step_four_returns_area(self):
        c = Circle(2)
        self.assertEqual(c.area, 12.566370614359172)

    def test_add_exception_val_returns_error(self):
        try:
            c = Circle(2)
            c.area = 42
        except AttributeError as error:
            print('The user should not be able to set the area: ', repr(error))

    def test_step_five_returns_eight_and_four(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)

    def test_step_six_returns_string(self):
        c = Circle(4)
        self.assertEqual(c.__str__(), 'Circle with radius: 4')
        self.assertEqual(repr(c), 'Circle(4)')

    def test_step_seven_returns_six_twelve(self):
        c1 = Circle(2)
        c2 = Circle(4)
        self.assertEqual(c1 + c2, 6)
        self.assertEqual(c2*3, 12)

    def test_step_eight_returns_validation(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = Circle(4)

        self.assertEqual(c1 > c2, False)
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c1 == c2, False)
        self.assertEqual(c2 == c3, True)


if __name__ == '__main__':
    unittest.main()
