print('Starting Program')
import time
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''
start = time.time()
def summod(numbers_below):
    summod = []
    summod = [i for i in range(1,numbers_below) if i%3 == 0 or i%5 == 0]
    return summod

print(sum(summod(1000)))
elapsed = time.time() - start
print(elapsed)

start = time.time()
x = 1
i = 1
max = 1000
list = []
while x > 0:
    if 3*x > max - 1:
        x = -1
    else:
        if x%5 != 0:
            list.append(3*x)
    x = x +1
while i > 0:
    if 5*i > max - 1:
        i = -1
    else:
        list.append(5*i)
    i = i +1

print(sum(list))
elapsed = time.time() - start
print(elapsed)
