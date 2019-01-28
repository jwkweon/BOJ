D, K = map(int, input().split())

f = [1, 1]

def find_AB(n):
    if n < len(f):
        return f[n]
    else:
        f.append(find_AB(n-1) + find_AB(n - 2))
        return f[-1]

A_num, B_num = find_AB(D - 3), find_AB(D - 2)

for i in range(1, K):
    j = (K - (i * A_num)) % B_num
    l = (K - (i * A_num)) // B_num
    if j == 0:
        print(i)
        print(l)
        break
