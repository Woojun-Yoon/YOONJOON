from sys import stdin
input = stdin.readline
# 97 ~ 122, a ~ z
s = input().strip() # str
cache = []
for i in range(97,123,1):
    if chr(i) in s:
        cache.append(s.index(chr(i)))
    else:
        cache.append(-1)
print(*cache)