from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

n, m = map(int, input().split())
turn_q = deque([i for i in range(1, n + 1)])
nums = list(map(int, input().split()))
result_count = 0
for num in nums:
    left_q = deepcopy(turn_q)
    right_q = deepcopy(turn_q)
    left_count = 0
    right_count = 0
    while(num != left_q[0]):
        left_q.append(left_q.popleft())
        left_count += 1
    left_q.popleft()
    while(num != right_q[0]):
        right_q.appendleft(right_q.pop())
        right_count += 1
    right_q.popleft()
    if left_count > right_count:
        result_count += right_count
        turn_q = right_q
    else:
        result_count += left_count
        turn_q = left_q
print(result_count)

