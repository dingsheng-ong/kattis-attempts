import sys

data = [[], []]
x = sys.stdin.read().strip().split('\n')[1::2]
x = list(map(lambda k: k.split('|')[1:-1], x))
for i in range(8):
  for j in range(8):
    t = x[i][j][1]
    if t.isalpha():
      p = t.upper() + chr(97 + j) + str(8 - i)
      data[t.islower()].append(p)

prec = {k: i for i, k in enumerate('KQRBNP')}

f = lambda k: prec[k[0]] * 100 + ord(k[1]) - 97 + 10 * int(k[2])
g = lambda k: prec[k[0]] * 100 + ord(k[1]) - 97 + 10 * (8 - int(k[2]))

w = ','.join(sorted(data[0], key=lambda k: f(k)))
b = ','.join(sorted(data[1], key=lambda k: g(k)))

print('White:', w.replace('P', ''))
print('Black:', b.replace('P', ''))
