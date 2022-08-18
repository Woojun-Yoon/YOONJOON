from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
''' 출력초과
if __name__ == '__main__':
    num = []
    n = int(input())
    for _ in range(n):
        num.append(int(input()))
    num.sort()
    cache = num[0] + num[1]
    result = num[0] + num[1]
    for _ in range(2, n):
        result += cache + num[_]
        cache = result
    print(result)
'''

if __name__ == '__main__':
    n = int(input())
    num = []
    for _ in range(n):
        heappush(num, int(input()))
    
    if len(num) == 1:
        print("0")
    else:
        result = 0
        while len(num) > 1:
            cache1 = heappop(num)
            cache2 = heappop(num)
            result += cache1 + cache2
            heappush(num, cache1 + cache2)
        print(result)