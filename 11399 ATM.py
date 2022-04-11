from sys import stdin
input = stdin.readline

n = int(input())
time = [x for x in map(int, input().split())]
time.sort()
result = 0
count = 0
for i in range(n):
    count += time[i]
    result += count

print(result)