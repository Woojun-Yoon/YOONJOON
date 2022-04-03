from sys import stdin
input = stdin.readline

m = int(input())
result = 0
change = 1000 - m
while (change != 0):
    if change >= 500:
        change -= 500
        result += 1
    elif change >= 100:
        change -= 100
        result += 1
    elif change >= 50:
        change -= 50
        result += 1
    elif change >= 10:
        change -= 10
        result += 1
    elif change >= 5:
        change -= 5
        result += 1
    else:
        change -= 1
        result += 1

print(result)
