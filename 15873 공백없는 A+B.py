from sys import stdin
input = stdin.readline

nums = input().rstrip()
if len(nums) == 2:
    print(int(nums[0]) + int(nums[1]))
elif len(nums) == 3:
    if int(nums[0:2]) > 10:
        print(int(nums[0]) + int(nums[1:3]))
    else:    
        print(int(nums[0:2]) + int(nums[2]))
else:
    print(20)