dial = input()

alp = [0, 0, 0, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ans = 0

for i in dial:
    for k in range(3, 11):
        if i in alp[k]:
            ans += k
        else:
            pass

print(ans)
