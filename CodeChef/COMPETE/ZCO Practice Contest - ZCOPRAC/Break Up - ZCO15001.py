# https://www.codechef.com/ZCOPRAC/problems/ZCO15001
def is_pal(a):
	for x, y in zip(a[:len(a) // 2], a[::-1]):
		if x != y:
			return False
	return True


def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n = int(rl())
	a = [int(x) for x in rl().split()]
	dp = [i for i in range(n + 1)]

	for i in range(1, n):
		dp[i + 1] = dp[i] + 1
		for j in range(i):
			if is_pal(a[j:i + 1]):
				dp[i + 1] = min(dp[i + 1], dp[j] + 1)

	stdout.write(str(dp[-1]))


main()
