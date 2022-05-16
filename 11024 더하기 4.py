from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    print(sum(nums))