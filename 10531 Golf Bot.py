from sys import stdin
from typing import List, Sequence
import decimal
input = stdin.readline

def fft(a : Sequence[int], b : Sequence[int]) -> List[int]:
    decimal.setcontext(decimal.Context(prec = decimal.MAX_PREC, Emax = decimal.MAX_EMAX))
    digit = 20
    fmat = f'0{digit}d'

    a_decimal = decimal.Decimal(''.join(format(x, fmat) for x in a))
    b_decimal = decimal.Decimal(''.join(format(x, fmat) for x in b))
    result_decimal = a_decimal * b_decimal
    l = digit * (len(a) + len(b) - 1)
    result = f'{result_decimal : 0{l}f}'
    return [int(result[i : i + digit]) for i in range(0, l, digit)]


if __name__ == '__main__':
    n = int(input())
    k = [int(input()) for _ in range(n)]
    m = int(input())
    d = [int(input()) for _ in range(m)]
    
    max_d = max(d)
    cache = [1] + [0] * max_d

    for index in k:
        if index <= max_d:
            cache[index] = 1
    
    fft_result = fft(cache, cache)
    result = sum(1 for index in d if fft_result[index] > 0)
    print(result)
