alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = [-1 for i in range(26)]

str = input()
for i in range(len(str)):
    for n, k in enumerate(alp):
        if str[i] == k:
            if ans[n] == -1:
                ans[n] = i
            else:
                break
        else:
            pass

print(ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6],
    ans[7], ans[8], ans[9], ans[10], ans[11], ans[12], ans[13],
    ans[14], ans[15], ans[16], ans[17], ans[18], ans[19], ans[20],
    ans[21], ans[22], ans[23], ans[24], ans[25],)
for j in range(len(ans)):
    print(ans[j], '',end='')
