from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n, c = map(int, input().split())
    m = int(input())
    truck = [c] * (n + 1)
    q = []
    count = 0
    for _ in range(m):
        q.append([*map(int, input().split())])
    
    q.sort(key = lambda x : (x[1]))
    
    for start, end, box in q:
        _min = c
        for _ in range(start, end):
            _min = min(_min, truck[_])
        _min = min(_min, box)
        for _ in range(start, end):
            truck[_] -= _min
        count += _min
    
    print(count)
