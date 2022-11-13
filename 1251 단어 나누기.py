from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    word = list(input().rstrip())
    cache = []
    _len = len(word)
    for i in range(1, _len - 1):
        for j in range(i + 1, _len):
            x, y, z = word[0 : i], word[i : j], word[j : _len]
            x.reverse()
            y.reverse()
            z.reverse()
            cache.append(''.join(x + y + z))
    print(sorted(cache)[0])