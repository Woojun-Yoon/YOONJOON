from sys import stdin
input = stdin.readline

def check(x, y, w):
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    return h1 * h2 / (h1 + h2)

if __name__ == '__main__':
    x, y, c = map(float, input().split())
    result = 0
    start, end = 0, min(x, y)

    while end - start > 0.000001:
        mid = (start + end) / 2
        if check(x, y, mid) >= c:
            result = mid
            start = mid
        else:
            end  = mid
    
    print(result)