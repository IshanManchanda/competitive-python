def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	T = int1(rl())
	l = []
	a = l.append
	for _ in xrange(T):
		a(int1(rl()))
	stdout.write("\n".join(str(x) for x in sorted(l)))


main()
