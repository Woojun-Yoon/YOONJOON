from sys import stdin
input = stdin.readline

num = int(input().rstrip(), 8)
print(bin(num)[2:])