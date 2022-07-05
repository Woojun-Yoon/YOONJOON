from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        line1 = [*map(int, input().split())]
        line2 = [*map(int, input().split())]

        for i in range(1, n):
            if i == 1:
                line1[i] += line2[i - 1]
                line2[i] += line1[i - 1]
            else:
                line1[i] += max(line2[i - 1], line2[i - 2])
                line2[i] += max(line1[i - 1], line1[i - 2])
        
        print(max(line1[n - 1], line2[n - 1]))