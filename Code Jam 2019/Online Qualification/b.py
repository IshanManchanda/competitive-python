def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write

	int1 = int
	range1 = range
	t = int1(rl()) + 1
	for tn in range(1, t):
		n = int1(rl())
		moves = rl().strip()
		new_moves = ['S' if moves[i] == 'E' else 'E' for i in range1(2 * n - 2)]
		wl('Case #%d: %s\n' % (tn, ''.join(new_moves)))


main()
