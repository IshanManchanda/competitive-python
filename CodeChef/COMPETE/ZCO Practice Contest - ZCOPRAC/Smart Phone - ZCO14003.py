def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	b = []
	a = b.append

	N = int1(rl())
	for i in range(N):
		a(int1(rl()))

	b = sorted(b, reverse=True)
	stdout.write(str(max([((x+1)*b[x]) for x in range(N)])))


main()
