from unittest import TestCase


class TestGrid(TestCase):


    def test_isInteger(self):

        def __test(val, expected):
            from GridClass import Grid
            self.assertEqual(Grid.test__isInteger(val), expected)

        __test(0, True)
        __test(1, True)
        __test(-1, True)
        __test(2, True)
        __test(5 * (10 ** -6), False)
        __test(-1 * (10 ** -6), False)
        __test(3.14, False)



    def test_get_cellSize(self):

        from GridClass import Grid

        self.assertEqual(1, Grid.get_cellSize(3, 2))
        self.assertEqual(4, Grid.get_cellSize(9, 2))
        self.assertEqual(4, Grid.get_cellSize(14, 3))
        self.assertEqual(1.5, Grid.get_cellSize(4, 2))



    def test__are_invalidArgs(self):

        from GridClass import Grid

        # gridHeightWidth == 0 or numRowsCols == 0
        self.assertTrue(Grid.test__are_invalidArgs(0, 1))
        self.assertTrue(Grid.test__are_invalidArgs(1, 0))

        # gridHeightWidth <= numRowsCols
        self.assertTrue(Grid.test__are_invalidArgs(3, 4))
        self.assertTrue(Grid.test__are_invalidArgs(10, 11))

        # not isInteger(cellSize(gridHeightWidth, numRowsCols))
        self.assertFalse(Grid.test__isInteger((Grid.get_cellSize(4, 2))))
        self.assertTrue(Grid.test__are_invalidArgs(4, 2))



    def test__check_params(self):

        def __test(size, numRowsCols, message):

            from GridClass import Grid
            from GridValueError import GridValueError

            try:
                Grid.test__check_params(size, numRowsCols, message)
                self.fail()
            except GridValueError as gve:
                self.assertEqual(message, str(gve))

            __test(0, 0, "Grid.size = ... - Invalid argument")
            __test(0, 1, "Grid.size = ... - Invalid argument")
            __test(2, 0, "Grid.numRowsCols = ... - Invalid argument")
            __test(3, 3, "Grid.resize = ... - Invalid arguments")



    def test_instantiateGrid(self):

        from GridClass import Grid

        grid = Grid(4, 1)
        self.assertEqual(4, grid.size)
        self.assertEqual(1, grid._numRowsCols)
        del grid

        grid = Grid(9, 2)
        self.assertEqual(9, grid.size)
        self.assertEqual(2, grid._numRowsCols)
        del grid

        try:
            from GridValueError import GridValueError
            grid = Grid(0,0)
            self.fail("Should raise GridValueError")
        except GridValueError as gve:
            self.assertEqual("Grid() - Invalid args", str(gve))

        try:
            from GridValueError import GridValueError
            grid = Grid(6, 3)
            self.fail("Should raise GridValueError")
        except GridValueError as gve:
            self.assertEqual("Grid() - Invalid args", str(gve))



    @staticmethod
    def __writeBenchmark(ostream):

        from GridClass import Grid
        from GridValueError import GridValueError
        import sys

        for size in range(100):
            for numRowsCols in range(100):
                try:
                    grid = Grid(size, numRowsCols)
                    ostream.write("Successfully created grid = Grid({},{}): ".format(size, numRowsCols))
                    ostream.write("\n")

                except GridValueError as gve:
                    ostream.write("Argument ({},{}): ".format(size, numRowsCols))
                    ostream.write(str(gve))
                    ostream.write("\n")

                except:
                    ostream.write("__test_writeBenchmark(self, ostream) - "
                              "Unexpected error: {}".format(sys.exc_info()[0]))
                    ostream.write("\n")



    @staticmethod
    def __writeBenchmarkTxt(pathToBenchFile):

        import sys

        try:
            with open(pathToBenchFile, 'w') as file:
                TestGrid.__writeBenchmark(file)

        except IOError as ioerr:
            print("__writeBenchmarkTxt(self, pathToFile)"
                  " - I/O error ({0}): ({1})".format(ioerr.errno, ioerr.strerror))

        except:
            print("__writeBenchmarkTxt(self, pathToFile) - "
                  "Unexpected error: {}".format(sys.exc_info()[0]))
            raise



    def test_stress_instantiateGrid(self):

        from TestsData import printBenchGrid

        # Benchmark file generation - Keep to false when coding, refactoring ...

        recreateBenchTxtFile = False # Set to true to recreate the file, then check the file
        if recreateBenchTxtFile:
            TestGrid.__writeBenchmarkTxt(printBenchGrid)

        # Test Grid() instantiation against benchmark file
        from Utilities import Utilities

        utils = Utilities()

        benchmarkStr = utils.fileToString(printBenchGrid)

        import io
        testStr = io.StringIO()
        TestGrid.__writeBenchmark(testStr)

        self.assertEqual(benchmarkStr, testStr.getvalue())



    def test_size(self):

        from GridClass import Grid
        import sys

        try:
            grid = Grid(3,2)
        except:
            print("test_size(self) - "
                  "Unexpected error: {}".format(sys.exc_info()[0]))

        self.assertEqual(3, grid.size)
        from GridValueError import GridValueError
        try:
            grid.size = 4
            self.fail("should raise GridValueError")
        except GridValueError as gve:
            self.assertEqual("Grid.size = ... - Invalid argument", str(gve))



    def test_numRowsCols(self):

        from GridClass import Grid
        import sys

        try:
            grid = Grid(5,3)
        except:
            print("test_size(self) - "
                  "Unexpected error: {}".format(sys.exc_info()[0]))

        self.assertEqual(3, grid.numRowsCols)
        from GridValueError import GridValueError
        try:
            grid.numRowsCols = 4
            self.fail("should raise GridValueError")
        except GridValueError as gve:
            self.assertEqual("Grid.numRowsCols = ... - Invalid argument", str(gve))



    def test_resize(self):

        from GridClass import Grid
        from GridValueError import GridValueError
        import sys

        try:
            grid = Grid(9,5)
        except GridValueError as gve:
            self.fail("should not raise GridValueError")
        except:
            print("test_size(self) - "
                  "Unexpected error: {}".format(sys.exc_info()[0]))

        self.assertEqual(9, grid.size)
        self.assertEqual(5, grid.numRowsCols)

        try:
            grid.resize(5,3) # size ok
        except GridValueError as gve:
            self.fail("should not raise GridValueError")
        try:
            grid.resize(9, 5)  # size ok
        except GridValueError as gve:
            self.fail("should not raise GridValueError")
        try:
            grid.resize(9,6) # size not ok
            self.fail("should raise GridValueError")
        except GridValueError as gve:
            self.assertEqual("Grid.resize = ... - Invalid arguments", str(gve))



    def test_compute_heightWidth(self):

        from GridClass import Grid

        self.assertEqual(9, Grid.compute_heightWidth(2, 4))
        self.assertEqual(3, Grid.compute_heightWidth(2, 1))
        self.assertEqual(19, Grid.compute_heightWidth(5, 3))