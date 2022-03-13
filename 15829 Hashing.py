from sys import stdin
input = stdin.readline

l = int(input())
word = input().strip()
result = 0

for i in range(l):
    result += (ord(word[i]) - 96) * (31 ** i)

print(result % 1234567891)
