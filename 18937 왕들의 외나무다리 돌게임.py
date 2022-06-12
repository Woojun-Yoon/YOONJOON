from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))

first = input().rstrip()
second = 'Whiteking' if first == 'Blackking' else 'Blackking'

grundy = 0
for cache in a:
    grundy ^= cache - 2

print(first if grundy > 0 else second)