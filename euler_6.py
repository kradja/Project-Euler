"""Project: Euler_6   Author: Kevin Radja   Date: July/13/2017.

The sum of the squares of the first ten natural numbers is. (1 + 2 + ... + 10)2 = 552 = 3025 - [ 1^2 + 2^2 + ... + 10^2 = 385 ].
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def sumofsq(min, max):
    """Sum of sq."""
    listofsquares = []
    for x in range(min, max + 1):
        listofsquares.append(x * x)
    return(sum(listofsquares))

def sqofsum(min, max):
    """Square of sum."""
    x = list(range(min, max + 1))
    answer = sum(x) * sum(x)
    return(answer)


answer = sqofsum(1, 100) - sumofsq(1, 100)
print(answer)
