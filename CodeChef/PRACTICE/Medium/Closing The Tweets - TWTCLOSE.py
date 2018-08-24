def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1, str1 = int, str

	n, k = map(int, rl().split())
	a = [0] * (n + 1)
	o = 0
	for _ in range(k):
		i = rl().strip()
		if i[:8] == "CLOSEALL":
			a = [0] * (n + 1)
			o = 0
		else:
			c = int1(i[6:])
			if a[c]:
				a[c] = 0
				o -= 1
			else:
				a[c] = 1
				o += 1
		wl(str1(o) + '\n')


main()
