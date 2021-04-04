def main():
	from sys import stdin, stdout
	from math import sqrt
	rl = stdin.readline
	wl = stdout.write

	a = rl().strip()
	while len(a) > 1:
		a = str(sum(int(x) for x in a))
	wl(a + '\n')


main()
