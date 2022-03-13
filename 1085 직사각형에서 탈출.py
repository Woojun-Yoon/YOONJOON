from sys import stdin
input = stdin.readline

x, y, w, h = map(int, input().split())
print(min([x, y, w - x, h - y]))
