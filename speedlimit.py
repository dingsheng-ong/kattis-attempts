while True:
  n = int(input())
  if n < 0: break
  d = p = 0
  for _ in range(n):
    s, t = list(map(int, input().split()))
    d += s * (t - p)
    p = t
  print('{:d} miles'.format(d))
