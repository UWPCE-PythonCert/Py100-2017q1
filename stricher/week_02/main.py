#!/usr/local/bin/python3


def main():

    # ---------- Run All Tests --------

    # unittest library needed

    from runAllTests import RunAllTests
    RunAllTests().launchAll()

    # -------- Homework exercises --------

    from PrintExercises import ExercisesToStdout

    ExercisesToStdout.allExercises_stdout()

if __name__ == "__main__":
	main()