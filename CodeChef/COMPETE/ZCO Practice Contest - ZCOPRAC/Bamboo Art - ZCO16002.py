# https://www.codechef.com/ZCOPRAC/problems/ZCO16002
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	inp = [int(x) for x in rl().split()]
	n, a = inp[0], inp[1:]

	a.sort()
	dp = [[1] * (a[-1] - a[0]) for _ in range(n)]

	for i, x in enumerate(a):
		for j, y in enumerate(a[:i]):
			dp[i][x - y - 1] = 1 + dp[j][x - y - 1]

	stdout.write(str(max(max(x) for x in dp)))


main()
