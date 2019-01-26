E, M, S = map(int, input().split())

while True:
    E_chk = M % 15
    S_chk = M % 19
    if E_chk == 0:
        E_chk = 15
    if S_chk == 0:
        S_chk = 19

    if E_chk == E and S_chk == S:
        print(M)
        break
    else:
        M += 28
