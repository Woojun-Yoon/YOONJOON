from sys import stdin
input = stdin.readline
'''
while 1:
    num = input().strip()
    if num == '0':
        break
    
    if len(num) == 1:
        print('yes')
    elif len(num) == 2 and num[0] == num[1]:
        print('yes')
    elif len(num) == 3 and num[0] == num[2]:
        print('yes')
    elif len(num) == 4 and num[0] == num[3] and num[1] == num[2]:
        print('yes')
    elif len(num) == 5 and num[0] == num[4] and num[1] == num[3]:
        print('yes')
    else:
        print('no')
'''

while True:
    a = input().strip()
    if a == '0':
        break
    else:
        print('yes' if a == a[::-1] else 'no')