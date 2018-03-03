def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	t = int1(rl())
	for i in range(t):
		n = int1(rl())
		l = 0
		for j in range(n):
			p, q, d = [int1(x) for x in rl().split()]
			l += q * p * d * d / 10000
		wl(str1(l) + '\n')


main()
