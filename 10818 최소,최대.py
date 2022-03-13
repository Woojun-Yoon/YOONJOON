from sys import stdin
input = stdin.readline

n = int(input())
cache = list(map(int,input().split()))
print(min(cache), max(cache))