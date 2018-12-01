dp = [0] + [-1] * 10000000


def solve(a, n):
	global dp
	if dp[n] != -1:
		return dp[n]
	if n == 0:
		return 0
	if n == 1:
		dp[1] = a[0]
		return dp[1]
	if n == 2:
		dp[2] = a[1]
		return dp[2]
	if n == 3:
		dp[3] = a[2]
		return dp[3]
	dp[n] = a[n - 1] + min(solve(a, n - 1), solve(a, n - 2), solve(a, n - 3))
	return dp[n]


def main():
	from sys import stdin, stdout, setrecursionlimit
	setrecursionlimit(10000000)
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	n = int1(rl().strip())
	a = list(map(int1, rl().strip().split()))
	solve(a, n)
	wl(str(sum(a) - min(dp[n - 2:n + 1])))


main()
