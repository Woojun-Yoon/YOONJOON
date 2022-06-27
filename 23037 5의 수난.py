from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    nums = input().rstrip()
    result = 0
    for num in nums:
        result += int(num) ** 5
    
    print(result)