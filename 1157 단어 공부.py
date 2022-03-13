from sys import stdin
input = stdin.readline
'''
소문자, 대문자 각각 26개
print(ord('a')) # 97
print(ord('A')) # 65     32 차이
'''
s = input().rstrip() # 입력 받은 단어( 대소 문자 )
alphabet = [0] * 26 # 0부터 A

for i in range(len(s)):
    if int(ord(s[i])) > 95: # 소문자 일 경우
        alphabet[int(ord(s[i])) - 97] += 1
    else:              # 대문자 일 경우
        alphabet[int(ord(s[i])) - 65] += 1

max_cache = max(alphabet)

if alphabet.count(max_cache) > 1: # count()를 통한 맥스값의 개수 카운팅
    print('?')
else:
    print(chr(alphabet.index(max_cache) + 65))

'''
정리
s = input().upper() # upper()로 대문자화, lower()로 소문자화
cnt = [0] * 26
for c in s:
    cnt[ord(c)-ord('A')] += 1
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    idx = cnt.index(max(cnt))
    print(chr(idx+ord('A')))
'''