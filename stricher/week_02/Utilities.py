class Utilities:
    @staticmethod
    def fileToString(pathToFile):
        testStr = ""
        try:
            with open(pathToFile, "r") as file:
                for line in file:
                    testStr += line
                return testStr
        except IOError as ioerr:
            print("fileToString(self, pathToFile)"
                  " - I/O error ({0}): ({1})".format(ioerr.errno,
                                                     ioerr.strerror))
