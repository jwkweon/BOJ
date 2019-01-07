import math

def dist(x, y, xc, yc, r):
    xd = (x - xc) ** 2
    yd = (y - yc) ** 2
    d = math.sqrt(xd + yd)
    if d > r:
        return 0
    else:
        return 1

def compare_flag(f1, f2, num_Circle):
    num = 0
    for i in range(num_Circle):
        if f1[i] == f2[i]:
            pass
        else:
            num += 1
    return print(num)


T = int(input())
for t in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    flag_1 = []
    flag_2 = []
    num_Circle = int(input())
    for c in range(num_Circle):
        rx, ry, r = map(int, input().split())
        flag_1.append(dist(x1, y1, rx, ry, r))
        flag_2.append(dist(x2, y2, rx, ry, r))

    compare_flag(flag_1, flag_2, num_Circle)
