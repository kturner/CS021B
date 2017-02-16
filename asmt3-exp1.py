#Author Kevin Turner CS21B
#Assignment 3 experiment 1
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
        arithmSeries(1100)
    except RecursionError:
        print("Error Found: ", sys.exc_info()[0], sys.exc_info()[1])
    finally:
        sys.setrecursionlimit(1200)
        print("After setting limit to 1200: ", arithmSeries(1100))

"""
Test run results:

Error Found:  <class 'RecursionError'> maximum recursion depth exceeded in comparison
After setting limit to 1200:  605550

Process finished with exit code 0

Test run results before increasing recursion limit:
Error Found:  <class 'RecursionError'> maximum recursion depth exceeded in comparison

Process finished with exit code 0
"""