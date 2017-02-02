# Fibonacci series
# f(n)  | = 0 if n == 0
#       | = 1 if n == 1
#       | = f(n-1) + f(n-2) ; otherwise

class Fibonacci:
    @staticmethod
    def iter(n: int) -> int:
        """Computes the nth value in the fibonacci series using iteration.

        Args:
            n: non negative index in the fibonacci series

        Returns:
            The nth value in the fibonacci series
        """
        if n < 0:
            raise ValueError("Fibonacci.iter(n) - n must be non negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        f_n_2 = 0
        f_n_1 = 1
        for ii in range(2, n + 1):
            f_n = f_n_2 + f_n_1
            f_n_2 = f_n_1
            f_n_1 = f_n
        return f_n

    @staticmethod
    def recurs(n: int) -> int:
        """Computes the nth value in the fibonacci series using recursion.

        Args:
            n: non negative index in the fibonacci series

        Returns:
            The nth value in the fibonacci series
        """
        if n < 0:
            raise ValueError("Fibonacci.recurs(n) - n must be non negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return Fibonacci().recurs(n - 2) + Fibonacci().recurs(n - 1)


# Lucas series:
# f(n)  | = 2 if n == 0
#       | = 1 if n == 1
#       | = f(n - 2) + f(n - 1) ; otherwise

class Lucas:
    @staticmethod
    def iter(n: int) -> int:
        """Computes the nth value in the Lucas series using iteration.

        Args:
            n: non negative index in the Lucas series

        Returns:
            The nth value in the Lucas series
        """
        if n < 0:
            raise ValueError("Lucas.iter(n) - n must be non negative")
        if n == 0:
            return 2
        if n == 1:
            return 1
        ii = 2
        f_n_2 = 2
        f_n_1 = 1
        while ii <= n:
            f_n = f_n_2 + f_n_1
            f_n_2 = f_n_1
            f_n_1 = f_n
            ii += 1
        return f_n

    @staticmethod
    def recurs(n: int) -> int:
        """Computes the nth value in the Lucas series using recursion.

        Args:
            n: non negative index in the Lucas series

        Returns:
            The nth value in the Lucas series
        """
        if n < 0:
            raise ValueError("Lucas.recurs(n) - n must be non negative")
        if n == 0:
            return 2
        if n == 1:
            return 1
        return Lucas().recurs(n - 2) + Lucas().recurs(n - 1)


class sum_series:
    @staticmethod
    def iter(n: int, f_0=0, f_1=1) -> int:
        """Computes the nth value in the sum f(n - 2) + f(n - 1) series
        given f(0) and f(1) using iteration.

        Args:
            n: non negative index in the sum series
            f_0 (:obj:`int`, optional): the value of f_0. Default to 0
            f_1 (:obj:`int`, optional): the value of f_1. Default to 1

        Returns:
            The nth value in the sum series
        """
        if n < 0:
            raise ValueError("sum_series.iter(n) - n must be non negative")
        if n == 0:
            return f_0
        if n == 1:
            return f_1
        f_n_2 = f_0
        f_n_1 = f_1
        for ii in range(2, n + 1):
            f_n = f_n_2 + f_n_1
            f_n_2 = f_n_1
            f_n_1 = f_n
        return f_n

    @staticmethod
    def recurs(n: int, f_0=0, f_1=1) -> int:
        """Computes the nth value in the sum f(n - 2) + f(n - 1) series
        given f(0) and f(1) using recursion.

        Args:
            n: non negative index in the sum series
            f_0 (:obj:`int`, optional): the value of f_0. Default to 0
            f_1 (:obj:`int`, optional): the value of f_1. Default to 1

        Returns:
            The nth value in the sum series
        """
        if n < 0:
            raise ValueError("sum_series.recurs(n) - n must be non negative")
        if n == 0:
            return f_0
        if n == 1:
            return f_1
        return sum_series().recurs(n - 2, f_0, f_1) + sum_series().recurs(n - 1, f_0, f_1)
