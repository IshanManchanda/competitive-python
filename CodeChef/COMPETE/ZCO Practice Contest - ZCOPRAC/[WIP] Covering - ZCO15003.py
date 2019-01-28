def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	n = int1(rl())
	a = []
	aa = a.append
	for i in range(n):
		aa(tuple(map(int1, rl().split())))
	a = sorted(a, key=lambda x: x[0])

	for i in range(n):
		for j in range(i + 1, n):
			if a[i][0] <= a[j][0] <= a[i][1]:
				n -= 1
				continue
			break
	wl(str(n))


main()
