from sys import stdin
input = stdin.readline

result = 0
n = int(input())

for _ in range(n):
    s = input().strip()
    cache = 0
    for i in range(len(s)):
        try:
            a =  s.index(s[i],i + 1)
        except ValueError:
            continue
        else:
            if a >= (i + 2):
                cache +=1
    if cache == 0: result += 1
print(result)
'''
print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)
'''