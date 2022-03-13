from sys import stdin
input = stdin.readline

a, b, v = map(int, input().split())

if a == v:
    print(1)
else:
    v_cache = v - a
    up_down = a - b
    if v_cache % up_down == 0:
        print((v_cache // up_down) + 1)
    else:
        print((v_cache // up_down) + 2)

