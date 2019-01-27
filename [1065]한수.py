def han(num):
    a = num // 100
    b = (num % 100) // 10
    c = num % 10
    diff1 = a - b
    diff2 = b - c
    if diff1 == diff2:
        return 1
    else:
        return 0

list_han = [i for i in range(1, 100)]

N = int(input())

for i in range(100, N + 1):
    if han(i) == 1:
        list_han.append(i)

if N < 100:
    print(N)
else:
    print(len(list_han))
