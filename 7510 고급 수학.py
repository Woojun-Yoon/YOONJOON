from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        l = sorted([*map(int, input().split())])
        if l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
            print("Scenario #", _ + 1, ':', sep = '')
            print("yes")
            print()
        else:
            print("Scenario #", _ + 1, ':', sep = '')
            print("no")
            print()