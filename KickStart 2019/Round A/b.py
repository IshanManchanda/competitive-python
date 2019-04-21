def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write

	int1 = int

	t = int1(rl())
	for tc in range(1, t + 1):
		n, q = map(int1, rl().split())
		a = []
		b = a.append

		for i in range(q):
			b(tuple(map(int1, rl().split())))
		a = sorted(a)
		o = [[0, x] for x in range(q)]

		for i in range(q - 1):
			for j in range(i + 1, q):
				if a[j][0] > a[i][1]:
					break
				o[i][0] += a[i][1] - a[j][0] + 1
				o[j][0] += a[i][1] - a[j][0] + 1
		o = sorted(o)

		for i in range(q):
			# Assign seats to o[i][1]
			pass


main()
