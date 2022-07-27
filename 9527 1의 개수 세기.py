from sys import stdin
input = stdin.readline

def check(n):
    count = 0
    binum = bin(n)[2 : ]
    l = len(binum)

    for _ in range(l):
        if binum[_] == '1':
            pow = l - _ - 1
            count += p[pow]
            count += (n - 2 ** pow + 1)
            n = n - 2 ** pow
    return count
        
if __name__ == '__main__':
    a, b = map(int, input().split())
    p = [0 for _ in range(59)]

    for _ in range(1, 59):
        p[_] = 2 ** (_ - 1) + 2 * p[_ - 1]
    
    print(check(b) - check(a - 1))