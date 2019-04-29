def main():
	from sys import stdout, stdin
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	t = int1(rl())
	for tn in range(1, t + 1):
		ans = 0

		wl('Case #%d: %d' % (tn, ans))


main()
