X = input()
C = dict(zip(set(X), [0, 0, 0]))
for k in X: C[k] += 1
s = sum(map(lambda k: k * k, C.values()))
s += (len(C) == 3) * 7 * min(C.values())
print(s)
