# import sys

while 1:
    try:
        word = input()
    except EOFError:
        break
    print(word)

# sys.stdin.readline()은 EOFError 즉 ^Z를 입력했을 떄 에러가 뜨지 않는다
''' 틀린 예시
while 1:
    try:
        word = sys.stdin.readline().strip()
    except EOFError:
        break
    print(word)
'''