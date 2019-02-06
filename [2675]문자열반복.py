T = int(input())

for t in range(T):
    R, S = map(str, input().split())
    ans = []
    for i in S:
        ans.append(i * int(R))
    for j in range(len(S)):
        print(ans[j], end='')
    print('')
