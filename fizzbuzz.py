x, y, n = list(map(int, input().split()))
print('\n'.join([[str(k), 'Fizz', 'Buzz', 'FizzBuzz'][(k % x == 0) + (k % y == 0) * 2] for k in range(1, n + 1)]))
