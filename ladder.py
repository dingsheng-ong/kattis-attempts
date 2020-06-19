import math
h, v = list(map(int, input().split()))
print(math.ceil(h / math.sin(math.radians(v))))
