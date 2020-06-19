import sys
print('\n'.join(['{} is {}'.format(k, ['even', 'odd'][int(k) % 2]) for k in sys.stdin.read().strip().split('\n')[1:]]))
