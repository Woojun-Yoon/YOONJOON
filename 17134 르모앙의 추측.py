from sys import stdin
from typing import List, Sequence
import decimal
import math
input = stdin.readline

def prime_list(a: int, b: int = -1) -> list[int]:
    beg, end = (1, a + 1) if b < 0 else (min(a, b), max(a, b) + 1)
    if end < 5:
        return [i for i in range(beg, end) if i in (2, 3)]
    n = end + 6 - end % 6
    sieve = [False] + [True] * (n // 3 - 1)
    for i in range(math.isqrt(n) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | 3 * i + 1) * 2, k * k, k * (k + 4 - 2 * (i & 1))
            sieve[s // 3::d] = [False] * ((n // 6 - s // 6 - 1) // k + 1)
            sieve[j // 3::d] = [False] * ((n // 6 - j // 6 - 1) // k + 1)
    b, e = (beg | 1) // 3, n // 3 - 2 + (end % 6 > 1)
    return ([p for p in (2, 3) if p >= beg] +
            [1 | 3 * i + 1 for i in range(b, e) if sieve[i]])

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
    T = int(input())
    num = [int(input()) for _ in range(T)]
    # find p + 2 * q = n, (p, q)
    _max = max(num)
    a = [0] * (_max + 1)
    b = [0] * (_max + 1)
    for p in prime_list(_max):
        a[p] = 1
        if 2 * p < _max:
            b[2 * p] = 1
    c = multipoly(a, b)
    print(*(c[_] for _ in num), sep = '\n')
