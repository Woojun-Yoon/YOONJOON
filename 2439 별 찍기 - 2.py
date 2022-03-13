from sys import stdin
input = stdin.readline

n = int(input())
'''
for i in range(0,n,1):
    print(('*' * (i + 1)).rjust(n))

'''
for i in range(0,n,1):
    space = n - i - 1
    print(' ' * space +'*' * (i + 1))

