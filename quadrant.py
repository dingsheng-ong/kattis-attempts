a, b = int(input()), int(input())
a = (1 - a // abs(a)) // 2
b = (1 - b // abs(b)) // 2
print(b * 2 + (a ^ b) + 1)
