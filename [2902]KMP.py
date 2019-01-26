str_in = input()

for i in str_in:
    if ord(i) >= 65 and ord(i) <= 90:
        print(i, end='')
