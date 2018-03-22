def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	t = int1(rl())
	for i in range(t):
		x, y = [int1(x) for x in rl().split()]
		n = y - x
		a = 4 * x * x
		b = ((2 * n) + 1) * ((2 * n) - 1) / 3
		c = 4 * n
		wl(str(int((n * ((a + b + c) % 1000000007)) % 1000000007)))

c
main()
