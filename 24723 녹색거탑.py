from sys import stdin
input = stdin.readline

n = int(input())
if n == 1:
    print(2)
elif n == 2:
    print(4)
elif n == 3:
    print(8)
elif n == 4:
    print(16)
else:
    print(32)