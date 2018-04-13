"""Program: Project Euler 3   author: Kevin Radja   date:June/29/17.

What is the largest prime factor of the number 600851475143 ?
"""

# import operator
import functools

def primenumbers(number, recurv, templist):
    """Fine all the primenumbers of a number."""
    for j in recurv:
        templist = [i for i in templist if i % j != 0]

    for x in templist:
        if not recurv:
            if number % x == 0:
                recurv.append(x)
                primenumbers(number, recurv, templist)
        if number % x == 0 and x > recurv[-1]:
            recurv.append(x)
            '''while tempnumber != 1 and tempnumber in recurv:
                if tempnumber % x == 0:
                    tempnumber = number / x
                    recurv.append(x)'''
            answer = functools.reduce(lambda x, y: x * y, recurv)
            print('answer:')
            print(answer)
            print(number)
            if answer == number:
                print('worked')
                break
            else:
                print('hi')
                primenumbers(number, recurv, templist)
    return recurv

number = 13195
start = 2


templist = list(range(2, number))
x = primenumbers(number, [], templist)
print(x)
