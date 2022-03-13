from sys import stdin
input = stdin.readline

N = int(input())
test_result = list(map(int, input().split()))
M = max(test_result)
result_sum = 0
for i in range(N):
    result_sum += test_result[i]

cheat_result = (100 * result_sum / M) / N
print(cheat_result)
