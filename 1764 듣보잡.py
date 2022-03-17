# set을 이용한 교집합으로 풀이 O(min(n, m)) 소요
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
n_set = set([])
m_set = set([])
count = 0
for _ in range(n):
    n_set.add(input().rstrip())

for _ in range(m):
    m_set.add(input().rstrip())

result_set = n_set & m_set
result_set = list(result_set)
result_set.sort()

print(len(result_set))
print('\n'.join(result_set))