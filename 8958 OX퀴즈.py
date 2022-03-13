from sys import stdin
input = stdin.readline

T = int(input()) # 테스트 케이스의 개수
for _ in range(T):
    case = input().strip()
    final_score = 0
    cache_score = 0
    for i in range(len(case)):
        if case[i] == 'O':
            cache_score += 1
            final_score += cache_score
        else:
            cache_score = 0
    print(final_score)
