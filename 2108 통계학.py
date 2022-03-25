from sys import stdin
from collections import Counter
input = stdin.readline

n_list = []
n = int(input())

for _ in range(n):
    n_list.append(int(input()))

n_list.sort()
n_counter = Counter(n_list).most_common()

result1 = sum(n_list) / n
result2 = n_list[n//2]
result3 = n_counter
result4 = max(n_list) - min(n_list)

print(round(result1))
print(result2)

if len(result3) > 1 and result3[0][1] == result3[1][1]: # 중복이 있을 경우
    print(result3[1][0])
else: # 없을 경우
    print(result3[0][0])

print(result4)