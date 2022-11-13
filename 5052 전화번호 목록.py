from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        nums = []
        flag = 0
        n = int(input())
        for i in range(n):
            nums.append(input().rstrip())
        nums.sort()
        for i in range(0, n - 1):
            if (len(nums[i]) <= len(nums[i + 1])):
                if (nums[i + 1][0 : len(nums[i])] == nums[i]):
                    flag = 1
                    break
        if flag:
            print("NO")
        else:
            print("YES")