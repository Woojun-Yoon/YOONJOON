from sys import stdin
input = stdin.readline

def ccw(p1, p2, p3):
    if ((p2[0] - p1[0]) * (p3[1] - p2[1])) > ((p2[1] - p1[1]) * (p3[0] - p2[0])):
        return True
    else:
        return False

def convex_hull(p):
    convex = []
    for p3 in p:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
    return len(convex)

if __name__ == '__main__':
    n, result = int(input()), -2
    p = []
    for _ in range(n):
        p.append(list(map(int, input().split())))
    
    p = sorted(p, key = lambda p : (p[0], p[1]))
    result += convex_hull(p)
    p.reverse()
    result += convex_hull(p)
    
    print(result)