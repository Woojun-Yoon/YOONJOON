from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    words = ''.join(input().split())
    alphabet = [0] * 26 # 0부터 a
    for i in words:
        alphabet[ord(i) - 97] += 1

    max_num = max(alphabet)
    max_index = alphabet.index(max_num)
    if alphabet.count(max_num) == 1:
        print(chr(max_index + 97))
    else:
        print('?')