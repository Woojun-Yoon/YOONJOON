#자연수 -> 1이상의 양의 정수 , 0은 유일한 수(그냥 정수)

from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b) # 파이썬의 몫 연산자
print(a%b) #파이썬의 나머지 연산자