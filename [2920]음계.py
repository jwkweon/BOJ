order = input().split()

d = 1
for i in range(7):
    d *= int(order[i + 1]) - int(order[i])

if d == 1:
    print('ascending')
elif d == -1:
    print('descending')
else:
    print('mixed')
