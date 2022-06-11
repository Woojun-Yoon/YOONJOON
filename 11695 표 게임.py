from sys import stdin
from functools import reduce
from typing import Sequence
input = stdin.readline

def game(nums : Sequence[int]):
    result = reduce(lambda x, y : x ^ y, nums)
    return result

if __name__ == '__main__':
    n, m  = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append(sum(map(int, input().split())))
    result = game(nums)
    print('august14' if result else 'ainta')