from sys import stdin
input = stdin.readline
L = 1000000007

def power(a, b, n):
    cal = []
    for i in range(n):
        temp = []
        for j in range(n):
            num = 0
            for k in range(n):
                num += a[i][k] * b[k][j]
            temp.append(num % L)
        cal.append(temp)
    return cal

def fibo(s, b):
    if b == 1:
        return s
    
    a = fibo(s, b // 2)

    cal = power(a, a, n)

    result = []

    if b % 2:
        result = power(cal, A, n)
    else:
        result = cal
    
    return result
if __name__ == '__main__':
    n, B = 2, int(input())
    A = [[1, 1], [1, 0]]
    print(fibo(A, B)[0][1])
