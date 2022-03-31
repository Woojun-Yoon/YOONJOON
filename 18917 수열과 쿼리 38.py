from sys import stdin
input = stdin.readline

a_sum = 0
a_xor = 0
a = [0]
for _ in  range(int(input())):
    com = input().split()
    if com[0] == '1':
        a_sum += int(com[1])
        a_xor = a_xor^int(com[1])
    elif com[0] == '3':
        print(a_sum)
    elif com[0] == '4':
        print(a_xor)
    else:
        a_sum -= int(com[1])
        a_xor = a_xor^int(com[1])