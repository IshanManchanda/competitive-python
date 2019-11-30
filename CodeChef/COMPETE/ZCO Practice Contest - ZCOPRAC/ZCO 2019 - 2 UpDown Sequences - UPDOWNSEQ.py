# https://www.codechef.com/ZCOPRAC/problems/UPDOWSEQ
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	for _ in range(int(rl())):
		n = int(rl())
		a = [int(x) for x in rl().split()]

		dp = [[1] * 2 for _ in range(n)]

		for i in range(n - 2, -1, -1):
			if a[i] <= a[i + 1]:
				dp[i][0] = 1 + dp[i + 1][1]

			if a[i] >= a[i + 1]:
				dp[i][1] = 1 + dp[i + 1][0]

		m = 0
		for i in range(n):
			l = dp[i][0]
			if l % 2 == 0:
				m = max(m, l + dp[i + l - 1][0])
			else:
				m = max(m, l + dp[i + l - 1][1])

		stdout.write(str(m) + '\n')


main()
