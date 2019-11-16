# https://www.codechef.com/ZCOPRAC/problems/ZCO14001
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n, h = (int(x) for x in rl().split())
	a = [int(x) for x in rl().split()]
	cs = [int(x) for x in rl().split()]

	p = b = 0
	for c in cs:
		if c == 1 and p != 0:
			p -= 1
		elif c == 2 and p != n - 1:
			p += 1
		elif c == 3 and not b and a[p] > 0:
			a[p] -= 1
			b = 1
		elif c == 4 and b and a[p] < h:
			a[p] += 1
			b = 0
		else:
			break

	stdout.write(' '.join(str(x) for x in a))


main()
