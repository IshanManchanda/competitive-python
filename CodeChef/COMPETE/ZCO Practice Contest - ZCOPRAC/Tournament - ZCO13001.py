def main():
	from sys import stdin, stdout
	int1 = int
	rl = stdin.readline

	N = int1(rl())
	s = sorted([int1(x) for x in rl().split()])
	stdout.write(str(sum([s[N - i] * (N + 1 - (i * 2)) for i in range(1, N+1)])))


main()
