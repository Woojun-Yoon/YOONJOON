from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (a < 2):
        print("Before")
    elif (a == 2):
        if (b < 18):
            print("Before")
        elif (b == 18):
            print("Special")
        else:
            print("After")
    else:
        print("After")