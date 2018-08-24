def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	range1 = range
	map1 = map
	str1 = str

	for _ in range1(int1(rl())):
		n, m = map1(int1, rl().split())
		adj = [[] for _ in range1(n)]
		t = [(0, 0)]
		v = [1] + [0] * (n - 1)

		for _ in range1(m):
			x, y = map1(int1, rl().split())
			adj[x - 1] += [y - 1]
			adj[y - 1] += [x - 1]

		while t:
			i, d = t[0]
			del t[0]
			for j in adj[i]:
				if j == n - 1:
					break
				if not v[j]:
					v[j] = 1
					t.append((j, d + 1))
		wl(str1(d + 1) + '\n')


main()
