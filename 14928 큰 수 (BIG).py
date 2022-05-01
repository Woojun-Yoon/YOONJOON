# from sys import stdin
from decimal import Decimal, getcontext
getcontext().prec = 10 ** 6
# input = stdin.readline

print(Decimal(input()) % Decimal(20000303))

''' 6s
print(int(input()) % 20000303)
'''