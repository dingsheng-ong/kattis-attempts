f = lambda x: [k for k in x.strip().split(':')[1].strip().split(',') if len(k)]
W = ['P' + k if len(k) < 3 else k for k in f(input())]
B = ['P' + k if len(k) < 3 else k for k in f(input())]
M = [[None for _ in range(8)] for _ in range(8)]

for c in W:
  t, i, j = list(c)
  t = t.upper()
  i = ord(i) - 97
  j = 8 - int(j)
  M[j][i] = t

for c in B:
  t, i, j = list(c)
  t = t.lower()
  i = ord(i) - 97
  j = 8 - int(j)
  M[j][i] = t  

for i in range(8):
  print('+---' * 8 + '+\n|', end='')
  for j in range(8):
    b = ':' if (i + j) % 2 else '.'
    if M[i][j]:
      b = b + M[i][j] + b
    else:
      b = b * 3
    print(b, end='|')
  print()
print('+---' * 8 + '+')
