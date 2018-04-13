"""Project: Euler_9   Author: Kevin Radja   Date: July/20/2017.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""
a = 1
boolean = True
while boolean == True:
	a = a +1
	for b in range(1, a):
		c = (a**2 + b**2) ** 0.5
		if (c % 1) == 0:
			print(str(a) + '^2 + ' + str(b) + '^2' + ' = ' + str((a**2 + b**2) ** 0.5) + '^2')
			if c + b + a == 1000:
				print(c + b + a)
				print(c*b*a)
				boolean = False
				break
			


"""if ((a**2 + b**2) ** 0.5 % 1) == 0:
print(str(a) + '^2 + ' + str(b) + '^2' + ' = ' + str((a**2 + b**2) ** 0.5) + '^2')
print(a + b + (a**2 + b**2) ** 0.5)
boolean = False
break"""
