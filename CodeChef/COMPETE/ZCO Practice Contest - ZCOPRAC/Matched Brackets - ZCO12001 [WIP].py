def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	d = md = s = ms = 0
	dp = mdp = sp = msp = 1
	n = int1(rl())
	b = rl().strip().split(' ')

	for i in range(n):
		if b[i] == '1':
			if d == 0:
				sp = i + 1
			else:
				s += 1
			d += 1
		else:
			if d > md:
				md = d
				mdp = i
			d -= 1
			s += 1
			if d == 0:
				if s > ms:
					msp = sp
				s = 0

	wl('%d %d %d %d' % (md, mdp, ms + 1, msp))


main()
