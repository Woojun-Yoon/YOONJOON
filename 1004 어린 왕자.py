T = int(input())
i = 0
while (i < T): #마지막 줄 i=+1
    a = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for j in range(n):
        Cx, Cy, r = map(int, input().split())
        if ((x1 - Cx)**2 + (y1 - Cy)**2 <= r**2) != ((x2 - Cx)**2 + (y2 - Cy)**2 <= r**2): #논리 XOR
            a = a + 1
    print(a)
    i += 1