from sys import stdin
input = stdin.readline
# Sprague-Grundy Theorem
n = int(input())
nums = list(map(int, input().split()))
result = 0
check = 0
for _ in range(n):
    if nums[_] == 1:
        check += 1

if check == n:
    if n % 2 == 0:
        print('koosaga')
    else:
        print('cubelover')
else:
    if check > 0 and check % 2 == 0:
        for _ in range(n):
            if nums[_] != 1:
                nums[_] = 1
                break
    for _ in range(n):
        result ^= nums[_]
    
    if result != 0:
        print('koosaga')
    else:
        print('cubelover')
