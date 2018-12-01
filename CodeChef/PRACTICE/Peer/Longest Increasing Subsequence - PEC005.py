dp = []


def lis(a, n):
	global dp
	if dp[n]:
		return dp[n]

	m = 0
	for i in range(n - 1, -1, -1):
		if a[i] < a[n]:
			if lis(a, i) > m:
				m = dp[i]
	dp[n] = 1 + m
	return dp[n]


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	global dp

	t = int1(rl().strip())
	for _ in range(t):
		n = int1(rl().strip())
		dp = [1] + [0] * n
		a = list(map(int1, rl().strip().split()))
		lis(a, n - 1)
		wl(str1(max(dp)) + '\n')


main()
