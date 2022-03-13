#브루트포스 알고리즘
from sys import stdin
input = stdin.readline

n, m = map(int, input().split()) #n = 카드의 개수, m = 넘지 않는 카드 수의 합
card_num = list(map(int, input().split()))
result_list = []
for x in range(n):
    for y in range(x + 1, n):
        for z in range(y + 1, n):
            if card_num[x] + card_num[y] + card_num[z] <= m:
                result_list.append(card_num[x] + card_num[y] + card_num[z])

print(max(result_list))
