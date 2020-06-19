a, b = list(map(int, input().split()))
if a > b: a, b = b, a
print(str.join('\n', map(str, range(a + 1, b + 2))))
