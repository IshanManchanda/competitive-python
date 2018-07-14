def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	for line in stdin:
		m = 0
		i, j = map(int1, line.split()[:2])
		for k in range(min(i, j), max(i, j) + 1):
			n = 0
			while k != 1:
				k = k / 2 if not k % 2 else 3 * k + 1
				n += 1
			m = max(m, n)
		wl("%d %d %d\n" % (i, j, m + 1))
	exit(0)


main()
