from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    result = []
    word = input().rstrip()
    for i in range(0, len(word), 1):
        result.append(word[i : len(word)])
    result.sort()
    for w in result:
        print(w)