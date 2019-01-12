'''def pr(a):
    print(a)

for i in range(3):
    a = input()
    pr(a)

pr()

list = []
list.append(input())
list.append(input())
if list[-1:] == '':
    print(list[-1:])


print(list)
print(list[-1:])
'''

while True:
    try:
        print(input())
    except EOFError:
        break
