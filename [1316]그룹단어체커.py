def group_chk(str_in):
    checker = []
    for i, s in enumerate(str_in):
        if s in checker:
            if str_in[i] == str_in[i - 1]:
                pass
            else:
                return 0
        else:
            checker.append(s)
    return 1

T = int(input())
ans = 0
for t in range(T):
    str_in = input()
    ans += group_chk(str_in)

print(ans)
