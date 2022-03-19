from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
sq_list = []
dp_list = [[0] * m for _ in range(n)]

for _ in range(n):
    sq_list.append(list(map(int, input().rstrip())))

result = 0
for x in range(n):
    for y in range(m):
            if (x == 0) or (y == 0): # 왼쪽, 위 원래 값 입력
                dp_list[x][y] = sq_list[x][y]
            elif sq_list[x][y] == 0: # 입력받은 값 0이면 0을 dq에 입력
                dp_list[x][y] = 0
            else: # 1인경우
                dp_list[x][y] = min(dp_list[x - 1][y - 1], dp_list[x][y - 1], dp_list[x - 1][y]) + 1
            
            result = max(dp_list[x][y], result)
print(result ** 2)