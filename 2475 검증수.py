from sys import stdin
input = stdin.readline

num_list = list(map(int, input().split()))
print(sum(num ** 2 for num in num_list) % 10)