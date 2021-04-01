def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write

	for _ in range(int(rl())):
		n, k = map(int, rl().split())
		s = rl().strip()
		a = [n + 1] * n

		i1 = 0
		while s[i1] != '*':
			i1 += 1
		i2 = n - 1
		while s[i2] != '*':
			i2 -= 1

		if i1 == i2:
			wl("1\n")
			continue

		a[i1] = 1
		for i in range(i1 + 1, i2 + 1):
			if s[i] == '.':
				continue
			for j in range(i - k, i):
				a[i] = min(a[i], 1 + a[j])

		wl(str(a[i2]) + '\n')


main()
