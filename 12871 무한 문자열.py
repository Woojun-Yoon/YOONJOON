from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    s = input().rstrip()
    t = input().rstrip()
    s_len, t_len = len(s), len(t)

    if (s * t_len == t * s_len):
        print(1)
    else:
        print(0)
