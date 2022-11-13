from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    k, d, a = map(int, input().split('/'))
    if (d == 0 or k + a < d):
        print("hasu")
    else:
        print("gosu")