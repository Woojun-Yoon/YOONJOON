from sys import stdin
input = stdin.readline

n = int(input())
number_list = input()
sum_result = 0 
for i in range(n):
    sum_result += int(number_list[i])
print(sum_result)

