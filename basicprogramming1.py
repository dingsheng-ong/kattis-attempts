N, t = list(map(int, input().split()))
A = list(map(int, input().split()))

def g(A):
  i = 0
  c = 0
  while c <= len(A):
    i = A[i]
    if i > len(A) - 1:
      print('Out')
      return
    if i == len(A) - 1:
      print('Done')
      return
    c += 1
  print('Cyclic')

f = [
  lambda A: print(7),
  lambda A: print(['Smaller', 'Equal', 'Bigger'][(A[0] >= A[1]) + (A[0] > A[1])]),
  lambda A: print(sorted(A[:3])[1]),
  lambda A: print(sum(A)),
  lambda A: print(sum(filter(lambda k: k % 2 == 0, A))),
  lambda A: print(str.join('', map(lambda k: chr(ord('a') + k % 26), A))),
  lambda A: g(A)
]
f[t - 1](A)
