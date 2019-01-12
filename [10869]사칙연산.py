def sum(a, b):
    return a + b

def subs(a, b):
    return a - b

def mul(a, b):
    return a * b

def remain(a, b):
    return a % b

def quotient(a, b):
    return int(a / b)

def calcul(a, b):
    print(sum(a, b))
    print(subs(a, b))
    print(mul(a, b))
    print(quotient(a, b))
    print(remain(a, b))

a, b = map(int, input().split())
calcul(a, b)
