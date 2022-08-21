from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    s = input().rstrip()
    result = 0
    for _ in range(len(s) - 1):
        if s[_] != s[_ + 1]:
            result += 1
    print((result + 1) // 2)