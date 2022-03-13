from sys import stdin
input = stdin.readline
'''
def FactCheck(word, cache_word):
    cache_list = []
    for i in range(len(word)):
        if word[i] != cache_word[i]:
            cache_list.append(i)
    return cache_list
            
T = int(input())
com_word = input()
cache_index = set()
for _ in range(T - 1):
    word = input()
    cache_index.update(FactCheck(com_word, word))
com_words = list(com_word)
for i in list(cache_index):
    com_words[i] = '?'
del com_words[-1]
print(*com_words, sep = '')
'''

n = int(input())
a = [input().strip() for i in range(n)]

res = ""
l = len(a[0])
for i in range(l):
    c = 0
    s = a[0][i]
    for j in range(1, n):
        if s == a[j][i]:
            c += 1
    if c == n - 1:  res += s
    else:   res +='?'
print(res)
# 더 빠른 풀이