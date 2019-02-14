razer = input()
razer_new = []


for i in range(len(razer)):
    if razer[i:i+2] == '()':
        razer_new.append('0')
    elif razer[i-1:i+1] == '()':
        pass
    else:
        razer_new.append(razer[i])

ans = 0
num = 0

for n, i in enumerate(razer_new):
    if i == '(':
        num += 1
    elif i == '0':
        ans += num
    else:
        num -= 1
        ans += 1

print(ans)
