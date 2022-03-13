from sys import stdin
input = stdin.readline

n = int(input())
num = list(map(int, input().split()))
result = []
for i in num:
    if i == int(i ** 0.5) ** 2: # 제곱근인 경우
        result.append('1')
    else:
        result.append('0')
print(' '.join(result))