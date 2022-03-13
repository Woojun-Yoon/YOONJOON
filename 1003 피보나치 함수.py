# N번째 피보나치 수를 구하는 함수
# 다이나믹 프로그래밍(타블레이션[Bottom-Up])(메모이제이션[Top-Down])
'''
dicZ = [0] * 50 #한번 계산된 값을 저장하는 리스트(0)
dicO = [0] * 50 #(1)
def fibo(n):
    if (n == 0):
        dicZ[n] = dicZ[n] + 1
    elif (n == 1):
        dicO[n] = dicO[n] + 1
    elif (dicZ[n] != 0 or dicO[n] != 0): #리스트에 올바른 값이 존재 할때
        print(dicZ[n],dicO[n])
    else:
        dicZ[n] = dicZ[n-1] + dicZ[n-2]
        dicO[n] = dicO[n-1] + dicO[n-2]

fibo(2)
print(dicZ[2])
print(dicO[2])
'''
dic = [0] * 50

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dic[n] == 0:
        dic[n] = fibo(n-1) + fibo(n-2)
        return dic[n]
    else:
        return dic[n]

T = int(input()) #테스트 개수 T
i = 0
while i < T:
    a = int(input())
    if a == 0:
        print('1 0')
    elif a == 1:
        print('0 1')
    else:
        print(fibo(a-1),fibo(a))
    i += 1





