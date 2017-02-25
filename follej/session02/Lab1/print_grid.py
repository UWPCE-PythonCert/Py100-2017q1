def print_grid(n):
    grid_size=n
    if grid_size % 2 == 0:
        grid_size += 1
    sub_box_size = (grid_size - 1) // 2
    top_segment = '+ ' + sub_box_size * '- '
    top = 2 * top_segment + '+'
    side_segment = '|' + grid_size * ' '
    side = 2 * side_segment + '|'
    print(top)
    for j in range(0, 2):
        for i in range(0, sub_box_size):
            print(side)
        print(top)

print_grid(11)
print_grid(3)
print_grid(15)
