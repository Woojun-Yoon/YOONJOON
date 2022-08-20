from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    s = int(input())
    count = 1
    result = 0
    while True:
        cache = (count * (count + 1)) // 2
        if s <= cache:
            break
        else:
            count += 1
    
    if s == cache:
        print(count)
    else:
        print(count - 1)