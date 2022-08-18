from sys import stdin
from collections import deque
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = deque([[n]])
    result = []

    while nums:
        a = nums.popleft()
        x = a[0]

        if x == 1:
            result = a
            break
        
        if x % 3 == 0:
            nums.append([x // 3] + a)
        
        if x % 2 == 0:
            nums.append([x // 2] + a)
        
        nums.append([x - 1] + a)
    
    print(len(result) - 1)
    print(*result[::-1])