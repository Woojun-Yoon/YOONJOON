from sys import stdin
input = stdin.readline

n = int(input())
result = 0
def find_5(num):
    count = 0
    while(num % 5 == 0):
        num = num // 5
        count += 1
    return count

for num in range(1, n + 1):
    result += find_5(num)

print(result)  