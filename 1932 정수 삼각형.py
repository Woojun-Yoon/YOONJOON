from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append([*map(int, input().split())])

    count = 2
    for i in range(1, n):
        for j in range(count):
            if j == 0:
                nums[i][j] = nums[i][j] + nums[i - 1][j]
            elif i == j:
                nums[i][j] = nums[i][j] + nums[i - 1][-1]
            else:
                nums[i][j] = max(nums[i - 1][j - 1], nums[i - 1][j]) + nums[i][j]
        
        count += 1

    print(max(nums[n - 1]))