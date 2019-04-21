def main():
	from sys import stdout, stdin
	rl = stdin.readline
	wl = stdout.write

	int1 = int
	t = int1(rl())
	for tc in range(1, t + 1):
		r, c = map(int1, rl().split())
		grid = [[0] * c for i in range(r)]
		offices = []

		for i in range(r):
			inp = rl().strip()
			for j in range(c):
				if inp[j] == '1':
					offices.append((i, j))

		mmd = 0
		mmds = []
		for i in range(r):
			for j in range(c):
				md = 1001
				for office in offices:
					di = office[0] - i
					if di > md:
						break
					d = abs(di) + abs(office[1] - j)
					md = min(md, d)
					if d == 0:
						break

				grid[i][j] = md
				# if md > mmd:
				# 	mmds = [(i, j)]
				# 	mmd = md
				# elif md == mmd:
				# 	mmds.append((i, j))

		nmmd = 1001
		# for office in mmds:
		# 	nmd = 0
		# 	for i in range(r):
		# 		for j in range(c):
		# 			d = abs(office[0] - i) + abs(office[1] - j)
		# 			nmd = max(nmd, min(grid[i][j], d))
		# 	nmmd = min(nmmd, nmd)

		for ox in range(r):
			for oy in range(c):
				nmd = 0
				for i in range(r):
					for j in range(c):
						d = abs(ox - i) + abs(oy - j)
						nmd = max(nmd, min(grid[i][j], d))
				nmmd = min(nmmd, nmd)

		wl('Case #%d: %d\n' % (tc, nmmd))


main()
