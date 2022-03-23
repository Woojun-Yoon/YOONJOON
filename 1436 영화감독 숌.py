from sys import stdin
input = stdin.readline

n = int(input())
count = 0
list666 = []
while True:
    if len(list666) > n:
        break

    if "666" in str(count):
        list666.append(count)
    
    count += 1

print(list666[n - 1])