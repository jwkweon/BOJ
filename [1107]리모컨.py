C = int(input())
n = int(input())

broken = []
if n != 0:
    broken = input().split()
ans = 0

ans = abs(C - 100)

L = len(broken)
def check(c):
    for i in range(L):
        if broken[i] in str(c):
            return 0
        else:
            pass
    return 1

for i in range(1000001):
    c = i
    if check(c) == 1:
        temp = len(str(c)) + abs(C - c)
        if temp < ans:
            ans = temp

print(ans)
