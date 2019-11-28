# https://www.codechef.com/ZCOPRAC/problems/ZCO13004
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	# Time taken to reach end is determined purely by size of grid
	# We simply need to determine if it is possible to reach it

	# Create dp table, mark all as visitable
	# Mark cells with blasters as unvisitable

	# Now, iterate over blasters.
	# For each blaster, check every cell in its row and col.
	# For each cell, there is a definite time at which spaceman can be at it

	# Pulse will take time t1 extra to reach cell after fire
	# Therefore, t0 should be = t1 + tstart + nf
	# Hence, we mod t0 - t1 - tstart with f

	# Finally, just try to find a path.
	# If a path exists, simply print n + m - 2 as the time to reach

	n, m, k = (int(x) for x in rl().split())
	a = [[int(x) for x in rl().split()] for _ in range(k)]

	dp = [[1] * m for _ in range(n)]
	for b in a:
		b[0] -= 1
		b[1] -= 1
		dp[b[0]][b[1]] = 0

		x, y = b[0], 0
		while y < m:
			t_cell = x + y
			t_check = t_cell - b[2] - abs(y - b[1])
			if t_check < 0:  # Negative time is impossible
				y += 1
				continue

			if t_check % b[3] == 0:
				dp[x][y] = 0
			y += 1

		x, y = 0, b[1]
		while x < n:
			t_cell = x + y
			t_check = t_cell - b[2] - abs(x - b[0])
			if t_check < 0:
				x += 1
				continue

			if t_check % b[3] == 0:
				dp[x][y] = 0
			x += 1

	for x in range(1, n):
		dp[x][0] = dp[x][0] and dp[x - 1][0]

	for y in range(1, m):
		dp[0][y] = dp[0][y] and dp[0][y - 1]

	for x in range(1, n):
		for y in range(1, m):
			dp[x][y] = dp[x][y] and (dp[x - 1][y] or dp[x][y - 1])

	if dp[-1][-1]:
		stdout.write('YES\n')
		stdout.write(str(n + m - 2))
	else:
		stdout.write('NO')


main()
