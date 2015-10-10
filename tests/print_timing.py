# borrowed/modified from https://www.daniweb.com/programming/software-development/code/216610/timing-a-function-python

import time

def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print('%s took %0.3fms' % (func.__name__, (t2-t1)*1000.0))
        return res
    return wrapper