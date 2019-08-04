N, M = map(int, input().split())
N_list = [i for i in map(int, input().split())]
ans = 0
for i, j in enumerate(N_list[:-2]):
    for m, n in enumerate(N_list[i+1:-1]):
        for r, s in enumerate(N_list[i+m+2:]):
            temp = j + n + s
            if temp <= M:
                ans = max(ans, temp)

print(ans)
