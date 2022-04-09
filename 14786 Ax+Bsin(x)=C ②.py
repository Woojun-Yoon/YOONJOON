# 수치해석, 뉴튼 랩슨 법
from sys import stdin
import math
input = stdin.readline

a, b, c = map(int, input().split())
x = 0

while(abs((a * x) + (b * math.sin(x)) - c) > 0.000000001):
    x = x - (((a * x) + (b * math.sin(x)) - c) / (a + b * math.cos(x)))

print(x)