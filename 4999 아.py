from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    can = input().rstrip()
    doc = input().rstrip()

    if len(can) >= len(doc):
        print("go")
    else:
        print("no")