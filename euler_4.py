"""Program: Project Euler_4 Palindrome author: Kevin Radja date = June/30/2017.

A palindromic number reads the same both ways.
"""
n1 = 100
n2 = 1000

l1 = list(reversed(range(n1, n2)))
l2 = list(reversed(range(n1, n2)))
palindromes = []
numbers = []
for x in l1:
    for y in l2:
        if x >= y:
            product = str(x * y)
            if len(product) % 2 == 0:
                if product[::-1][:int(len(product) / 2)] == product[:int(len(product) / 2)]:
                    palindromes.append(product)
                    numbers.append([x, y])

print(numbers)
print(numbers[palindromes.index(max(palindromes))])
print(max(palindromes))
