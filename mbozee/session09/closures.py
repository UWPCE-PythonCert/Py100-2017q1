
shapes = ['dot', 'line', 'square', 'cube', 'tesseract']

tv_sayings = ['yabba dabba doo', 'do\'h', 'zoinks', 'to the moon', 'turtle flu']


def list_iter(a_list):
    # This is the outer enclosing function.

        def iter():
            # This is the nested function.
            dimension = 0
            for item in a_list:
                print(str(dimension) + "D: " + item)
                dimension += 1

        iter()

list_iter(shapes)

print('\n')

another_iter = list_iter(tv_sayings) # prints dimensions still, but okay for this exercise
