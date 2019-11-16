# https://www.codechef.com/ZCOPRAC/problems/ZCO14004
dp = [-1] * int(1e6)


def solve(a, d):
	if d < 0:
		return 0
	if d == 0:
		return a[0]
	if d == 1:
		return a[0] + a[1]

	if dp[d] != -1:
		return dp[d]

	dp[d] = max(
		solve(a, d - 1),
		solve(a, d - 2) + a[d],
		solve(a, d - 3) + a[d] + a[d - 1]
	)
	return dp[d]


def main():
	from sys import stdin, stdout, setrecursionlimit
	setrecursionlimit(int(1e6))
	rl = stdin.readline

	n = int(rl())
	a = [int(x) for x in rl().split()]

	if n < 3:
		stdout.write(str(sum(a)))
		return

	stdout.write(str(solve(a, n - 1)))


main()
