def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	b = []
	a = b.append

	N, k = map(int1, rl().split())
	for i in xrange(N):
		a(int1(rl()))
	n = len([x / x for x in b if ((x % k) == 0)])

	stdout.write(str(n))


if __name__ == "__main__":
	main()
