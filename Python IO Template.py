# For timing functions - remove before submitting code
import profile


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	# Single line, single input
	n = int1(rl())
	b = []
	a = b.append
	for i in range(n):
		a(int1(rl()))

	# Single line, multiple input
	n, k = map(int1, rl().split())
	s = [int1(x) for x in rl().split()]

	# Single line, single output
	wl(str1(b))

	# Single line, multiple output
	wl(" ".join([str1(n), str1(k), str1(s)]))


# Timing functions
profile.run('main()')

main()
