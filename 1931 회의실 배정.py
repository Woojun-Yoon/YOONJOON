from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x : (x[1], x[0]))
    result = 0
    end = 0
    for count1, count2 in nums:
        if count1 >= end:
            result += 1
            end = count2
    print(result)