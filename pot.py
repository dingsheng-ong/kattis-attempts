import sys
print(sum([int(k[:-1]) ** int(k[-1]) for k in sys.stdin.read().strip().split('\n')[1:]]))
