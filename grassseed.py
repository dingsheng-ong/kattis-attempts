C = float(input())
L = int(input())

f = lambda a, b: float(a) * float(b)
x = sum([C * f(*input().split()) for _ in range(L)])
print('{:.7f}'.format(x))
