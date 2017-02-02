from unittest import TestCase


class TestGrid_printer(TestCase):



    def test_print_grid(self):

        from grid_printer import print_grid, print_grid2
        from TestsData import GridTestsStr
        import io

        # Exercise part 1

        gridStrStream = io.StringIO()
        print_grid(ostream = gridStrStream)
        self.assertEqual(gridStrStream.getvalue(), GridTestsStr['grid1'])
        del gridStrStream


        # Exercise part 2

        gridStrStream = io.StringIO()
        print_grid(size = 3, ostream = gridStrStream)
        self.assertEqual(gridStrStream.getvalue(), GridTestsStr['grid2'])
        del gridStrStream

        gridStrStream = io.StringIO()
        print_grid(size = 15, ostream = gridStrStream)
        self.assertEqual(gridStrStream.getvalue(), GridTestsStr['grid3'])
        del gridStrStream



    def test_print_grid2(self):

        from grid_printer import print_grid, print_grid2
        from TestsData import GridTestsStr
        import io

        # Exercise part 3

        gridStrStream = io.StringIO()
        print_grid2(numRowsCols=3, cellSize=4, ostream=gridStrStream)
        self.assertEqual(gridStrStream.getvalue(), GridTestsStr['grid4'])
        del gridStrStream

        gridStrStream = io.StringIO()
        print_grid2(numRowsCols=5, cellSize=3, ostream=gridStrStream)
        self.assertEqual(gridStrStream.getvalue(), GridTestsStr['grid5'])
        del gridStrStream
