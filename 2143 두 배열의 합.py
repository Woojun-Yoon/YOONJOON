from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

if __name__ == '__main__':
    t = int(input())
    n = int(input())
    num_n = [*map(int, input().split())]
    m = int(input())
    num_m = [*map(int, input().split())]

    n_sum = []
    m_sum = []
    result = 0

    for i in range(n):
        cache = num_n[i]
        n_sum.append(cache)
        for j in range(i + 1, n):
            cache += num_n[j]
            n_sum.append(cache)
    for i in range(m):
        cache = num_m[i]
        m_sum.append(cache)
        for j in range(i + 1, m):
            cache += num_m[j]
            m_sum.append(cache)
    
    n_sum.sort(); m_sum.sort()
    for _ in range(len(n_sum)):
        left = bisect_left(m_sum, t - n_sum[_])
        right = bisect_right(m_sum, t - n_sum[_])
        result += right - left
    
    print(result)
