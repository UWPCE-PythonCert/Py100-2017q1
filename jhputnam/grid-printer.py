#!/usr/bin/env python3

"""A little module to print a grid."""


def build_frame(cell_count, cell_size):
    """
    Function to build the top and bottom rows and side columns for each cell.
    Positional Arguments:
    cell_count -- Number of cells in the grid.
    cell_size -- Size of each cell in the grid.
    """

    row = ""
    for count in range(cell_count):
        row += "+ " + "- " * cell_size
        if count == cell_count - 1:
            row += "+"
    col = ""
    for count in range(cell_count):
        col += "| " + "  " * cell_size
        if count == cell_count - 1:
            col += "|"

    return row, col


def grid_printer(cell_count, cell_size):
    """
    Function prints a grid.
    Positional Arguments:
    cell_count -- The number of cells to print.
    cell_size -- The size of each cell.
    """

    row, col = build_frame(cell_count, cell_size)

    for ccount in range(cell_count * cell_size):
        if ccount % cell_size == 0:
            print(row)
            for cscount in range(cell_size):
                print(col)
    print(row)


def get_numbers():
    """Function to ask the user for cell count and cell size."""

    while True:
        try:
            cell_count = int(input("Enter an integer value to represent the "
                                   "cell count: "))
            cell_size = int(input("Enter an integer value to represent the "
                                  "cell size: "))
        except ValueError:
            print("Not a standard int. Please try again.")
            continue
        else:
            break

    return cell_count, cell_size


def main():
    """
    Main entry point for the program.
    """

    cell_count, cell_size = get_numbers()
    grid_printer(cell_count, cell_size)


if __name__ == '__main__':
    main()
