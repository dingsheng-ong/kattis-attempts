n, w, h = list(map(int, input().split()))
a = w * w + h * h
for i in range(n):
  k = int(input())
  k = k * k
  print('DA' if k <= a else 'NE')
