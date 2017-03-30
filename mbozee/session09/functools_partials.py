# Functools partials practice, based on https://www.pydanny.com/python-partials-are-fun.html


def perimeter(single_length, sides):
    '''Calculates the perimeter of an equilateral shape, given length of one side and number of sides.'''
    return single_length * sides


def pentagon(single_length):
    '''Returns perimeter of an equilateral pentagon, taking length of one side as argument.'''
    return perimeter(single_length, 5)


def square(single_length):
    '''Returns perimeter of an equilateral square, taking length of one side as argument.'''
    return perimeter(single_length, 4)


def triangle(single_length):
    '''Returns perimeter of an equilateral triangle, taking length of one side as argument.'''
    return perimeter(single_length, 3)


# pentagon
pentagon1 = {'name': 'pentagon1'}
pentagon1['perimeter'] = pentagon(5)

#square
square1 = {'name': 'square1'}
square1['perimeter'] = square(10)

# triangle
triangle1 = {'name': 'triange1'}
triangle1['perimeter'] = triangle(3)

shapes = [pentagon1, square1, triangle1]
print(shapes)
print("\n")

for shape in shapes:
    print(shape['name'] + "'s perimeter: " + str(shape['perimeter']))
