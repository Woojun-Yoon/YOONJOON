from sys import stdin
input = stdin.readline
'''
string = set(input().rstrip() for _ in range(int(input()))) # 중복 제거(set은 중복을 허용하지 않음)(인덱스값 즉 순서를 가지지 않음)
string=sorted(string)  # 사전 순 정렬
#string=sorted(string, key=lambda x : len(x))    # 길이 순 정렬
for i in string : print(i)
'''
lists = set(stdin.readline().rstrip() for i in range(int(input())))
print('\n'.join(sorted(lists, key=lambda item: (len(item), item))))