from sys import stdin
input = stdin.readline

max_list = []

for _ in range(9):
    cache = int(input())
    max_list.append(cache)

max_number = max(max_list)
print(max_number)
print(max_list.index(max_number) + 1)

'''
for i in range(9):
    if max_list[i] == max_number:
        print(i+1)
'''
# list.index(obj)를 통한 풀이 가능