from sys import stdin
input = stdin.readline

R1, S = map(int, input().split())
R2 = (S * 2) - R1
print(R2)