from sys import stdin
from itertools import permutations
input = stdin.readline
''' for 중첩으로 푼문제
num = int(input())
result_hello = 0
result_world = 0
Find = False
for a in range(1, 10):
    for b in range(10):
        if a == b:
            continue
        for c in range(10):
            if (c == b) or (c == a):
                continue
            for d in range(10):
                if (d == c) or (d == b) or (d == a):
                    continue
                for e in range(1, 10):
                    if (e == d) or (e == c) or (e == b) or (e == a):
                        continue
                    for f in range(10):
                        if (f == e) or (f == d) or (f == c) or (f == b) or (f == a):
                            continue
                        for g in range(10):
                            if (g == f) or (g == e) or (g == d) or (g == c) or (g == b) or (g == a):
                                continue
                            hello = (a*10000) + (b*1000) + (c*100) + (c*10) + d
                            world = (e*10000) + (d*1000) + (f*100) + (c*10) + g
                            if (num == hello + world):
                                result_hello = hello
                                result_world = world
                                Find = True
                                break
                        if Find:
                            break
                    if Find:
                        break
                if Find:
                    break
            if Find:
                break
        if Find:
            break
    if Find:
        break

if (result_hello) == 0 or (result_world) == 0:
    print("No Answer")
else:
    print(" ", result_hello)
    print("+", result_world)
    print("-------")
    if len(str(num)) == 5:
        print(" ", num)
    else:
        print(" ", num, sep = '')
'''
real_num = int(input())
Find = False
num_list = [i for i in range(10)]
for num in permutations(num_list, 7):
    a, b, c, d, e, f, g = num
    if (a == 0) or (e == 0):
        continue
    else:
        hello = (a*10000) + (b*1000) + (c*100) + (c*10) + d
        world = (e*10000) + (d*1000) + (f*100) + (c*10) + g
        if real_num == hello + world:
            result_hello = hello
            result_world = world
            Find = True
            break
if Find:
    print(" ", result_hello)
    print("+", result_world)
    print("-------")
    if len(str(real_num)) == 5:
        print(" ", real_num)
    else:
        print(" ", real_num, sep = '')
else:
    print("No Answer")