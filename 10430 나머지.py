from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
# 5~6 출력값이 서로 같음
# 7~8 출력값이 서로 같음