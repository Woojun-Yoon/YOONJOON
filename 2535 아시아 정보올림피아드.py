from sys import stdin
input = stdin.readline

score = []
result = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    score.append((a, b, c))
score.sort(key = lambda x : x[2])
count = []
for item in score[::-1]:
    if count.count(item[0]) == 2:
        continue
    else:
        count.append(item[0])
        print(*item[:2])
    
    if len(count) == 3:
        break