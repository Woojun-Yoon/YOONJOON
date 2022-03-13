from re import A
from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
cache = a * b
if a < b:
    n = a
    a = b
    b = n

while(b != 0):
    n = a % b
    a = b
    b = n

print(a)
print(cache // a)