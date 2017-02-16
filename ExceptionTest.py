#Author Kevin Turner CS21B
#Assignment 3 part 1
import sys

try:
    import fake
except ImportError:
    print("1. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])

class myClass():
    def test(b):
        a = 3 + b
        print('test')

try:
    myClass.test1(4)
except AttributeError:
    print("2. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])

try:
    fobj1 = open('wrong_file.txt', 'r')
except FileNotFoundError:
    print("3. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])



letter = ['a', 'b', 'c']

try:
    print(letter[3])
except IndexError:
    print("4. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])

try:
    print(letter['d'])
except TypeError:
    print("5. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])

try:
    print(Letter[1])
except NameError:
    print("6. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])

try:
    myChar = int('s')
except ValueError:
    print("7. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])

myDictonary = {'Me': 'Turner', 'Myself': 'Kevin', 'I': 'Kev'}

try:
    notIn = myDictonary['Jack']
except KeyError:
    print("8. Error Found: ", sys.exc_info()[0], sys.exc_info()[1])
finally:
    print('Made through all 8 errors!')

"""
Test run results:
1. Error Found:  <class 'ModuleNotFoundError'> No module named 'fake'
2. Error Found:  <class 'AttributeError'> type object 'myClass' has no attribute 'test1'
3. Error Found:  <class 'FileNotFoundError'> [Errno 2] No such file or directory: 'wrong_file.txt'
4. Error Found:  <class 'IndexError'> list index out of range
5. Error Found:  <class 'TypeError'> list indices must be integers or slices, not str
6. Error Found:  <class 'NameError'> name 'Letter' is not defined
7. Error Found:  <class 'ValueError'> invalid literal for int() with base 10: 's'
8. Error Found:  <class 'KeyError'> 'Jack'
Made through all 8 errors!

Process finished with exit code 0
"""