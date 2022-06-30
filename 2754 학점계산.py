from sys import stdin
input = stdin.readline

if __name__ == '__main__':

    result = 0

    score = input().rstrip()
    if score[0] == 'A':
        result = 4.0
    elif score[0] == 'B':
        result = 3.0
    elif score[0] == 'C':
        result = 2.0
    elif score[0] == 'D':
        result = 1.0
    else:
        result = 0.0
        
    if len(score) == 2:
        if score[1] == '+':
            result += 0.3
        elif score[1] == '-':
            result -= 0.3
    
    print(result)