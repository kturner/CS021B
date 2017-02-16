#Author Kevin Turner CS21B
#Test stuff for class
'''Arithmetic Game (easyMath.py) :
Randomly chooses numbers and an arithmetic function, displays the question, and
verifies the results. Shows answer after three wrong tries and does not continue
until the user enters the correct answer.
'''
"""
from operator import add, sub
from random import randint, choice
ops = {'+': add, '-': sub}
MAXTRIES = 2

def doprob():
    op = choice('+-')#random choice
    nums = [randint(1,10) for i in range(2)]#list generates number in loop
    nums.sort(reverse=True) #if reverse sort
    ans = ops[op](*nums) #random gererator to pick + or -  ops is the dictonary above
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print('sorry, the answer is\n%s%d'%(pr, ans))
                break
            else:
                print('incorrect... try again')
            oops += 1
        except (KeyboardInterrupt, \
            EOFError, ValueError):
            print('invalid input... try again')

def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
"""

"""
def newfoo(arg1, arg2, *nonkw, **kw): # * tuple (non-keyword), ** dictionary
    '''display regular args and all variable args'''
    print('arg1 is:', arg1)
    print('arg2 is:', arg2)
    for eachNONKW in nonkw:
        print('additional non-keyword arg:', eachNONKW)
    for eachKW in kw.keys():
        print("additional keyword arg '%s': %s" % (eachKW, kw[eachKW]))

newfoo('wolf', 3, 'projects', freud=90, gamble=96)
"""

"""
from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func()
    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(2)
for i in range(2):
    sleep(1)
    foo()
"""

"""
from random import randint
def pickOdd(n):
    return n % 2

allNums = []
for eachNum in range(9): #[ri(1,99) for i in range(9)]
    allNums.append(randint(1, 99))

print('Complete list: ',allNums)
print('Filtered list: ',list(filter(pickOdd, allNums)))
"""

"""
#Use list comprehension twice
from random import randint as ri #ri is local var for randint

print('\n' 'Use list comprehension twice')
print('Filtered list: ',[n for n in [ri(1,99) for i in range(9)] if n%2])
"""

"""
#Single Sequence
print(list(map((lambda x: x + 2), [0, 1, 2, 3, 4, 5])))
print(list(map(lambda x: x ** 2, range(6))))
print([x + 2 for x in range(6)])
print([x ** 2 for x in range(6)])

#Multiple Sequences
print('\n', list(map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6])))
print(list(map(lambda x, y: (x + y, x - y), [1, 3, 5], [2, 4, 6])))
print(list(zip([1, 3, 5], [2, 4, 6])))
"""

"""
from functools import reduce

print(reduce( (lambda x, y: x * y), [1, 2, 3, 4] ))
print(reduce( (lambda x, y: x / y), [1, 2, 3, 4] ))
"""

"""
#PARTIAL FUNCTION APPLICATION (PFA)
from functools import partial

myBin = input("Please enter a binary number:")

basetwo = partial(int, base=2)
print(basetwo(myBin))
"""

"""
from operator import add, mul
from functools import partial
add1 = partial(add, 1) # add1(x) == add(1, x)
mul100 = partial(mul, 100) # mul100(x) == mul(100, x)
print(add1(7))
print(mul100(8))
"""

"""
#Closure not working, address error
def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr
"""

"""
#Generator
def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


count = counter(5)
print('\nuse send() and close():')
print(next(count))
print(next(count))
print(next(count))
count.send(9)
print(next(count))
count.close()

#print(next(count))# will give an error since the generator is complete
"""

stuff = ['computer', 'a', 2, 3.14, 'pen']
def findStuff(stuff):
    for value in stuff:
            yield value

fs = findStuff(stuff)
for x in fs:
    print(x)
    if x == 3.14:
        fs.close()


"""
amount = int(input('Give amount: '))


def fib():
    a = 0
    b = 1
    while 1:
        yield a
        b += a
        yield b
        a += b

mygen = fib()
next(mygen)

for i in range(amount):
    print(next(mygen))
"""

#Author Kevin Turner CS21B
#Test stuff for class
'''Arithmetic Game (easyMath.py) :
Randomly chooses numbers and an arithmetic function, displays the question, and
verifies the results. Shows answer after three wrong tries and does not continue
until the user enters the correct answer.
'''
"""
from operator import add, sub
from random import randint, choice
ops = {'+': add, '-': sub}
MAXTRIES = 2

def doprob():
    op = choice('+-')#random choice
    nums = [randint(1,10) for i in range(2)]#list generates number in loop
    nums.sort(reverse=True) #if reverse sort
    ans = ops[op](*nums) #random gererator to pick + or -  ops is the dictonary above
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print('sorry, the answer is\n%s%d'%(pr, ans))
                break
            else:
                print('incorrect... try again')
            oops += 1
        except (KeyboardInterrupt, \
            EOFError, ValueError):
            print('invalid input... try again')

def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
"""

