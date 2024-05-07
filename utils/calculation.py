import datetime


class Fibonacci:
    @staticmethod
    def get_calculated_number():
        day_of_month = datetime.datetime.now().day + 1
        fib1, fib2 = 1, 1
        for _ in range(day_of_month - 2):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2