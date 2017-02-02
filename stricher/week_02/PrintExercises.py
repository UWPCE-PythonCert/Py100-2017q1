
class ExercisesToStdout():

    @staticmethod
    def printExerciseRef(exercise: str) -> None:
        print(2 * "\n" + 4 * "*" + " " + exercise + " exercise " + 4 * "*" + "\n")

    @staticmethod
    def printSeries(upperLimit: int, name: str, f_0 = 0, f_1 = 1) -> None:

        from series import sum_series

        if upperLimit < 0:
            raise ValueError("ExercisesToStdout.printSeries(name, upperLimit)"
                             " - Invalid argument: upperLimit must be >= 0")
        tab = 2 * "\t"
        for ii in range(upperLimit):
            print("{}({}) ".format(name, ii) + tab + " = {}".
                  format(sum_series.iter(ii, f_0 = f_0, f_1 = f_1)))

    @staticmethod
    def fizzBuzz_stdout() -> None:
        from FizzBuzz import fizzBuzz
        import sys

        ExercisesToStdout.printExerciseRef("fizzBuzz")
        fizzBuzz(sys.stdout)


    @staticmethod
    def Fibonacci_stdout() -> None:
        from series import Fibonacci

        fib = Fibonacci()
        name = "Fibonacci"
        ExercisesToStdout.printExerciseRef(name)
        ExercisesToStdout.printSeries(upperLimit = 11, name = name)


    @staticmethod
    def Lucas_stdout() -> None:
        from series import Lucas

        luc = Lucas()
        name = "Lucas"
        ExercisesToStdout.printExerciseRef(name)
        ExercisesToStdout.printSeries(upperLimit=11, name=name, f_0=2, f_1=1)


    @staticmethod
    def gridPrinter_stdout() -> None:

        def gridPrinterExerciseRef(index: int) -> None:
            print("\nGrid Printer Exercise " + str(index) + "\n")

        from grid_printer import print_grid, print_grid2

        ExercisesToStdout.printExerciseRef("Grid printer")

        # Exercise part 1
        gridPrinterExerciseRef(1)
        print_grid()
        print()

        # Exercise part 2
        gridPrinterExerciseRef(2)
        print_grid(size=3)
        print()
        print_grid(size=15)
        print()

        # Exercise part 3
        gridPrinterExerciseRef(3)
        print_grid2(numRowsCols=3, cellSize=4)
        print()
        print_grid2(numRowsCols=5, cellSize=3)

    @staticmethod
    def allExercises_stdout() -> None:

        ExercisesToStdout.fizzBuzz_stdout()
        ExercisesToStdout.Fibonacci_stdout()
        ExercisesToStdout.Lucas_stdout()
        ExercisesToStdout.gridPrinter_stdout()