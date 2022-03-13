from sys import stdin
import time
input = stdin.readline

start = time.process_time()

prime_list = [True for _ in range(10000+1)]
prime_list[0] = False; prime_list[1] = False

for i in range(2, int(10000 ** 0.5) + 1):
    if prime_list[i]:
        j = 2
        while i * j <= 10000:
            prime_list[i * j] = False
            j += 1

# 92ms
for _ in range(int(input())):
    n = int(input())
    half_n = n // 2
    for i in range(half_n, 1, -1): # 가운데 부터 스타트
        if (prime_list[i] and prime_list[n - i]):
            print('%d %d' %(i, n - i))
            break

# 3000ms
'''
for _ in range(int(input())):
    n = int(input())
    result_list = []
    prime_list_left = []
    for i in range(n):
        if prime_list[i] and i <= (n // 2):
            prime_list_left.append(i)

    for x in prime_list_left: #이중 for문 시간복잡도 풀어내기
        if prime_list[n - x]:
            result_list.append([x, n - x])
    print(*result_list[-1])
'''


end = time.process_time()
print(f"{int(round((end - start) * 1000))} ms")