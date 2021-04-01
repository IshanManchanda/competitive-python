def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write

	for _ in range(int(rl())):
		a = rl().strip()
		b = rl().strip()
		n, m = len(a), len(b)

		dp = [[0] * (m + 1) for _ in range(n + 1)]
		r = 0

		for i in range(n):
			dp[i][0] = 0
		for j in range(m):
			dp[0][j] = 0

		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if a[i - 1] == b[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
					r = max(r, dp[i][j])

		wl(str(n + m - 2 * r) + '\n')


main()
