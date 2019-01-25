for i in range(3):
    k = sum([int(n) for n in input().split()])
    if k == 0:
        print('D')
    elif k == 1:
        print('C')
    elif k == 2:
        print('B')
    elif k == 3:
        print('A')
    else:
        print('E')
