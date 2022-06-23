from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    rope = sorted([int(input()) for _ in range(n)])
    result = 0
    count = n
    for _ in range(n):
        cache = rope[_] * count
        if cache > result:
            result = cache
        count -= 1
    
    print(result)