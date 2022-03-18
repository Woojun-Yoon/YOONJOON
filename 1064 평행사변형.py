from sys import stdin
from math import sqrt
input = stdin.readline

x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
try:
    gradient_ab = (y_a - y_b) / (x_a - x_b)
except:
    gradient_ab = "parallel"
try:
    gradient_bc = (y_b - y_c) / (x_b - x_c)
except:
    gradient_bc = "parallel"
try:
    gradient_ca = (y_c - y_a) / (x_c - x_a)
except:
    gradient_ca = "parallel"

if gradient_ab == gradient_bc == gradient_ca:
    print(-1.0)
else:
    ab = sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
    bc = sqrt((x_c - x_b) ** 2 + (y_c - y_b) ** 2)
    ac = sqrt((x_c - x_a) ** 2 + (y_c - y_a) ** 2)

    line_list = [ab + bc, bc + ac, ab + ac]
    print((max(line_list) - min(line_list)) * 2)
