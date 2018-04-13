"""Project: Euler_5   Author: Kevin Radja   Date: July 12th 2017.

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def divisible(min, max):
    """By brute force checks and iterates the largest number that is divisible by the range of numbers."""
    answer = max + max
    print(max)
    min = int(round(max / 2 + 1))
    print(min)
    l = [1, 2]
    while l[-1] is not l[-2]:
        l.append(answer)
        for x in range(min, max + 1):
            if answer % x is not 0:
                answer = answer + max
                break
    return l[-1]
print(divisible(1, 20))

"""def changerange(min, max):
Finding the best range
    list = []
    l = []
    temp = max
    count = 0
    while temp > 1:
        l = []
        for i in range(min, max + 1):
            if temp % i is not 0:
                l.append(i)
        l.append(temp)
        list.append(l)
        print(temp)
        print(list[count])
        temp = temp - 1
        count = count + 1
    return list

newlist = changerange(1, 99)
newlist = set.intersection(*map(set,newlist))
print(newlist)"""
