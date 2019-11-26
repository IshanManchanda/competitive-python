# https://www.codechef.com/ZCOPRAC/problems/ZCO13002
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n, m = (int(x) for x in rl().split())
	grid = [[int(x) for x in rl().split()] for _ in range(n)]
	charms = [[int(x) for x in rl().split()] for _ in range(m)]

	n_inf = -9999
	dp = [[n_inf] * n for _ in range(n)]

	for c in charms:
		c[0] -= 1
		c[1] -= 1

		x = max(0, c[0] - c[2])
		while x < n and x <= c[0] + c[2]:
			off = abs(x - c[0])
			y = max(0, c[1] - c[2] + off)
			while y < n and y <= c[1] + c[2] - off:
				dp[x][y] = grid[x][y]
				y += 1
			x += 1

	for x in range(1, n):
		if dp[x - 1][0] == n_inf:
			for x1 in range(x, n):
				dp[x1][0] = n_inf
			break
		dp[x][0] += dp[x - 1][0]

	for y in range(1, n):
		if dp[0][y - 1] == n_inf:
			for y1 in range(y, n):
				dp[0][y1] = n_inf
			break
		dp[0][y] += dp[0][y - 1]

	for x in range(1, n):
		for y in range(1, n):
			m = max(dp[x - 1][y], dp[x][y - 1])
			dp[x][y] = m + dp[x][y] if m != n_inf else n_inf

	if dp[-1][-1] != n_inf:
		stdout.write('YES\n')
		stdout.write(str(dp[-1][-1]))
	else:
		stdout.write('NO')


main()
