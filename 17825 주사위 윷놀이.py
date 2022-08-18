from sys import stdin
from typing import List
input = stdin.readline

def back(num : int, cache : int, piece : List, check : List):
    global result
    if num >= 10:
        result = max(result, cache)
        return
    
    for i in range(4):
        x = piece[i]
        if len(board[x]) == 2: # JC
            x = board[x][1]
        else:
            x = board[x][0]
        
        for _ in range(1, dice[num]):
            x = board[x][0]
        if x == 32 or (x < 32 and x not in piece):
            before = piece[i]
            piece[i] = x
            check.append(x)
            back(num + 1, cache + score[x], piece, check)
            check.pop()
            piece[i] = before

if __name__ == '__main__':
    board = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17]
    , [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]] # 32 -> done
    score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24,
    28, 27, 26, 30, 35, 0]
    dice = [*map(int, input().split())]
    global result
    result = 0

    back(0, 0, [0, 0, 0, 0], [])
    print(result)