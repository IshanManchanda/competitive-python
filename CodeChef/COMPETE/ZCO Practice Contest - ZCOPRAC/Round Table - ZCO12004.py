# https://www.codechef.com/ZCOPRAC/problems/ZCO12004
dp = [[-1] * int(1.1e6), [-1] * int(1.1e6)]


def solve(a, d, l):
	if dp[l][d] != -1:
		return dp[l][d]

	if d == 0:
		return a[0]
	if d == 1:
		return a[1] if l else a[1] + a[0]

	dp[l][d] = a[d] + min(
		solve(a, d - 1, l),
		solve(a, d - 2, l)
	)
	return dp[l][d]


def main():
	from sys import stdin, stdout, setrecursionlimit
	setrecursionlimit(int(1e6))
	rl = stdin.readline

	n = int(rl())
	a = [int(x) for x in rl().split()]

	stdout.write(str(min(
		solve(a, n - 1, 1),
		solve(a, n - 2, 0)
	)))


main()
