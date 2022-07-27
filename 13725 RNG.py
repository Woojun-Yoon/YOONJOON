from sys import stdin
input = stdin.readline
from typing import Sequence
L = 104857601
# Kitamasa

def kitamasa(n, k, a : Sequence[int], c : Sequence[int]):
    c0 = [0] * k
    c1 = [0] * k

    if n == 0:
        return a[0]
    c0[1] = 1

    def cache1(k, c0, c1):
        c1[0] = c0[k - 1] * c[0] % L
        for _ in range(k - 1):
            c1[_ + 1] = (c0[_] + c0[k - 1] * c[_ + 1]) % L
    
    def cache2(k, c0, c1):
        d0 = [0] * k
        d1 = [0] * k
        d0[:] = c0[:]

        for _ in range(k):
            c1[_] = c0[0] * c0[_] % L
        
        for i in range(1, k):
            cache1(k, d0, d1)
            for j in range(k):
                c1[j] += c0[i] * d1[j] % L
            d0, d1 = d1, d0
        
        for _ in range(k):
            c1[_] %= L
    
    p = 32
    while (n >> p) & 1 == 0:
        p -= 1
    
    while p:
        p -= 1
        cache2(k, c0, c1)
        c0, c1 = c1, c0

        if (n >> p) & 1:
            cache1(k, c0, c1)
            c0, c1 = c1, c0
    
    return sum(c0[x] * a[x] for x in range(k)) % L





if __name__ == '__main__':
    k, n = map(int, input().split())
    an = list(map(int, input().split()))
    cn = list(map(int, input().split()))

    print(kitamasa(n, k, an[:: -1], cn))

