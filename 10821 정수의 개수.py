from sys import stdin
from collections import Counter
input = stdin.readline

if __name__ == '__main__':
    nums = input().rstrip()
    count = Counter(nums)
    print(count[','] + 1)
