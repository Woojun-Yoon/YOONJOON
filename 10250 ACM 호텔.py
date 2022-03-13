from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    w_cache = n // h
    h_cache = n % h
    if h >= n:
        print('%d01' %(n))    
    else:
        if h_cache == 0:
            if w_cache <= 9:
                print('%d0%d' %(h, w_cache))
            else:
                print('%d%d' %(h, w_cache))
        else:
            if w_cache < 9:
                print('%d0%d' %(h_cache, w_cache + 1))
            else:
                print('%d%d' %(h_cache, w_cache + 1))