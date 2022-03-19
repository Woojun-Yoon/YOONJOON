from sys import stdin
input = stdin.readline
'''
def fibo(n):
    dic = [0] * (n + 3)
    dic[0], dic[1] = 1, 2
    
    if n == 1:
        return dic[n]

    for i in range(2, n + 1):
        dic[i] = (dic[i - 1] + dic[i - 2]) % 15746
    
    return dic[n]

n = int(input())
print(fibo(n - 1))
'''
# 더 쉬운 풀이

def fibo(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
        if a >= 15746:
            a, b = a % 15746, b % 15746
    return a

n = int(input())
print(fibo(n))