from sys import stdin
input = stdin.readline

score = []
for i in range(1, 9):
    score.append((i, int(input())))

real_score = sorted(score, key = lambda x : x[1], reverse = 1)
print(real_score[0][1] + real_score[1][1] + real_score[2][1] + real_score[3][1] + real_score[4][1])
real_index = [real_score[0][0], real_score[1][0], real_score[2][0],  real_score[3][0], real_score[4][0]]
print(*sorted(real_index))