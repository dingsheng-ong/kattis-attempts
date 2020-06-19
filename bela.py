import sys

V = {
  'A': [11, 11],
  'K': [ 4,  4],
  'Q': [ 3,  3],
  'J': [20,  2],
  'T': [10, 10],
  '9': [14,  0],
  '8': [ 0,  0],
  '7': [ 0,  0],
}
x = sys.stdin.read().strip().split('\n')
n, b = x.pop(0).split()
print(sum(map(lambda k: V[k[0]][k[1] != b], x)))
