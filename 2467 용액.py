from sys import stdin, maxsize
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = [*map(int, input().split())]

    left = 0
    right = n - 1
    ansleft = 0
    ansright = 0
    _min = maxsize

    while left < right:
        cache = nums[left] + nums[right]

        if abs(cache) < _min:
            ansleft = left
            ansright = right
            _min = abs(cache)
        
        if cache > 0:
            right -= 1
        elif cache < 0:
            left += 1
        else:
            break
    
    print(nums[ansleft], nums[ansright])