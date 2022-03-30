'''
from sys import stdin
from collections import deque
input = stdin.readline

def make(command, subway): # command = str, subway = list
    if command[0] == "BN":
        while int(command[1]) != subway[-1]:
            subway.appendleft(subway.pop())
        print(subway[0])
        subway.append(int(command[2]))
        return 0
    elif command[0] == "BP":
        while int(command[1]) != subway[-1]:
            subway.appendleft(subway.pop())
        subway.appendleft(subway.pop())
        print(subway[-1])
        subway.append(int(command[2]))
        return 0
    elif command[0] == "CP":
        while int(command[1]) != subway[-1]:
            subway.appendleft(subway.pop())
        subway.appendleft(subway.pop())
        print(subway.pop())
        return 0
    elif command[0] == "CN":
        while int(command[1]) != subway[-1]:
            subway.appendleft(subway.pop())
        print(subway.popleft())
        return 0
    else:
        pass

n, m = map(int, input().split())
subway = deque(list(map(int, input().split())))
for _ in range(m):
    command = input().split()
    make(command, subway)
'''
# 파이썬으로 풀 수 없는 문제, pypy3를 이용한 더 빠른 입출력을 사용해야함
import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


N, M = map(int, input().split())
st = list(map(int, input().split()))
ans = __pypy__.builders.StringBuilder()
arr_n = [0] * 1000001
arr_p = [0] * 1000001
st.append(st[0])

for i in range(len(st) - 1):
   arr_n[st[i]] = st[i + 1]
   arr_p[st[i + 1]] = st[i]

for _ in range(M):
   cmd, *x = input().split()

   if cmd == b'BN':
      i, j = int(x[0]), int(x[1])
      nxt = arr_n[i]
      ans.append(str(nxt) + '\n')
      arr_p[j] = i
      arr_n[j] = nxt
      arr_n[i] = j
      arr_p[nxt] = j

   elif cmd == b'BP':
      i, j = int(x[0]), int(x[1])
      prv = arr_p[i]
      ans.append(str(prv) + '\n')
      arr_n[j] = i
      arr_p[j] = prv
      arr_p[i] = j
      arr_n[prv] = j

   elif cmd == b'CN':
      i = int(x[0])
      nxt = arr_n[arr_n[i]]
      ans.append(str(arr_n[i]) + '\n')
      arr_n[i] = nxt
      arr_p[nxt] = i

   else:
      i = int(x[0])
      prv = arr_p[arr_p[i]]
      ans.append(str(arr_p[i]) + '\n')
      arr_p[i] = prv
      arr_n[prv] = i

os.write(1, ans.build().encode())