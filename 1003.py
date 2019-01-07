'''
시간초과
def fibo(n):
    n_0 = 0
    n_1 = 0
    if n == 0:
        n_0 += 1
    elif n == 1:
        n_1 += 1
    else:
        n_0_temp, n_1_temp = fibo(n-1)
        n_0_temp2, n_1_temp2 = fibo(n-2)
        n_0 = n_0_temp + n_0_temp2
        n_1 = n_1_temp + n_1_temp2

    return n_0, n_1

t = input()
for i in range(int(t)):
    n = int(input())
    a, b = fibo(n)
    print(a, b)
'''
def fibo(n):
    for i in range(n-1):
            b = a[-1] + a[-2]
            a.append(b)
    if n == 0:
        print('1 0')
    else:
        print(a[-2], a[-1])

t = input()
for i in range(int(t)):
    a = [0, 1]
    n = int(input())
    fibo(n)
