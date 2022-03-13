from sys import stdin
input = stdin.readline

n = int(input())
a = 1
t = 1
while True:
    a = a + ((t - 1) * 6)
    if n <= a:
        break
    else:
        t += 1
print(t)