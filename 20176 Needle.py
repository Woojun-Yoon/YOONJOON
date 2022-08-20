from sys import stdin
from typing import List, Sequence
import decimal
input = stdin.readline
L = 30000

def multipoly(a : Sequence[int], b : Sequence[int]) -> List[int]:
    decimal.setcontext(decimal.Context(prec = decimal.MAX_PREC, Emax = decimal.MAX_EMAX))
    digit = min(20, len(str(min(len(a), len(b)) * max(a) * max(b))))
    fmat = f'0{digit}d'

    a_decimal = decimal.Decimal(''.join(format(x, fmat) for x in a))
    b_decimal = decimal.Decimal(''.join(format(x, fmat) for x in b))
    result_decimal = a_decimal * b_decimal
    l = digit * (len(a) + len(b) - 1)
    result = format(result_decimal, f'0{l}f')
    return [int(result[i : i + digit]) for i in range(0, l, digit)]

if __name__ == '__main__':
    a = int(input())
    _a = [*map(int, input().split())]
    b = int(input())
    _b = [*map(int, input().split())]
    c = int(input())
    _c = [*map(int, input().split())]

    x = [0] * 60001
    y = [0] * 60001
    for n in _a:
        x[n + L] = 1
    for _ in range(b):
        _b[_] += L
    for n in _c:
        y[n + L] = 1
    z = multipoly(x, y)

    result = 0
    for cache in _b:
        result += z[cache * 2]
    print(result)