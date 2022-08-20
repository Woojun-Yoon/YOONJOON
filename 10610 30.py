from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = list(input().rstrip())
    n.sort(reverse = True)
    sum = 0

    for _ in n:
        sum += int(_)
    
    if sum % 3 != 0 or '0' not in n:
        print('-1')
    else:
        print(''.join(n))