from sys import stdin
input = stdin.readline

n = int(input())

people = []

for _ in range(n):
    people.append(list(map(int, input().split())))

for i in people:
    cache = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            cache += 1
    print(cache, end = ' ')