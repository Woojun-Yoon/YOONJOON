from sys import stdin
input = stdin.readline

x = int(input())
a = 0
n = 1
while True:
    a = a + n
    if x <= a:
        break
    else:
        n += 1

if (n % 2) != 0: # n은 홀수 일 경우
    cache = a - x
    print(1+cache,'/',n-cache,sep='')
else: # n은 짝수 일 경우
    cache = a - x
    print(n-cache,'/',1+cache,sep='')