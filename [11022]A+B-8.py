T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    print('Case #%d:' %(t + 1) , '%d + %d = %d'  %(A, B, A + B))
