url = https://www.naukri.com/code360/problems/nth-fibonacci-number_74156

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

""" 1 way of doing it """

a = 0
b = 1

n = int(input())


for i in range(a,n):
    sum = a + b
    a = b
    b = sum

print(a)


""" 2 way of doing it"""


fib = [1,1]

n = int(input())
sum = 0
for i in range(2,n):

    a = fib[i-1]
    b = fib[i-2]

    sum = a+b
    fib.append(sum)


print(fib[n-1])











