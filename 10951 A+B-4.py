from sys import stdin
input = stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except: #오류 발생시 실행
        break