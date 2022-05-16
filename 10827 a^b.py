from sys import stdin
from decimal import *
input = stdin.readline
getcontext().prec = 1200
a, b = map(Decimal, input().split())
print(format(a ** b, 'f'))