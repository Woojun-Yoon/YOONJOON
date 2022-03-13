from sys import stdin
input = stdin.readline

a = int(input())
b = int(input())
c = int(input())
n = a * b * c
result = list(str(n))

'''
result = list(map(int, result))

for i in range(10): # 0 ~ 9
    cache = 0
    for j in range(len(result)):
        if result[j] == i:
            cache += 1
    print(cache)
'''

for i in range(10):
    print(result.count(str(i))) #list의 count 함수를 이용한 풀이법
