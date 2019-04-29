def main():
	from sys import stdout, stdin
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	t = int1(rl())
	for tn in range(1, t + 1):
		p, q = map(int1, rl().split())
		npeople, epeople, speople, wpeople = [], [], [], []
		xcount, ycount = [0] * q, [0] * q

		for i in range(p):
			x, y, d = rl().split()
			if d == 'E':
				epeople.append((int1(x), int1(y)))
			elif d == 'W':
				wpeople.append((int1(x), int1(y)))
			elif d == 'N':
				npeople.append((int1(y), int1(x)))
			else:
				speople.append((int1(y), int1(x)))

		npeople.sort()
		epeople.sort()
		speople.sort()
		wpeople.sort()

		le = len(epeople)
		for i in range(1, le):
			for j in range(epeople[i - 1][0] + 1, min(epeople[i][0] + 1, q - 1)):
				xcount[j] += i
		if le != 0:
			for i in range(epeople[le - 1][0] + 1, q):
				xcount[i] += le

		lw = len(wpeople)
		for i in range(1, lw):
			for j in range(wpeople[i - 1][0], min(wpeople[i][0] + 1, q - 1)):
				xcount[j] -= i
		if lw != 0:
			for i in range(wpeople[lw - 1][0], q):
				xcount[i] -= lw

		ln = len(npeople)
		for i in range(1, ln):
			for j in range(npeople[i - 1][0] + 1, min(npeople[i][0] + 1, q - 1)):
				ycount[j] += i
		if ln != 0:
			for i in range(npeople[ln - 1][0] + 1, q):
				ycount[i] += ln

		ls = len(speople)
		for i in range(1, ls):
			for j in range(speople[i - 1][0], min(speople[i][0] + 1, q - 1)):
				ycount[j] -= i
		if ls != 0:
			for i in range(speople[ls - 1][0], q):
				ycount[i] -= ls

		wl('Case #%d: %d %d\n' % (tn, xcount.index(max(xcount)), ycount.index(max(ycount))))


main()
