import math

T = int(input())

for t in range(T):
    X, Y = map(int, input().split())
    dist = Y - X
    d = math.sqrt(dist)
    d_ceil = math.ceil(d)
    if d == d_ceil:
        print(int(d * 2 - 1))
    else:
        print(int(d * 2))
    
