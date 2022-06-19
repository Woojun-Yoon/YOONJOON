from sys import stdin
input = stdin.readline

word = input().rstrip()
for _ in word:
    if _.isupper():
        print(_.lower(), end = '')
    else:
        print(_.upper(), end = '')
