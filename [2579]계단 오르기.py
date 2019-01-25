T = int(input())

def dp(n):
    if dp_list[n] != 0:
        return dp_list[n]
    dp_list[n] = max(dp(n - 2) + st_val[n - 1], dp(n - 3) + st_val[n - 2] + st_val[n - 1])
    return dp_list[n]

dp_list = [0 for i in range(T + 1)]

st_val = []

for t in range(T):
    st_val.append(int(input()))

dp_list[1] = st_val[0]
dp_list[2] = st_val[0] + st_val[1]
dp_list[3] = max(st_val[0] + st_val[2], st_val[1] + st_val[2])


print(dp(T))
