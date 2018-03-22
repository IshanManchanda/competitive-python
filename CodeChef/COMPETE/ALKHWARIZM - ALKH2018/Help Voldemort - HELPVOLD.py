def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	rl()
	a = [int1(x) for x in rl().split()]
	a = sorted(a)
	c = 0
	for i in range(len(a) - 1):
		c += a[i] * a[i + 1]
	wl(str1(c))


main()
