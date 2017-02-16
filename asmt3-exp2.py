#Author Kevin Turner CS21B
#Assignment 3 experiment 2
import sys

def arithmSeries(number):
    if number == 0:
        return 1        # this is called the trivial case
    elif number >1:
        return number + arithmSeries(number-1)  # here is the recursive call
    else:
        return 1

if __name__ == "__main__":

    try:
        arithmSeries(11000)
    except RecursionError:
        print("Error Found: ", sys.exc_info()[0], sys.exc_info()[1])
    finally:
        sys.setrecursionlimit(25000)
        print("After exceeding stack size : ", arithmSeries(21000))

"""
Test run results:
Error Found:  <class 'RecursionError'> maximum recursion depth exceeded in comparison

Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)

"""