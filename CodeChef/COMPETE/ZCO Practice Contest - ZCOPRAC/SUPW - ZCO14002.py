# https://www.codechef.com/ZCOPRAC/problems/ZCO14002
dp = [-1] * int(1e6)


def solve(a, d):
	if d < 2:
		return 0

	if dp[d] != -1:
		return dp[d]

	dp[d] = min(
		a[d] + solve(a, d - 1),
		a[d - 1] + solve(a, d - 2),
		a[d - 2] + solve(a, d - 3)
	)

	return dp[d]


def main():
	from sys import stdin, stdout, setrecursionlimit
	setrecursionlimit(int(5e5))
	rl = stdin.readline

	n = int(rl())
	a = [int(x) for x in rl().split()]

	stdout.write(str(solve(a, n - 1)))


main()
