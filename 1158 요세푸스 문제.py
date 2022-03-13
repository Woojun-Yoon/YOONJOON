# 요세푸스 순열
# 덱(큐) 사용 풀이 복잡도 O(nk), O(n) 풀이는 점화식 사용
from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
num = deque([i for i in range(1,n+1)])
result = []
for i in range(n):
    for j in range(k - 1):
        num.append(num.popleft())
    result.append(str(num.popleft()))
'''
print('<', end = '')
print(*result, sep = ', ', end = '')
print('>')
'''
print('<', ', '.join(result), '>' , sep = '')