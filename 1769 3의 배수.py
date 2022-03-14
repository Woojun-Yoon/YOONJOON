from sys import stdin
input = stdin.readline

def multiple_3(num, try_count): # num은 str, try_count는 int
    if len(num) < 2: # 입력값의 자리수가 백만개 이므로 이를 int로 변환하면 시간이 천문학적으로 걸림(따라서, 입력에 따른 int 안씀)
        return num, try_count
    
    cache = 0
    for i in num:
        cache += int(i)
    
    try_count += 1
    num = str(cache)
    return multiple_3(num, try_count) # 리턴으로 함수 재귀하기

n = input().strip()
try_count = 0
result, try_count = multiple_3(n, try_count)

print(try_count)

if int(result) % 3 == 0:
    print("YES")
else:
    print("NO")