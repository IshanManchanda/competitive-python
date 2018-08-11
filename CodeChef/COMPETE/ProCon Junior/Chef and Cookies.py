def main():
	from sys import stdin, stdout
	from math import log as l, ceil as c
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	map1 = map

	for _ in range(int1(rl())):
		n, b = map1(int1, rl().split())
		i = int1(l((n * (b - 1) / b) - 1, b))
		pass
		wl(str1(c(n * (b ** (i - 2)) * (b - 1) / ((b ** (i - 1)) - 1))) + "\n")
		pass


main()
