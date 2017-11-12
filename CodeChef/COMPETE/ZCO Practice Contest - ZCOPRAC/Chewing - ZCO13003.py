def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int

	N, k = map(int1, rl().split())
	s = sorted([int1(x) for x in rl().split()])
	for i in xrange(N):
		if s[i] > k:
			del s[i:]
			break
	n = l = 0
	r = len(s) - 1

	while l < r:
		if s[l] + s[r] < k:
			n += r - l
			l += 1
		else:
			r -= 1

	stdout.write(str(n))


main()
