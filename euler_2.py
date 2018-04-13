"""Project: Euler_2     author: Kevin Radja     date: June/29/17.

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fib(limit):
    """Creating Fibonacci sequence."""
    fiblist = [1, 2]
    while fiblist[-1] < limit:
        fiblist.append(sum(fiblist[-2:]))
    return fiblist
fiblist = fib(4e6)
sumofeven = sum([x for x in fiblist if x % 2 == 0])
print(sumofeven)
