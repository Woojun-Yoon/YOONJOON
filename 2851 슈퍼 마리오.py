# 브루트포스 알고리즘
from sys import stdin
input = stdin.readline

result = 0
result1 = 200
num_list = []
for i in range(10):
    num_list.append(int(input()))

for j in range(10):
    if result + num_list[j] < 100:
        result += num_list[j]
    else:
        result1 = result + num_list[j]
        break


if (100 - result) < (result1 - 100):
    print(result)
else:
    print(result1)