from sys import stdin
input = stdin.readline

n = int(input())
tp_list = [] # 0 = day, 1 = pay
dp_list = [0] * (n + 1)
for i in range(n):
    tp_list.append(list(map(int, input().split())))

for i in range(n - 1, -1, -1): # 역순
    if (i + tp_list[i][0]) <= n: # n을 넘치지 않는 경우
        dp_list[i] = max(tp_list[i][1] + dp_list[i + tp_list[i][0]], dp_list[i + 1]) # (day이전값 + 현재값)과 dp이전값과 비교
    else: # 넘치는 경우
        dp_list[i] = dp_list[i + 1] # dp 밀어내서 저장
print(dp_list[0]) # 마지막값 출력