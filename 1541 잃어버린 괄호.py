from sys import stdin
import re
input = stdin.readline
'''
cache = input().rstrip()
cache_operator = re.split('[0-9]', cache)
cache_operator = list(filter(None, cache_operator))
cache_nums = re.split('[^0-9]', cache)

result = int(cache_nums[0])
for _ in range(len(cache_operator)):
    if cache_operator[_] == '+':
        result += int(cache_nums[_ + 1])
    else:
        result -= int(cache_nums[_ + 1])
    
print(result)
'''

cache = input().split('-')
result = 0

for i in cache[0].split('+'):
    result += int(i)
for j in cache[1:]:
    for i in j.split('+'):
        result -= int(i)

print(result)
