from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    check = int(input())
    result = 0
    for _ in range(int(input())):
        a, b = map(int, input().split())
        result += a * b
    if check == result:
        print("Yes")
    else:
        print("No")