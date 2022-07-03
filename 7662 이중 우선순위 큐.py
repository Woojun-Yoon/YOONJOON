from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict
input = stdin.readline

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        K = int(input())
        Q1, Q2 = [], []
        vis = defaultdict(bool)

        for i in range(K):
            com, num = input().split()

            if com == 'I':
                heappush(Q1, (int(num), i)) # Create min heap
                heappush(Q2, (-int(num), i)) # Create max heap
                vis[i] = True
            else:
                if num == '1': # max D
                    while Q2 and not vis[Q2[0][1]]:
                        heappop(Q2)
                    if Q2:
                        vis[Q2[0][1]] = False
                        heappop(Q2)
                else: # min D
                    while Q1 and not vis[Q1[0][1]]:
                        heappop(Q1)
                    if Q1:
                        vis[Q1[0][1]] = False
                        heappop(Q1)
    
        while Q1 and not vis[Q1[0][1]]:
            heappop(Q1)
        while Q2 and not vis[Q2[0][1]]:
            heappop(Q2)
        
        if Q1 and Q2:
            max_value = -Q2[0][0]
            min_value = Q1[0][0]
            print(max_value, min_value)
        else:
            print("EMPTY")