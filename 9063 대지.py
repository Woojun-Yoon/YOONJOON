from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    px = []
    py = []
    for _ in range(n):
        x, y = map(int, input().split())
        px.append(x)
        py.append(y)
    
    minx = min(px); miny = min(py); maxx = max(px); maxy = max(py)
    print((maxx - minx) * (maxy - miny))
    
