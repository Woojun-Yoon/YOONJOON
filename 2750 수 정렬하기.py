from sys import stdin
input = stdin.readline
print(*sorted([int(input()) for _ in range(int(input()))]), sep = '\n')