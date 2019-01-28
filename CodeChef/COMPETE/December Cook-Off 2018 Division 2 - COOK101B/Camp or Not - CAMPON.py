def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	for _ in range(int1(rl())):
		d = int1(rl())
		a = [0] * 32
		for i in range(d):
			day, probs = [int1(x) for x in rl().split()]
			a[day - 1] = probs

		p = [a[0]] + [0] * 31
		for i in range(1, 32):
			p[i] = (p[i - 1] + a[i])

		q = int1(rl())
		for _ in range(q):
			dead, req = [int1(x) for x in rl().split()]
			if p[dead - 1] >= req:
				wl("Go Camp\n")
			else:
				wl("Go Sleep\n")


main()
