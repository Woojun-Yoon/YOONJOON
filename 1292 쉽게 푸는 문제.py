from sys import stdin
input = stdin.readline
'''
def num_add1(n):
    cache = 0
    count = 1
    result = 0
    while cache < n:
        result += count * count
        count += 1
        cache += count - 1
    count -= 1
    result -= (cache - n) * count
    return result

def num_add2(n):
    cache = 0
    count = 1
    result = 0
    while cache < n:
        result += count * count
        count += 1
        cache += count - 1
    count -= 1
    result -= (cache - n + 1) * count
    return result

a, b = map(int, input().split())
print(num_add1(b) - num_add2(a))
'''
# 리스트 인덱싱을 이용한 풀이
num_data = []
for i in range(1, 46):
    num_data += [i] * i
a, b = map(int, input().split())
print(sum(num_data[a-1:b]))