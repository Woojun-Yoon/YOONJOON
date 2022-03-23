from sys import stdin
input = stdin.readline

def check(word1, word2):
    count = 0
    for i in range(8):
        if word1[i] != word2[i]:
            count += 1
    return count

wb_list = ["WBWBWBWB"    
,"BWBWBWBW"
,"WBWBWBWB"
,"BWBWBWBW"
,"WBWBWBWB"
,"BWBWBWBW"
,"WBWBWBWB"
,"BWBWBWBW"]
bw_list = ["BWBWBWBW"
,"WBWBWBWB"
,"BWBWBWBW"
,"WBWBWBWB"
,"BWBWBWBW"
,"WBWBWBWB"
,"BWBWBWBW"
,"WBWBWBWB"]
n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(input().rstrip())

result = []

for i in range(n - 7): # n 은 세로
    cache_list = chess[i : i + 8]
    for j in range(m - 7): # m 은 가로
        wb_result = 0
        bw_result = 0
        for k in range(8):
            wb_cache = check(cache_list[k][j : j + 8], wb_list[k])
            bw_cache = check(cache_list[k][j : j + 8], bw_list[k])
            wb_result += wb_cache
            bw_result += bw_cache
        result.append(min(wb_result, bw_result))

print(min(result))
        


