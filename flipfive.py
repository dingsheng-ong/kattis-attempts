from copy import deepcopy as copy


def flip(m, i, j):
	m_ = copy(m)
	for x, y in [(-1,0),(0,-1),(0,0),(1,0),(0,1)]:
		if i + x < 0 or i + x > 2: continue
		if j + y < 0 or j + y > 2: continue
		m_[i+x][j+y] = not m_[i+x][j+y]
	return m_


def hash(m):
	return sum([m[i // 3][i % 3] * 2 ** i for i in range(9)])


def solve(M):
	if all(map(lambda k: not any(k), M)):
		return 0

	S = [(M, 0)]
	H = []
	
	while len(S):
		m, n = S.pop(0)
		v = hash(m)
		if v in H:
			continue
		else:
			H.append(v)

		for i in range(3):
			for j in range(3):
				m_ = flip(m, i, j)
				if all(map(lambda k: not any(k), m_)):
					return n + 1
				S.append((m_, n + 1))


p = int(input())
for _ in range(p):
	m = [list(map(lambda k: ord(k) < 43, input())) for _ in range(3)]
	n = solve(m)
	print(n)
