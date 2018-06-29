from time import sleep
import timeit


def logger(message=None):

    def sleep_decorator(function):
        """
        Limits how fast the function is
        called.
        """

        def wrapper(*args, **kwargs):
            print('[INFO]:', message if message else 'logging')
            return "your number is: {}".format(function(*args, **kwargs))
        return wrapper
    return sleep_decorator


@logger(message='power')
def print_number(num):
    return num


print(print_number(222))

for num in range(1, 6):
    print(print_number(num))
