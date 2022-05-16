from sys import stdin
from decimal import *
input = stdin.readline

getcontext().prec = 400
for _ in range(int(input())):
    n = Decimal(input())
    getcontext().rounding = ROUND_HALF_UP # 사사오입
    result = round(n ** (Decimal(1) / Decimal(3)), 200)
    # result = n ** (Decimal(1) / Decimal(3))
    print(result)
    getcontext().rounding = ROUND_FLOOR # 버림
    result = round(result, 10)
    print(result)