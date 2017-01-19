def print_grid(horizontal,vertical,blocks_vertical):
    border = ("+ - - - - - - - ")
    body = "|               "
    length = (int(horizontal)-1)
    for n in range(0, blocks_vertical):
        print(border + (border*length+"+"))
        for n in range(0, vertical):
            print(body + (body*length+"|"))
    print(border + (border*length)+ "+")

#horizontal = (int) Number of grids (horizontal) to expand to the left
#vertical = (int) Number of lines (|) that each block will utilize
#blocks_vertical = (int) Number of grids (vertical) to expand downwards

print_grid (2,7,2)