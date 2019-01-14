month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

x, y = map(int, input().split())
sum = 0
for i in range(x):
    sum += month[i]
sum += y
print(day[sum%7])
