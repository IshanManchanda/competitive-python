def main():
	from sys import stdin, stdout
	from math import gcd
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	t = int1(rl())
	for i in range(t):
		b = m = 0
		n, k = [int1(x) for x in rl().split()]
		s = rl()

		for c in s:
			if (ord(c) - 96) > (2 * k):
				b += ord(c) - 96
				m += 1
		a = ((n - (2 * m)) * k) + b
		g = gcd(a, k)
		wl(str1(int1(a / g)) + " " + str1(int1(k / g)) + "\n")


main()
