import time

tic = time.time()

def comb(N, M):
    prod_mole = 1
    prod_denom = 1
    for i in range(N):
        prod_mole *= (M - i)
        prod_denom *= (i + 1)
    return int(prod_mole / prod_denom)

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    print(comb(N, M))

toc = time.time()
print('%.3f' %(toc - tic))
