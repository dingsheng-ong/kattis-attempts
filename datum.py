q, m = list(map(int, input().split()))
h = q + (13*(m + 12 * (m < 3) + 1) // 5) - 24 - (m < 3)
w = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(w[h % 7])
