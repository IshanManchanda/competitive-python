# https://www.codechef.com/ZCOPRAC/problems/SINGTOUR
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	# The score of each singer is a function of their indices
	# when sorted in order of lower and upper limit.

	# This works because each of the 2 limits independently influences
	# a single point for each singer.
	# Further, it doesn't matter how many wins/loses/ties each singer has:
	# any time they exceed any limit of another, they gain a point.

	# First, we sort the singers by their lower limit in desc order.
	# For a singer at index i,
	# They gain a point for each of i singers with a higher lower limit.
	# This is because they either tie or win with them.

	# Similarly, we sort the singers by their upper limit in asc order.
	# For a singer at index j,
	# They gain a point for each of j singers with a lower upper limit.

	# Alternatively, we could add 2 * i initially,
	# and then subtract n - j - 1, and other such variations.

	t = int(rl())
	for _ in range(t):

		n = int(rl())
		a = [[int(x) for x in rl().split()] + [i] for i in range(n)]
		s = [0] * n

		a.sort(reverse=True)
		for i, x in enumerate(a):
			s[x[2]] += i

		a.sort(key=lambda x: x[1])
		for j, x in enumerate(a):
			s[x[2]] += j

		stdout.write(' '.join(str(x) for x in s) + '\n')


main()
