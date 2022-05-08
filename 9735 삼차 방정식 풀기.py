from sys import stdin
input = stdin.readline

# Ax3 + Bx2 + Cx + D = 0 

def GetDivsor(num): # num의 약수 구하기
    cache = []
    for nums in range(1, int(num ** 0.5) + 1): # num의 절반 만큼만 search
        if (num % nums == 0):
            cache.append(nums)
            if (nums ** 2 != num): # 짝이되는 수가 다를 경우 다른 한쪽도 append
                cache.append(num // nums)
    return cache

def GetAns1(a, d):
    a_divisor = GetDivsor(a)
    d_divisor = GetDivsor(d)
    for a in a_divisor:
        for d in d_divisor:
            sub = d // a
            if (sub == 0):
                continue
            else:
                for ans in [sub, -sub]:
                    if ((coef[0] * ans ** 3 + coef[1] * ans ** 2 + coef[2] * ans + coef[3]) == 0):
                        return ans

for _ in range(int(input())):
    coef = list(map(int, input().split())) # [A, B, C, D]
    if (coef[3] == 0):
        Ans1 = 0
    else:
        Ans1 = GetAns1(abs(coef[0]), abs(coef[3]))
    # 구한 해로 조립제법
    a = coef[0]
    b = a * Ans1 + coef[1]
    c = b * Ans1 + coef[2]
    # 이차다항식 근 판별식
    D = b ** 2 - 4 * a * c
    result = [Ans1]
    if (D == 0): # 중근인 경우
        Ans2 = -(b / (2 * a)) # 근의 공식 사용
        if (Ans1 != Ans2):
            result.append(Ans2)
    
    elif (D > 0):
        Ans2 = (-b + D ** 0.5) / (2 * a)
        Ans3 = (-b - D ** 0.5) / (2 * a)
        if (Ans1 == Ans2):
            result.append(Ans3)
        elif (Ans1 == Ans3):
            result.append(Ans2)
        else:
            result.append(Ans2)
            result.append(Ans3)
    
    result.sort()
    print(*result)