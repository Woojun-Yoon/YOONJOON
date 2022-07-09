from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    while True:
        triangle = sorted(list(map(int, input().split())))
        a, b, c = triangle[0], triangle[1], triangle[2]
        if a == 0 and b == 0 and c == 0:
            break

        if c >= a + b:
            print("Invalid")
        else:
            if a == b and b == c and a == c:
                print("Equilateral")
            elif a == b or b == c or a == c:
                print("Isosceles")
            else:
                print("Scalene")
