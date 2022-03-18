from sys import stdin
input = stdin.readline
result = 0
for _ in range(5):
    grade = int(input())
    if grade <= 40:
        result += 40
    else:
        result += grade
print(result // 5)
