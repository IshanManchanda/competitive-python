# https://www.codechef.com/ICL2018/problems/ICL1801
def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	sort = sorted

	t = int1(rl())
	for i in range(t):
		a = []
		b = 0
		n, m = [int1(x) for x in rl().split()]

		for j in range(n):
			a += [int1(x) for x in rl().split()]
		a = sort(a, reverse=True)

		for j in range(len(a)):
			if j % 2 == 0:
				b += a[j]
			else:
				b -= a[j]

		if b > 0:
			wl("Cyborg\n")
		else:
			wl("Draw\n")


main()
