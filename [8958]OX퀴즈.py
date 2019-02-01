T = int(input())

def score(n):
    result = 0
    for i in range(n):
        result += i + 1
    return result

for t in range(T):
    OX = input().split('X')
    sum = 0
    for i in OX:
        sum += score(len(i))
    print(sum)
