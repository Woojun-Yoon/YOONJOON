from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    t = int(input())
    a, b, c = 0, 0, 0
    while True:
        if t >= 300:
            a += 1
            t -= 300
        elif t >= 60:
            b += 1
            t -= 60
        elif t >= 10:
            c += 1
            t -= 10
        else:
            break
    
    if t == 0:
        print(a, b, c)
    else:
        print('-1')