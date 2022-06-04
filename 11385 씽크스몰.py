from sys import stdin
from typing import List, Sequence
from functools import reduce
import decimal
input = stdin.readline

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
    n, m = map(int, input().split())
  
    f = list(map(int ,input().split()))
    g = list(map(int, input().split()))

    result = multipoly(f, g)
    print(reduce(lambda x, y : x ^ y, result))