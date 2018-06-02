def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	r1 = range

	t = int1(rl())
	for _ in r1(t):
		x, y, n, s, e, w, p = [int1(x) for x in rl().split()]
		c = (n * y) + (e * x)
		if c > p:
			wl("-1\n")
		elif c == p:
			wl(str1(x + y) + "\n")
		else:
			cs = sorted([n + s, e + w], reverse=True)
			ca = p - c
			j = 0
			while (ca % cs[0]) != 0:
				ca -= cs[1]
				j += 2
				if ca == 0:
					wl(str1(x + y + j) + "\n")
				if ca < 0:
					wl("-1\n")
					break
			if ca > 0:
				j += 2 * int1(ca / cs[0])
				wl(str1(x + y + j) + "\n")


main()
