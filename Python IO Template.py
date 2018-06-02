# For timing functions - remove before submitting code
import profile


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	str1 = str

	# Single line, single input
	N = int1(rl())
	b = []
	a = b.append
	for i in range(N):
		a(int1(stdin.readline()))

	# Single line, multiple input
	N, k = map(int1, rl().split())
	s = [int1(x) for x in rl().split()]

	# Single line, single output
	stdout.write(str1(b))

	# Single line, multiple output
	stdout.write(" ".join([str1(N), str1(k), str1(s)]))


# Timing functions
profile.run('main()')


main()
