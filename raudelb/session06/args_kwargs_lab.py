
def func(fore_color='white', back_color='white', link_color='white', visited_color = 'white'):
    print('Fore Color: ', fore_color)
    print('Back Color: ', back_color)
    print('Link Color: ', link_color)
    print('Visited Color: ', visited_color)


def func_parm(*args, **kwargs):
    print('Fore Color: ', args[0])
    print('Back Color: ', args[1])
    print('Link Color: ', kwargs['link_color'])
    print('Visited Color: ', kwargs['visited_color'])


def func_direct(*args, **kwargs):
    print('Values for args are: ', args)
    print('Value for kwargs are: ', kwargs)


def func_adapted(*args, **kwargs):
    if len(args):
        print('Values for args are: ', args)
    else:
        print('You are not passing any args argument..')

    if len(kwargs):
        print('Value for kwargs are: ', kwargs)
    else:
        print('You are not passing any  kwargs argument..')


def main():
    # Write a function that has four optional parameters (with defaults):
    # Have it print the colors (use strings for the colors)

    func()

    # Call it with a couple different parameters set
    print('--------------------------')
    print('Different parameters set..')
    func('red', 'blue', 'yellow', 'chartreuse')

    # using just keyword arguments
    print('--------------------------')
    print('Using just keyword arguments')

    func(link_color='red', back_color='blue')
    print('-------------------------..')

    # using a combination of positional and keyword

    print('Using a combination of positional and keyword')
    func('purple', link_color='red', back_color='blue')
    print('-------------------------..')

    # using *some_tuple and/or **some_dict

    print('Using *some_tuple and/or **some_dict')

    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}

    func(*regular, **links)
    print('-------------------------..')

    # Write a the same function with the parameters as: *args and **kwags

    # Have it print the colors (use strings for the colors)

    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse', 'visited_color': 'blue'}

    # Call it with the same various combinations of arguments used above.

    func(*regular, **links)

    print('-------------------------..')

    # Also have it print args and kwargs directly, so you can be sure you understand what’s going on.

    func_direct(*regular, **links)

    # Note that in general, you can’t know what will get passed into **kwargs
    # So maybe adapt your function to be able to do something reasonable with any keywords.

    print('-------------------------..')
    func_adapted(*regular) # not passing kwargs argument

    print('-------------------------..')
    func_adapted(**links) # not passing args argument


if __name__ == '__main__':
    main()