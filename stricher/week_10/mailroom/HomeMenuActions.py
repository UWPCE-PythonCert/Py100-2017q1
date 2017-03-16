
#TODO: complete/update


from MenuActions import MenuActions


class HomeMenuActions(MenuActions):

    from sys import stdout

    @staticmethod
    def thank_you(ostream=stdout):

        from BenchData import TestThat
        test_that = TestThat()
        if test_that.do():
            ostream.write(test_that.get_trace("thank_you"))
        else:
            pass

    @staticmethod
    def create_report(ostream=stdout):

        from BenchData import TestThat
        test_that = TestThat()
        if test_that.do():
            ostream.write(test_that.get_trace("create_report"))
        else:
            from TextGenerator import ReportGenerator
            #TODO: improve, refactor ...
            ReportGenerator.print_report(ostream)
