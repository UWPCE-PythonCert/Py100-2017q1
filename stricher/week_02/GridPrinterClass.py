class GridPrinter:

    from GridClass import Grid
    import io

    def __init__(self, grid: Grid):
        self._grid = grid
        self._size = grid.size
        self._numRowsCols = grid.numRowsCols

    @property
    def grid(self) -> Grid:
        return self._grid

    @grid.setter
    def grid(self, value: Grid):
        self._grid = value

    def __print_row(self, sep: str, fill: str, ostream: io.IOBase):
        ostream.write(sep)
        for ii in range(self._numRowsCols):
            for jj in range(self._size // self._numRowsCols):
                ostream.write(" ")
                ostream.write(fill)
            ostream.write(" ")
            ostream.write(sep)

    def iter(self, ostream: io.IOBase):
        self.__print_row('+', '-', ostream)
        for ii in range(self._numRowsCols):
            ostream.write('\n')
            for jj in range(self._size // self._numRowsCols):
                self.__print_row('|', ' ', ostream)
                ostream.write('\n')
            self.__print_row('+', '-', ostream)

    def recurs(self, ostream: io.IOBase, index = 0):
        if index == self._size + 2: return
        isBorder = index % \
                   (int(self.grid.get_cellSize(self._size,
                                               self._numRowsCols)) + 1)\
                   == 0
        sep = '+' if isBorder else '|'
        fill = '-' if isBorder else ' '

        self.__print_row(sep, fill, ostream)
        ostream.write("" if index == (self._size + 1) else "\n")
        self.recurs(ostream, index + 1)

    # Grid Printer Exercise - Parts 1/2/3
    import sys
    @staticmethod
    def print_grid(size: int = None, numRowsCols: int = None,
                   cellSize: int = None, ostream = sys.stdout):

        from GridClass import Grid

        while True:
            if (size is None and numRowsCols is None) and cellSize is None:
                size = 9
                numRowsCols = 2
                break

            if numRowsCols is None:
                numRowsCols = 2
                break

            if size is None:
                size = Grid().compute_heightWidth(numRowsCols, cellSize)
                break
            break

        printer = GridPrinter(Grid(size = size, numRowsCols = numRowsCols))
        printer.iter(ostream)