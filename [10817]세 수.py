A, B, C = map(int, input().split())

def sort(a, b, c):
    if a >= b:
        temp = b
        b = a
        a = temp

    if b >= c:
        temp = c
        c = b
        b = temp

    if a >= b:
        temp = b
        b = a
        a = temp
    print(b)

sort(A, B, C)
