from sys import stdin
input = stdin.readline
# 분할정복을 이용한 거듭제곱
def power(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a * a) % c
    else:
        if b % 2: # b is odd
            return ((power(a, b // 2, c) ** 2) * a) % c
        else:
            return (power(a, b // 2, c) ** 2) % c

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(power(a, b, c))