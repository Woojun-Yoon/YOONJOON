# 이분 탐색(이진 탐색) ? bisect
# 이분 탐색은 O(n log n) (sort - O(n), search - O(log n))
from sys import stdin
input = stdin.readline
'''
def binary_search(list, num):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if list[mid] == num:
            return 1
        elif list[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort() # O(n log n)
m = int(input())
m_list = list(map(int, input().split()))
for i in m_list:
    print(binary_search(n_list, i))
'''
# set()을 이용한 풀이
# set()과 dict()는 hash table을 사용하기 때문에 써치가 O(1), 해시함수에 인풋값을 넣어 인덱스 접근후 존재유무 파악
n = int(input())
n_list = set(input().split())

m = int(input())
m_list = list(input().split())
for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)