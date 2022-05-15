from sys import stdin
from collections import Counter
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    item = []
    for i in range(n):
        a, b = input().split()
        item.append(b)
    item_count = Counter(item)
    result = 1
    for j in item_count:
        result *= item_count[j] + 1
    print(result - 1)