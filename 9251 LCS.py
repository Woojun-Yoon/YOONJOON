from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    word1 = input().rstrip()
    word2 = input().rstrip()

    cache = [0] * len(word2)

    for i in range(len(word1)):
        count = 0
        for j in range(len(word2)):
            if count < cache[j]:
                count = cache[j]
            elif word1[i] == word2[j]:
                cache[j] = count + 1
    
    print(max(cache))
