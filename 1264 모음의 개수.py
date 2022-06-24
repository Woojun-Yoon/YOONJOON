from sys import stdin
input = stdin.readline

while True:
    words = input().rstrip()
    if words == '#':
        break
    
    result = 0

    for word in words:
        if word == 'a' or word == 'A' or word == 'e' or word == 'E' or word == 'i' or word == 'I' or word == 'o' or word == 'O' or word == 'u' or word == 'U':
            result += 1
    print(result)