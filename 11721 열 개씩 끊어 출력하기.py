from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    words = input().rstrip()
    count = 0

    for word in words:
        if count == 10:
            count = 0
            print()
        print(word, end = '')
        count += 1