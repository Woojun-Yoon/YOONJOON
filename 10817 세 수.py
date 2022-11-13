from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    nums = sorted([*map(int, input().split())])
    print(nums[1])
