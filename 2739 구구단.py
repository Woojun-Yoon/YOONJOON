from sys import stdin
input = stdin.readline

n = int(input())
for i in range(1,10,1):
    print(n,'*',i,'=',n * i)