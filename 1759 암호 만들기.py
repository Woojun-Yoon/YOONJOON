from sys import stdin
input = stdin.readline

def back(count, index):
    if count == L:
        x, y = 0, 0

        for _ in range(L):
            if result[_] in check:
                x += 1
            else:
                y += 1
        
        if x >= 1 and y >= 2:
            print("".join(result))
    

    for _ in range(index, C):
        result.append(word[_])
        back(count + 1, _ + 1)
        result.pop()


if __name__ == '__main__':
    L, C = map(int, input().split())
    word = sorted(input().split())
    check = ['a', 'e', 'i', 'o', 'u']
    result = []
    back(0, 0)