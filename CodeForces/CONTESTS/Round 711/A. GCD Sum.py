def main():
	from sys import stdin, stdout
	from math import gcd
	rl = stdin.readline
	wl = stdout.write

	for _ in range(int(rl())):
		i = int(rl())
		while (i % 3 != 0) and (gcd(i, sum(int(x) for x in str(i))) == 1):
			i += 1
		wl(str(i) + "\n")


main()
