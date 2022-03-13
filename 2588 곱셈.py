from sys import stdin
input = stdin.readline

a = input() #세자리 자연수
b = input() #세자리 자연수
print(int(a) * int(b[2]))
print(int(a) * int(b[1]))
print(int(a) * int(b[0]))
print(int(a) * int(b))


