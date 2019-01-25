T = int(input())

#def tri_dp(list, list_max, k):
#    big_list = []
#    for i in range(k):
#        big_list.append(max(list[i], list[i + 1]))
#        list_max[i] = int(big_list[i]) + int(list_max[i])

tri_list = []

for t in range(T):
    tri_list.append(input().split())

#for i in range(T):
#    k = T - i - 1
#    if k == 0:
#        break
#    tri_dp(tri_list[k], tri_list[k - 1], k)
#
#print(int(tri_list[0][0]))


dp_list = [[] for i in range(T)]


def dp(i):
    for m in range(i + 1):
        if m == 0:
            dp_list[i].append(int(tri_list[i][m]) + dp_list[i - 1][m])
        elif m == i:
            dp_list[i].append(int(tri_list[i][m]) + dp_list[i - 1][m - 1])
        else:
            dp_list[i].append(int(tri_list[i][m]) + max(dp_list[i - 1][m - 1], dp_list[i - 1][m]))

for i in range(T):
    if i == 0:
        dp_list[i].append(int(tri_list[i][0]))
    else:
        dp(i)

print(max(dp_list[T - 1]))
