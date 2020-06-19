input()
print(len(list(filter(lambda k: k < 0, map(int, input().split())))))
