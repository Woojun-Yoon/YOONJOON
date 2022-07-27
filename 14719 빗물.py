from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    h, w = map(int, input().split())
    block = [*map(int, input().split())]
    result = 0

    for i in range(1, h + 1):
        check = False
        count = 0
        for j in block:
            if j >= i:
                check = True
                result += count
                count = 0
            
            if j < i and check == True:
                count += 1
    
    print(result)   