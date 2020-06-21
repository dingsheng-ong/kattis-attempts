import sys

for line in sys.stdin.read().strip().split('\n'):
  s, p, y, j = list(map(int, line.split()))

  Y = (12 + j - y - p) // 3
  P = (12 + j - Y - s) // 2
  S = 12 + j - P - Y

  print(S, P, Y)
