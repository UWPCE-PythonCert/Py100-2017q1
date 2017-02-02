from unittest import TestCase


class TestFizzBuzz(TestCase):

    @staticmethod
    def __test_writeTestFile(testStr):

        from FizzBuzz import fizzBuzz

        fizzBuzz(testStr)



    @staticmethod
    def __writeBenchTxt(pathToFile):

        from FizzBuzz import fizzBuzz

        try:
            with open(pathToFile, "w") as file:
                fizzBuzz(file)
        except IOError as ioerr:
            print("writeBenchTxt(self, pathToFile)"
                  " - I/O error ({0}): ({1})".format(ioerr.errno,
                                                     ioerr.strerror))



    def test_fizzBuzz(self, recreateBenchTxtFile = False):

        from Utilities import Utilities
        from TestsData import printFizzBuzzBenchTestPath
        import io

        # recreateBenchTxtFile: whether or not recreating the benchmark file
        # If set to True:
        #   - check the file
        #   - refactor ... against the bench file (frozen with recreateBenchTxtFile = False)

        if recreateBenchTxtFile:
            TestFizzBuzz.__writeBenchTxt(printFizzBuzzBenchTestPath)

        utils = Utilities()
        benchmarkTestStr = utils.fileToString(printFizzBuzzBenchTestPath)
        testStr = io.StringIO()
        TestFizzBuzz.__test_writeTestFile(testStr)
        self.assertEqual(benchmarkTestStr, testStr.getvalue())
