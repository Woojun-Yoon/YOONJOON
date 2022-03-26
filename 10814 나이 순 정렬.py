from sys import stdin
input = stdin.readline

n = int(input())

people = []
for i in range(n):
    age_name = list(input().split())
    people.append(age_name)
    people[i][0] = int(people[i][0])
people.sort(key = lambda x : x[0])

for j in range(n):
    print(*people[j])