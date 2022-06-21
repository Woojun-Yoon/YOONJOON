from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    nums = [0] * 31
    for _ in range(28):
        nums[int(input())] = 1

    for _ in range(1, 31):
        if nums[_] == 0:
            print(_)
    