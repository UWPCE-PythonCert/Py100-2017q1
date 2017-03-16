
class MenuActions:

    from sys import stdout

    @staticmethod
    def quit_program(ostream=stdout):

        from BenchData import TestThat
        test_that = TestThat()
        if test_that.do():
            ostream.write(test_that.get_trace("quit_program"))
        else:
            ostream.write("The program quits. Goodbye !")
            from Signal import Signal
            sig = Signal()
            return sig.get_quit_program()