from unittest import TestCase


class TestGridPrinter(TestCase):

    def test_instantiateGridPrinter(self):

        from GridPrinterClass import GridPrinter
        from GridClass import Grid
        from GridValueError import GridValueError

        try:
            gridPrinter = GridPrinter(Grid(3, 2))
        except GridValueError as gve:
            self.fail("Shouldn't raise a GridValueError exception")
        else:
            del gridPrinter

        try:
            gridPrinter = GridPrinter(Grid(5, 4))
            self.fail("Should raise a GridValueError exception")
        except GridValueError as gve:
            self.assertEqual("Grid() - Invalid args", str(gve))



    def test_getSetGrid(self):

        from GridPrinterClass import GridPrinter
        from GridClass import Grid

        # Getter
        grid = Grid(3, 2)
        gridPrinter = GridPrinter(grid)
        self.assertEqual(grid, gridPrinter.grid)

        # Setter
        newGrid = Grid(5,3)
        gridPrinter.grid = newGrid
        self.assertNotEqual(gridPrinter.grid, grid)
        self.assertEqual(gridPrinter.grid, newGrid)



    def test_iterAndRecurs_againstGivenSetOfGrids(self):

        from TestsData import GridTestsStr
        from GridPrinterClass import GridPrinter
        from GridClass import Grid
        import io

        def compareGrids(dim: str, name: str):

            gridPars = dim.split('_')
            printer = GridPrinter(Grid(size = int(gridPars[0]), numRowsCols = int(gridPars[1])))

            # iter
            gridStrStream = io.StringIO()
            printer.iter(gridStrStream)
            self.assertEqual(gridStrStream.getvalue(), GridTestsStr[name])
            del gridStrStream

            # recurs
            gridStrStream = io.StringIO()
            printer.recurs(gridStrStream)
            self.assertEqual(gridStrStream.getvalue(), GridTestsStr[name])

        # Grids given in the lesson webpage:
        refGrids = {'9_2':'grid1', '3_2':'grid2', '15_2':'grid3', '14_3':'grid4', '19_5':'grid5'}
        for dim, name in refGrids.items():
            compareGrids(dim, name)



    @staticmethod
    def __writeBenchmark(method, ostream, log):

        if method != "iter" and method != "recurs":
            raise ValueError("__writeBenchmark() - method must be either iter or recurs")

        from GridValueError import GridValueError
        from GridClass import Grid
        from GridPrinterClass import GridPrinter
        import sys

        for size in range(100):
            for numRowsCols in range(100):
                try:
                    gridPrinter = GridPrinter(Grid(size, numRowsCols))

                    if method == "iter":
                        gridPrinter.iter(ostream)
                    else:
                        gridPrinter.recurs(ostream)

                    ostream.write("\n\n")

                except GridValueError as gve:
                    log.write(method + "({},{}): ".format(size, numRowsCols))
                    log.write(str(gve))
                    log.write("\n")

                except:
                    log.write("__writeBenchmark(method = {}, ostream, log) - "
                                  "Unexpected error: {}".format(method, sys.exc_info()[0]))
                    log.write("\n")



    @staticmethod
    def __writeBenchTxt(benchFiles):

        import sys

        for key, value in benchFiles.items():

            file = open(value[0], "w")
            logFile = open(value[1], "w")

            try:
                TestGridPrinter.__writeBenchmark(str(key), file, logFile)

            except IOError as ioerr:
                print("__writeBenchTxt(..., {}, {})"
                      " - I/O error ({0}): ({1})".format(value[0],
                                                         value[1],
                                                         ioerr.errno,
                                                         ioerr.strerror))

            except:
                print("writeBenchTxt(self, {}, {}) - "
                      "Unexpected error: {}".format(value[0],
                                                    value[1],
                                                    sys.exc_info()[0]))
                raise

            finally:
                file.close()
                logFile.close()



    def __benchIterRecurs_filesAreEqual(self, benchFiles):

        from Utilities import Utilities
        utils = Utilities()

        gridBenchIterStr = utils.fileToString(benchFiles['iter'][0])
        gridBenchRecursStr = utils.fileToString(benchFiles['recurs'][0])
        self.assertEqual(gridBenchIterStr, gridBenchRecursStr)

        # log files: need to remove iter and recurs names to test files are equal
        logBenchIterStr = utils.fileToString(benchFiles['iter'][1])
        logBenchIterStr = logBenchIterStr.replace('iter','')

        logBenchRecursStr = utils.fileToString(benchFiles['recurs'][1])
        logBenchRecursStr = logBenchRecursStr .replace('recurs','')

        self.assertEqual(logBenchIterStr, logBenchRecursStr)



    def __test_iter_recurs_against_benchTxt(self, benchFiles):

        from Utilities import Utilities
        utils = Utilities()

        import io
        for key, value in benchFiles.items():

            gridBenchStr = utils.fileToString(value[0])
            logBenchStr = utils.fileToString(value[1])

            gridTestStr = io.StringIO()
            logTestStr = io.StringIO()

            TestGridPrinter.__writeBenchmark(method = str(key), ostream = gridTestStr, log = logTestStr)

            self.assertEqual(gridBenchStr, gridTestStr.getvalue())
            self.assertEqual(logBenchStr, logTestStr.getvalue())



    def test_stress_printMethods(self, recreateBenchTxtFile = False):

        # recreateBenchTxtFile: whether or not recreating the benchmark files
        # If set to True:
        #   - check the files (equality between iter and recurs generated files is tested)
        #   - refactor ... against the bench files (frozen with recreateBenchTxtFile = False)

        from TestsData import bench_GridPrinter_files

        if recreateBenchTxtFile:
            TestGridPrinter.__writeBenchTxt(bench_GridPrinter_files)
            self.__benchIterRecurs_filesAreEqual(bench_GridPrinter_files)

        # Test iter and recurs against benchmark file
        self.__test_iter_recurs_against_benchTxt(bench_GridPrinter_files)
