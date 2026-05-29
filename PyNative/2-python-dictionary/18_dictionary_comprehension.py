# Write a Python program to generate a dictionary of the squares of numbers from 1 to 10 using a dictionary comprehension in a single line.

n = 10
sqr = {}

for i in range(1, n+1):
    sqr[i] = i*i

print(sqr)