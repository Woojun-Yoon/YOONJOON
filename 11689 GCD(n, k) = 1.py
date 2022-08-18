from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    result = n

    for _ in range(2, int(n ** 0.5) + 1):
        if n % _ == 0:
            while n % _ == 0:
                n = n // _
            result -= result / _
    
    if n > 1:
        result -= result / n
    
    print(int(result))