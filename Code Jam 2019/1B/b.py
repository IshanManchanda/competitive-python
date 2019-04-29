def main():
	from sys import stdout, stdin
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	t, w = map(int1, rl().split())
	if w == 2:
		wl(-1)
		exit(0)
	for tn in range(1, t + 1):
		wl('1')
		n1 = int1(rl())
		wl('2')
		n2 = int1(rl())
		wl('3')
		n3 = int1(rl())
		wl('4')
		n4 = int1(rl())

		wl('6')
		n6 = int1(rl())
		wl('7')
		n7 = int1(rl())

		a1 = (n7 - n6) // 64
		a2 = n2 - n1 - 2 * a1
		a3 = n3 - n2 - 4 * a1
		a4 = n4 - n3 - 8 * a1 - 2 * a2
		# a6 =

		ans = 0

		wl('Case #%d: %d' % (tn, ans))


main()
