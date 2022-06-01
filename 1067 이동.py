from sys import stdin
from cmath import exp, pi
from math import log2
input = stdin.readline

# 고속푸리에변환 구현
def fft(p):
    n = len(p)
    if n == 1:
        return p
    p_even = fft(p[0::2])
    p_odd = fft(p[1::2])
    w = [exp(2j * pi * x / n) for x in range(n // 2)]
    return [p_even[x] + w[x] * p_odd[x] for x in range(n // 2)] + [p_even[x] - w[x] * p_odd[x] for x in range(n // 2)]
# inverse
def ifft(p):
    n = len(p)
    if n == 1:
        return p
    p_even = fft(p[0::2])
    p_odd = fft(p[1::2])
    w = [exp(-2j * pi * x / n) for x in range(n // 2)]
    return [p_even[x] + w[x] * p_odd[x] for x in range(n // 2)] + [p_even[x] - w[x] * p_odd[x] for x in range(n // 2)]
# 2의 제곱인지 확인
def isPowerOf2(n):
    return (n & (n - 1)) == 0


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if isPowerOf2(n):
        a = a[:] + [0] * (2 ** int(log2(n)) - 2 * n // 2)
        b = b[-1::-1] + [0] * (2 ** int(log2(n)) - 2 * n) + b[-1::-1]
        c = [0] * 2 ** int(log2(n))
        a_fft = fft(a)
        b_fft = fft(b)

        for _ in range(int(log2(n))):
            c[_] = a_fft[_] * b_fft[_]
        
        c_fft = ifft(c)
        for _ in range(int(log2(n))):
            c_fft[_] = round(c_fft[_].real / int(log2(n)))
        result = max(c_fft)
    else:
        a = a[:] + a[:]
        b = b[-1::-1] + [0] * n
        c = [0] * n * 2
        a_fft = fft(a)
        b_fft = fft(b)

        for _ in range(n * 2):
            c[_] = a_fft[_] * b_fft[_]
        
        c_fft = ifft(c)
        for _ in range(n * 2):
            c_fft[_] = round(c_fft[_].real / n)
        result = max(c_fft)
    
    print(result)