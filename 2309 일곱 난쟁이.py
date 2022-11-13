from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    h = []
    for _ in range(9):
        h.append(int(input()))
    h.sort()
    all_sum = sum(h)
    cache1 = 0
    cache2 = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if (all_sum - h[i] - h[j] == 100):
                cache1 = i
                cache2 = j
                break
    for _ in range(9):
        if (_ != cache1 and _ != cache2):
            print(h[_])
