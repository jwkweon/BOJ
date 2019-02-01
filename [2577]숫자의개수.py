A = int(input())
B = int(input())
C = int(input())

check = [0 for i in range(10)]

prod = A * B * C
str_prod = str(prod)

for i in str_prod:
    check[int(i)] += 1

for i in check:
    print(i)
