from sys import stdin, maxsize
input = stdin.readline

def dis(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

if __name__ == '__main__':
    n = int(input())
    p = []
    _max = maxsize
    result = 0

    for _ in range(n):
        p.append([*map(int, input().split())])
    
    for i in range(n):
        check = -1
        cache = 0
        for j in range(n):
            d = dis(p[i], p[j])
            if check < d:
                check = d
                cache = i

        if check < _max:
            _max = check
            result = cache
    print(*p[result])
