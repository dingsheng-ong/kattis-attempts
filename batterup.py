_ = input()
x = list(filter(lambda k: k >= 0, map(int, input().split())))
print(sum(x) / len(x))
