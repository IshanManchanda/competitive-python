dp = [0] * 10000
x = {}


def f(i):
	if i < 0:
		return 0
	if dp[i]:
		return 1
	if i in x:
		dp[i] = 1
		return 1

	for j in x:
		if f(i - j):
			return 1
	return 0


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	range1 = range
	sorted1 = sorted
	global x

	for _ in range1(int1(rl())):
		n = int1(rl())
		x = {int1(i) for i in rl().split()}
		k = int1(rl())
		wl('1' if f(k) else '0')


main()
