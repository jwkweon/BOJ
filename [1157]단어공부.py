alp = input()
upper_alp = alp.upper()
upper_alp_set = list(set(upper_alp))
ans = [0 for i in range(len(upper_alp_set))]

for i in range(len(ans)):
    ans[i] = upper_alp.count(upper_alp_set[i])

max_a = max(ans)
max_alp = []

for i in range(len(ans)):
    if ans[i] == max_a:
        max_alp.append(upper_alp_set[i])
    else:
        pass

if len(max_alp) == 1:
    print(max_alp[0])
else:
    print('?')
