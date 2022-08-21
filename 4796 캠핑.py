from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    count = 1
    while True:
        l, p, v = map(int, input().split())
        if l == 0 and p == 0 and v == 0:
            break

        a, b = divmod(v, p)
        result = l * a
        result += min(b, l)
        print("Case ", count, ': ', result, sep = '')
        count += 1
