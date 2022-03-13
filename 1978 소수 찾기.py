# 에라토스테네스의 체
import math
from sys import stdin
input = stdin.readline

list_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # 97**2 = 9409까지 소수 판별 가능
n = int(input())
list_n = list(map(int, input().split()))
result_cache = 0

for i in list_n:
    if i in list_100:
        result_cache += 1
    elif i == 1:
        pass
    else:
        cache = 0
        for j in list_100:
            if (i % j) == 0:
                cache += 1
        if cache == 0:
            result_cache += 1
print(result_cache)

# 숏코딩
# all()은 리스트 값 안에 0이나 공백 있을시 False 출력, 아닐 시 True 출력
'''
input()
m = map(int, input().split())
print(sum(all(n % i for i in range(2, n)) * n > 1 for n in m))
'''
'''
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함

print(is_prime_number(26))
'''
