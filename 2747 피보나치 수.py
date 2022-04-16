from sys import stdin
input = stdin.readline

dic = [0] * 50
dic[1] = 1

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dic[n] == 0:
        dic[n] = fibo(n-1) + fibo(n-2)
        return dic[n]
    else:
        return dic[n]

n = int(input()) #테스트 개수 T
fibo(n)
print(dic[n])
