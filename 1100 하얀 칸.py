from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    result = 0
    for i in range(8):
        line = input().rstrip()
        if (i % 2 == 0):
            if (line[0] == 'F'):
                result += 1
            if (line[2] == 'F'):
                result += 1
            if (line[4] == 'F'):
                result += 1
            if (line[6] == 'F'):
                result += 1
        else:
            if (line[1] == 'F'):
                result += 1
            if (line[3] == 'F'):
                result += 1
            if (line[5] == 'F'):
                result += 1
            if (line[7] == 'F'):
                result += 1
    print(result)
