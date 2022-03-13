import math
from sys import stdin
input = stdin.readline

# 소수 판별 함수
def prime_num(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1): #제곱근 까지만 소수 판별
        if x % i == 0:
            return False 
    return True #for문 종료까지 False리턴 안될 시 True 리턴

prime_list = []
m = int(input()); n = int(input()) # m <= n
for i in range(m,n+1,1):
    if prime_num(i):
        prime_list.append(i)

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))