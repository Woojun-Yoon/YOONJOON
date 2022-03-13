from sys import stdin
input = stdin.readline

song = input().strip()

if song == '1 2 3 4 5 6 7 8':
    print('ascending')
elif song == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')


