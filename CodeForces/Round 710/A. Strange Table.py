def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write

	for _ in range(int(rl())):
		n, m, x = map(int, rl().split())
		a = (x - 1) % n
		b = (x - 1) // n
		r = 1 + m * a + b
		wl(str(r) + '\n')


main()
