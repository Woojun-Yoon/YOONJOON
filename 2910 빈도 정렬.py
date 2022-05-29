from sys import stdin
from collections import Counter
input = stdin.readline

n, c = map(int, input().split())
nums = list(map(int, input().split()))

count_result = Counter(nums).most_common()
for index in range(len(count_result)):
    for _ in range(count_result[index][1]):
        print(count_result[index][0], end = ' ')