from sys import stdin
input = stdin.readline
''' 시간 초과
max_len = 0
cache_time = 10 ** 100000
result_time = 0
block = []
n, m ,b = map(int, input().split())
for _ in range(n):
    cache = list(map(int, input().split()))
    for i in range(m):
        block.append(cache[i])

max_ = max(block)
min_ = min(block)
# 평지 만들기
for i in range(min_ , max_ + 1):
    cache_b = b
    time = 0
    for j in range(n * m):
        cache = block[j] - i
        if cache > 0:
            cache_b +=  cache
            time += (cache * 2)
        else:
            cache_b += cache
            time -= cache
        
    
    if cache_b >= 0:
        if time <= cache_time:
            cache_time = time
            result_time = cache_time
            max_len = i

print(result_time, max_len)
'''

n, m ,b=map(int,input().split())
list = [0]*257
poli=[]
for _ in range(n):
    for num in map(int,stdin.readline().split()):
        list[num]+=1
#목표하는 고르기 높이
for j in range(0,257):
    sum1=0
    sum2=0
    #모든 땅의 위치를 확인
    for i in range(257):
        #만약 땅이 높으면
        if i>=j:
            #땅의 높이를 낮춘다
            sum1+=(i-j)*list[i]
        #아님
        else:
            #땅의 높이를 높인다
            sum2+=(j-i)*list[i]
    if sum2>sum1+b:
        break
    poli.append(sum1*2+sum2)
min=poli[0]
place=0
for i in range(1,len(poli)):
    if min>=poli[i]:
        min=poli[i]
        place=i
print(min,place)