x = [sum(map(int, input().split())) for _ in range(5)]
i, v = max(enumerate(x), key=lambda k: k[1])
print(i + 1, v)
