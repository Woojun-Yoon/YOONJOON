from sys import stdin
input = stdin.readline

C = int(input()) # 테스트 케이스의 개수
for _ in range(C):
    case = list(map(int, input().split()))
    n = case[0] #학생의 수
    case_sum = sum(case) - n
    case_average = case_sum / n
    alpha_student = 0
    for i in range(1,n+1):
        if case[i] > case_average:
            alpha_student += 1
    result = alpha_student / n * 100
    print('{0:0.3f}%'.format(result)) #format을 통한 반올림 
    # 중괄호로 인덱스 표현가능
    
    # print(round(alpha_student / n * 100, 3), '%', sep='') [round는 사사오입이고, 0이 끝까지 출력이 안됨]


