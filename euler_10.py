"""Project: Euler_10   Author: Kevin Radja   Date: July/25/2017.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


print('Hello')
primenumber = [2]
for x in range(2,10):
	for z in primenumber:
		print('x: ' + str(x))
		print('z: ' + str(z))
		if x % z != 0:
			primenumber.append(x) 
			break

print(primenumber)
