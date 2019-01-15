import sys
T = int(input())

for t in range(T):
    input_ = sys.stdin.readline().split()
    a, b = map(int, input_)
    print(a + b)
