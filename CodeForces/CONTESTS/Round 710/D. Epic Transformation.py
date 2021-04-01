def main():
	from sys import stdin, stdout
	from collections import Counter
	rl = stdin.readline
	wl = stdout.write

	for _ in range(int(rl())):
		n = int(rl().strip())
		c = Counter(rl().strip().split())
		a = c.most_common(1)[0][1]

		if a * 2 <= n:
			wl(str(n % 2)+"\n")
		else:
			wl(str(2 * a - n) + '\n')


main()
