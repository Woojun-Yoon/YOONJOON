from sys import stdin
input = stdin.readline
''' 시간 초과
n = int(input())
nums = []
result = 0
for _ in range(n):
    nums.append(int(input()))

result += n - 1 # 사이에 아무도 없을 때
for i in range(1, n - 1): # 사이에 한명 일때
    if (nums[i] <= nums[i - 1]) and (nums[i] <= nums[i + 1]):
        result += 1

for i in range(2, n): # 사이에 두명 이상있는 묶음 카운팅
    for j in range(0, n - i - 1): # stack slicing
        # stack = nums[j : j + i + 1]
        stack = nums[j + 1 : j + i + 1]
        top = max(stack)
        if (nums[j] >= top) and (nums[j + i + 1] >= top):
            result += 1

print(result)
'''

n = int(input())
result = 0
stack = []

for _ in range(n):
    h = int(input())

    while stack and stack[-1][0] < h:
        result += stack.pop()[1]
    
    if stack and stack[-1][0] == h:
        cache = stack.pop()[1]
        result += cache
    
        if len(stack) != 0:
            result += 1
    
        stack.append((h, cache + 1))
    
    else:
        if len(stack) != 0:
            result +=1 
        stack.append((h , 1))
print(result)

