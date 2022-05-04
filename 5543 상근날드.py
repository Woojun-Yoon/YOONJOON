from sys import stdin
input = stdin.readline

burger = 3000
drink = 3000

for _ in range(3):
    cache = int(input())
    if cache < burger:
        burger = cache
    
for _ in range(2):
    cache = int(input())
    if cache < drink:
        drink = cache
    
print(burger + drink - 50)