from sys import stdin
input = stdin.readline
alphabet = [0] * 26
word = input().rstrip()

for i in word:
    alphabet[ord(i) - 97] += 1

print(*alphabet)
