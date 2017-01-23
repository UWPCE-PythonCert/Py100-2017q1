def print_grid2(m, n):
    grid_dim = m
    sub_box_size = n
    # if grid_size % 2 == 0:
    #     grid_size += 1
    # sub_box_size = (grid_size - 1) // 2

    top_segment = '+ ' + sub_box_size * '- '
    top = grid_dim * top_segment + '+'
    side_segment = '|' + (sub_box_size * 2 + 1) * ' '
    side = grid_dim * side_segment + '|'
    print(top)
    for j in range(0, grid_dim):
        for i in range(0, sub_box_size):
            print(side)
        print(top)


print_grid2(3, 4)
print_grid2(5, 3)
