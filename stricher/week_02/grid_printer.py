
import sys

def print_grid(size: int = None, ostream = sys.stdout):
    from GridPrinterClass import GridPrinter
    GridPrinter.print_grid(size = size, ostream = ostream)

def print_grid2(numRowsCols: int, cellSize: int, ostream = sys.stdout):
    from GridPrinterClass import GridPrinter
    GridPrinter.print_grid(numRowsCols = numRowsCols, cellSize = cellSize, ostream = ostream)