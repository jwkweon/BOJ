N, X = map(int, input().split())
list = input().split()
ans = []

for i, k in enumerate(list):
    if int(k) < X:
        ans.append(k)

kkk = " ".join(ans)
print(kkk)
