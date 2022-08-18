from sys import stdin
input = stdin.readline

def ser(left, right):
    while abs(right - left) > 0.000000001:
        left_t = (2 * left + right) / 3
        right_t = (left + 2 * right) / 3
        if cal(left_t) > cal(right_t):
            left = left_t
        else:
            right = right_t
    return cal(left)

def cal(n):
    minx = Ax * n + Bx * (1 - n)
    miny = Ay * n + By * (1 - n)
    kangx = Cx * n + Dx * (1 - n)
    kangy = Cy * n + Dy * (1 - n)

    return ((minx - kangx) ** 2 + (miny - kangy) ** 2) ** 0.5

if __name__ == '__main__':
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())
    result = ser(0, 1)
    print(format(result, '.10f'))
