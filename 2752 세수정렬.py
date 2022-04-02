from sys import stdin
input = stdin.readline

num = list(map(int, input().split()))
num.sort()
print(*num)
