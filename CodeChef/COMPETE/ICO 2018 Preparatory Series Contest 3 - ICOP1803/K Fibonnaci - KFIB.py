def f(n, k, s, x):
	if n <= k:
		return 1
	return s([f(y, k, s, x) for y in x(n-k, n)])


def main():
	from sys import stdin, stdout
	N, K = map(int, stdin.readline().split())
	stdout.write(str(f(N, K, sum, xrange) % 1000000007))
	pass


main()
