from sys import stdin
input = stdin.readline
# just use backtracking
n, m = map(int, input().split())
nums = []

def back(num):
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return
    
    for i in range(num, n + 1):
        nums.append(i)
        back(i) # make recursion
        nums.pop()

back(1)