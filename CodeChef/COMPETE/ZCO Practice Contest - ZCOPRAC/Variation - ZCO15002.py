def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int

	N, k = map(int1, rl().split())
	s = sorted([int1(x) for x in rl().split()])
	i = j = v = 0

	while i < N and j < N:
		if s[j] - s[i] >= k:
			v += N - j
			i += 1
		else:
			j += 1

	stdout.write(str(v))


main()
