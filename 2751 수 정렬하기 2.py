from sys import stdin
input = stdin.readline

n = int(input())
num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)
num_list.sort()
print("\n".join(map(str, num_list))) # join()은 리스트 안의 문자열을 합치는 역할을 함(int 안됨)