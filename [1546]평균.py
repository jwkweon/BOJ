T = int(input())
list = input().split()
list_int = map(int, list)

M = max(list_int)
sum = 0

for t in range(T):
    list[t] = int(list[t]) / M * 100
    sum += float(list[t])

print("%0.6f" %(sum / T))
