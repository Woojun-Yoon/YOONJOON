from sys import stdin
input = stdin.readline
'''
def aka(words):
    result = 0
    l = len(words)
    words_left = words[0:l // 2]
    words_right = words[-(l // 2)::]
    
    if l == 1:
        return result
    elif (words_left == words_right):
        result += aka(words_left)
        result += aka(words_right)
    else:
        result += 1
    return result

words = input().strip()
result = aka(words)

if 0 != result:
    print("IPSELENTI")
else:
    print("AKARAKA")
'''
# 더 빠르고 효율적인 풀이
def aka(words):
    if len(words) == 1:
        return True
    
    if words == words[::-1]:
        return aka(words[:len(words) // 2])
    else:
        return False
word = input().strip()
if aka(word):
    print("AKARAKA")
else:
    print("IPSELENTI")




