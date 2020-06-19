n = int(input())
H = list(map(int, input().split()))

L, R = [], []
l, r = 0, 0
for i in range(n):
  L.append(l)
  R.append(r)
  l = max(l, H[i])
  r = max(r, H[n - i - 1])
R = R[::-1]

h_max = 0
for i in range(n):
  h = min(L[i], R[i]) - H[i]
  h_max = max(h_max, h)

print(h_max)
