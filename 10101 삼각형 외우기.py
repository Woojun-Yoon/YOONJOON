from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    check = a + b + c
    if check != 180:
        print("Error")
    else:
        if a == 60 and b == 60 and c == 60:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")