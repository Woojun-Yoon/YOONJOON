from sys import stdin
input = stdin.readline

if __name__ == '__main__':

    n = int(input())
    price = []

    for _ in range(n):
        price.append([*map(int, input().split())])
    
    for _ in range(1, n):
        price[_][0] = min(price[_ - 1][1], price[_ - 1][2]) + price[_][0]
        price[_][1] = min(price[_ - 1][0], price[_ - 1][2]) + price[_][1]
        price[_][2] = min(price[_ - 1][0], price[_ - 1][1]) + price[_][2]
    
    print(min(price[n - 1]))