"""
def newfoo(arg1, arg2, *nonkw, **kw): # * tuple (non-keyword), ** dictionary
    '''display regular args and all variable args'''
    print('arg1 is:', arg1)
    print('arg2 is:', arg2)
    for eachNONKW in nonkw:
        print('additional non-keyword arg:', eachNONKW)
    for eachKW in kw.keys():
        print("additional keyword arg '%s': %s" % (eachKW, kw[eachKW]))

newfoo('wolf', 3, 'projects', freud=90, gamble=96)
"""

"""
from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func()
    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(2)
for i in range(2):
    sleep(1)
    foo()
"""

"""
from random import randint
def pickOdd(n):
    return n % 2

allNums = []
for eachNum in range(9): #[ri(1,99) for i in range(9)]
    allNums.append(randint(1, 99))

print('Complete list: ',allNums)
print('Filtered list: ',list(filter(pickOdd, allNums)))
"""

"""
#Use list comprehension twice
from random import randint as ri #ri is local var for randint

print('\n' 'Use list comprehension twice')
print('Filtered list: ',[n for n in [ri(1,99) for i in range(9)] if n%2])
"""

"""
#Single Sequence
print(list(map((lambda x: x + 2), [0, 1, 2, 3, 4, 5])))
print(list(map(lambda x: x ** 2, range(6))))
print([x + 2 for x in range(6)])
print([x ** 2 for x in range(6)])

#Multiple Sequences
print('\n', list(map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6])))
print(list(map(lambda x, y: (x + y, x - y), [1, 3, 5], [2, 4, 6])))
print(list(zip([1, 3, 5], [2, 4, 6])))
"""

"""
from functools import reduce

print(reduce( (lambda x, y: x * y), [1, 2, 3, 4] ))
print(reduce( (lambda x, y: x / y), [1, 2, 3, 4] ))
"""

"""
#PARTIAL FUNCTION APPLICATION (PFA)
from functools import partial

myBin = input("Please enter a binary number:")

basetwo = partial(int, base=2)
print(basetwo(myBin))
"""

"""
from operator import add, mul
from functools import partial
add1 = partial(add, 1) # add1(x) == add(1, x)
mul100 = partial(mul, 100) # mul100(x) == mul(100, x)
print(add1(7))
print(mul100(8))
"""

"""
#Closure not working, address error
def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr
"""

"""
amount = int(input('Give amount: '))


def fib():
    a = 0
    b = 1
    while 1:
        yield a
        b += a
        yield b
        a += b

mygen = fib()
next(mygen)

for i in range(amount):
    print(next(mygen))
"""

"""
seconds =  int(input('Please enter the number of seconds to convert: '))

m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
mo, d = divmod(d, 30.4)
y, mo = divmod(mo, 12)
print ("%s%d%s%d%s%d%s%d%s%02d%s%02d%s" %
       ("Convert ", seconds, " Seconds to: ", y, " Years ", mo, " Months ", h," Hours ", m, " Minutes ", s, " Seconds"))
"""

"""
myTuple = (1, 2, 3, 4, 5)
if 2 in myTuple:
    print(2)


def eatHowManyAnimals(number=7, animal='cow'):
    print('Eat %i %ss every week.' % (number, animal))
    return None

eatHowManyAnimals(animal='chikin')

eatHowManyAnimals(animal='chikin', number=6)
"""

"""
myList = ["myitem", 'youritem', 'someone elses item']
for i in myList:
    print(', '.join(myList))
    if "myitem" in myList:

def testYield():
    myList = ["myitem", 'youritem', 'someone elses item']
    print(myList[0])
    for item in myList:
        print(myList[0])
        if  myList[0] is  "myitem":
            print("myitem")
            #yield


#print()
#testYield.item.send(count.close())
#count.send(9)
#print(next(count))
#count.close()
"""
"""
e1 = "Frank", "Intern"
e2 = "John", "DOE"
e3 = "Fred", "Nu"
e4 = "John", "DOE"

def __eq__(self, other):
    return self.firstName.lower() == other.firstName.lower() and \
           self.lastName.lower() == other.lastName.lower()

def match(emp1, emp2):
    if emp1 == emp2:
        print(emp1, "Is a match for", emp2)
    else:
        print(emp1, "Not a match for", emp2)

print("")
match(e1, e2)

print("\n")
match(e3, e4)

print("\n")
match(e2, e4)
"""

"""
#Generator
def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


count = counter(5)
print('\nuse send() and close():')
print(next(count))
print(next(count))
print(next(count))
count.send(9)
print(next(count))
count.close()

#print(next(count))# will give an error since the generator is complete
"""

"""
#not working foo.close no attribute
def foo():
    yield 'one'
    yield 'two'
    yield 'three'
    yield 'four'
    yield 'five'

for num in foo():
    if num == 'three':
        print('three')
        foo.close()
    else:
        print('not three')
"""