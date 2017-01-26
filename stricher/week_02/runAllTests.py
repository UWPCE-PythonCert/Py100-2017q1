
class RunAllTests:

    # ------------- FizzBuzz -------------

    @staticmethod
    def launch_tests_fizzBuzz():

        print("Testing fizzBuzz() ... " + 3 * "\t", end = "")

        from test_fizzBuzz import TestFizzBuzz
        tester = TestFizzBuzz()

        # Set recreateBenchTxtFile to True to regenerate the benchmark files
        # Reset to False for testing
        tester.test_fizzBuzz(recreateBenchTxtFile = False)

        print("Success !")

    # ------------- Tests series -----------

    @staticmethod
    def launch_tests_Fibonacci():

        print("Testing Fibonacci() ... " + 2 * "\t", end="")

        from test_fibonacci import TestFibonacci

        tester = TestFibonacci()
        tester.test_iter()
        tester.test_recurs()

        print("Success !")

    @staticmethod
    def launch_tests_Lucas():

        print("Testing Lucas() ... " + 3 * "\t", end="")

        from test_lucas import TestLucas

        tester = TestLucas()
        tester.test_iter()
        tester.test_recurs()

        print("Success !")

    @staticmethod
    def launch_tests_sumSeries():

        print("Testing sum_series() ... " + 2 * "\t", end="")

        from test_sum_series import TestSum_series

        tester = TestSum_series()

        tester.test_iter_fibonacci()
        tester.test_iter_lucas()
        tester.test_recurs_fibonacci()
        tester.test_recurs_Lucas()

        print("Success !")

    # ------------- Tests Grid -------------

    @staticmethod
    def launch_tests_GridValueError():

        print("Testing GridValueError() ... " + 2 * "\t", end="")

        from test_gridValueError import TestGridValueError
        tester = TestGridValueError()
        tester.test_raise_()

        print("Success !")

    @staticmethod
    def launch_tests_Grid():

        print("Testing Grid() ... " + 3 * "\t", end="")

        from test_grid import TestGrid

        tester = TestGrid()

        tester.test_isInteger()
        tester.test_get_cellSize()
        tester.test__are_invalidArgs()
        tester.test__check_params()
        tester.test_instantiateGrid()
        tester.test_stress_instantiateGrid()
        tester.test_size()
        tester.test_numRowsCols()
        tester.test_resize()
        tester.test_compute_heightWidth()

        print("Success !")

    @staticmethod
    def launch_tests_GridPrinter():

        print("Testing GridPrinter() ... " + 2 * "\t", end="")

        from test_gridPrinterClass import TestGridPrinter

        tester = TestGridPrinter()

        tester.test_instantiateGridPrinter()
        tester.test_getSetGrid()
        tester.test_iterAndRecurs_againstGivenSetOfGrids()

        # Set recreateBenchTxtFile to True to regenerate the benchmark files
        # Reset to False for testing
        tester.test_stress_printMethods(recreateBenchTxtFile = False)

        print("Success !")

    @staticmethod
    def launchAll():
        print("\nLaunching the tests ...\n")
        RunAllTests.launch_tests_fizzBuzz()
        RunAllTests.launch_tests_Fibonacci()
        RunAllTests.launch_tests_Lucas()
        RunAllTests.launch_tests_sumSeries()
        RunAllTests.launch_tests_GridValueError()
        RunAllTests.launch_tests_Grid()
        RunAllTests.launch_tests_GridPrinter()

        print("\nAll tests pass !")
