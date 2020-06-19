import sys

x = sys.stdin.read().strip().split('\n')
a, b = list(zip(*map(lambda k: map(int, k.split()), x)))
print((min(a)+max(a))*2-sum(a), (min(b)+max(b))*2-sum(b))
