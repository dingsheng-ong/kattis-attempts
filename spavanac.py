h, m = list(map(int, input().split()))
t = h * 60 + m - 45
if t <= 60: t += 1440
print(t // 60, t % 60)
