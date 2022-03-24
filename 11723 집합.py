from sys import stdin
input = stdin.readline

result = set()

for _ in range(int(input())):
    com = input().split()
    if com[0] == 'add':
        result.add(int(com[1]))
    elif com[0] == 'check':
        if int(com[1]) in result:
            print(1)
        else:
            print(0)
    elif com[0] == 'remove':
        result.discard(int(com[1]))
    elif com[0] == 'toggle':
        if int(com[1]) in result:
            result.discard(int(com[1]))
        else:
            result.add(int(com[1]))
    elif com[0] == 'all':
        result = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif com[0] == 'empty':
        result = set([])
