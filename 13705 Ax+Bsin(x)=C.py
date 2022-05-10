# 보다 정확한 sin(x)의 값이 필요함 -> 테일러 급수 -> 매클로린 급수

from sys import stdin
from decimal import *
import math
getcontext().prec = 100
getcontext().rounding = ROUND_HALF_UP
input = stdin.readline


# a, b, c = map(int, input().split())
x = input().rstrip()

def sin(x): # x = Decimal(x)
    how_much = Decimal(1)
    count = 0
    result = Decimal(0)
    while (abs(how_much) > (10) ** (-60)):
        how_much = Decimal((x ** Decimal(2 * count + 1)) / Decimal(math.factorial(2 * count + 1)))
        count += 1
    print(count)
    for k in range(count + 1):
        result += Decimal(((-1) ** k) * Decimal((x ** Decimal(2 * k + 1)) / Decimal(math.factorial(2 * k + 1))))
    if result < 0:
        k = k + 1
        result += Decimal(((-1) ** k) * Decimal((x ** Decimal(2 * k + 1)) / Decimal(math.factorial(2 * k + 1))))

    print(result)


sin(Decimal(x))





'''
getcontext().prec = 1000
print(Decimal(str(math.sin(x))))
'''