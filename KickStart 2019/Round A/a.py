def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write

	int1 = int

	t = int1(rl())
	for tc in range(1, t + 1):
		n, p = map(int1, rl().split())
		s = sorted(list(map(int1, rl().split())))

		# Precompute first round
		m = p * s[p - 1]
		for i in range(0, p):
			m -= s[i]
		mm = m

		# Sliding window from i to i + p.
		for i in range(1, n - p + 1):
			up = i + p - 1

			# Remove last person
			m -= s[up] - s[i - 1]

			# Everyone needs to reach level of s[up]
			# so diff = s[up] - s[up - 1]
			if s[up] != s[up - 1]:
				d = s[up] - s[up - 1]
				m += d * p

			mm = min(mm, m)

		wl('Case #%d: %d\n' % (tc, mm))


main()
