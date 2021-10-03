# Write a Python program to count the number of even and odd numbers from a series of numbers.

import math

s = (1,2,3,4,5,6,7,8,9)
b = 0
a = 0
for i in s:
    if(i % 2) == 0:
        b=b+1
    else:
        a=a+1
print('Number of even numbers :',a)
print('Number of odd numbers :',b)
