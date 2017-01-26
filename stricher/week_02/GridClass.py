class Grid:
    def __init__(self, size: int, numRowsCols: int):
        Grid.__check_params(size, numRowsCols, "Grid() - Invalid args")
        self._size = size
        self._numRowsCols = numRowsCols

    @staticmethod
    def __isInteger(val) -> bool:
        import math
        return math.floor(val) == val

    @staticmethod
    def get_cellSize(gridSize: int, numRowsCols: int) -> float:
        numInteriorBorders = numRowsCols - 1
        return (gridSize - numInteriorBorders) / numRowsCols

    @staticmethod
    def __are_invalidArgs(size: int, numRowsCols: int) -> bool:
        return ((size == 0 or numRowsCols == 0) or
                (size <= numRowsCols) or not
                Grid.__isInteger(Grid.get_cellSize(size, numRowsCols)))

    @staticmethod
    def __check_params(size: int, numRowsCols: int, message: str):
        assert isinstance(size, int)
        assert isinstance(numRowsCols, int)
        if Grid.__are_invalidArgs(size, numRowsCols):
            from GridValueError import GridValueError
            raise GridValueError(message)

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        assert isinstance(value, int)
        if Grid.__are_invalidArgs(size=value, numRowsCols=self.numRowsCols):
            from GridValueError import GridValueError
            raise GridValueError("Grid.size = ... - Invalid argument")
        self._size = value

    @property
    def numRowsCols(self) -> int:
        return self._numRowsCols

    @numRowsCols.setter
    def numRowsCols(self, value: int):
        assert isinstance(value, int)
        if Grid.__are_invalidArgs(size=self.size, numRowsCols=value):
            from GridValueError import GridValueError
            raise GridValueError("Grid.numRowsCols = ... - Invalid argument")
        self._numRowsCols = value

    def resize(self, size: int, numRowsCols: int):
        Grid.__check_params(size, numRowsCols,
                            "Grid.resize = ... - Invalid arguments")
        self._size = size
        self._numRowsCols = numRowsCols

    @staticmethod
    def compute_heightWidth(numRowsCols: int, cellSize: int) -> int:
        numInteriorBorders = numRowsCols - 1
        return numRowsCols * cellSize + numInteriorBorders

    # ------- For test_grid.py ------
    @staticmethod
    def test__isInteger(val): return Grid.__isInteger(val)

    @staticmethod
    def test__are_invalidArgs(size, numRowsCols): return Grid.__are_invalidArgs(size, numRowsCols)

    @staticmethod
    def test__check_params(size, numRowsCols, message): return Grid.__check_params(size, numRowsCols, message)
    # ------- End For test_grid.py ------