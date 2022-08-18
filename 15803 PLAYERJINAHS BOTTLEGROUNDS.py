from sys import stdin
input = stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

if __name__ == '__main__':
    p1 = [*map(int, input().split())]
    p2 = [*map(int, input().split())]
    p3 = [*map(int, input().split())]

    result = ccw(p1, p2, p3)

    if result == 0:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")