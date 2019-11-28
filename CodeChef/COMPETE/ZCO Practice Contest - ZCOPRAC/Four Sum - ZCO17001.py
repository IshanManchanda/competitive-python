# https://www.codechef.com/ZCOPRAC/problems/ZCO17001
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	inp = [int(x) for x in rl().split()]
	n, t, a = inp[0], inp[1], inp[2:]
	s, c = 0, {}

	for k in range(2, n - 1):
		for x in a[:k - 1]:
			p = x + a[k - 1]
			c[p] = 1 + c[p] if p in c else 1

		for z in a[k + 1:]:
			p = t - z - a[k]
			s += c[p] if p in c else 0

	stdout.write(str(s))


main()
