"""Project: Euler_7   Author: Kevin Radja   Date: July/13/2017.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number.
"""

def primenumbers():
    """By brute force create a list of prime numbers."""
    listofprime = [2, 3, 5, 7, 11, 13]
    iterate = 15
    while len(listofprime) < 10001:
        x = [iterate % x for x in listofprime]
        if 0 not in x:
            listofprime.append(iterate)
        iterate = iterate + 2
    return listofprime[-1]
print('10001th prime number')
print(primenumbers())
