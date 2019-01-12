n = int(input())
n_q = n // 5
n_r = n % 5
n_w = [0, 1, 2, 1, 2]

if n_q == 0:
    if n_r == 4:
        print('-1')
    else:
        print('1')
elif n_q == 1:
    if n_r == 2:
        print('-1')
    else:
        print(n_q + n_w[n_r])
else:
    print(n_q + n_w[n_r])
