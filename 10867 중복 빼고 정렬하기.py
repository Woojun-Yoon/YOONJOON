from sys import stdin
input = stdin.readline

int(input())
nums = set(map(int, input().split()))
result = sorted(list(nums))
print(*result)