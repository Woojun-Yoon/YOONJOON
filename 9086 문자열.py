from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    word = input().rstrip()
    print(word[0], word[-1], sep = '')