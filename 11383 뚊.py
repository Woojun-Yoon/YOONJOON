from sys import stdin
input = stdin.readline

def dolm(word):
    cache = ""
    for i in word:
        cache += i + i
    return cache

n, m = map(int, input().split())
word = []
word2 = []
word_cache = []
for _ in range(n):
    word.append(input().strip())
for _ in range(n):
    word2.append(input().strip())

for i in word:
    word_cache.append(dolm(i))

if word2 == word_cache:
    print("Eyfa")
else:
    print("Not Eyfa")
