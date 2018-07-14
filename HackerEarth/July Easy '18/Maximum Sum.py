def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	rl()
	b = list(map(int1, rl().split(" ")))
	a = [x for x in b if x >= 0]
	wl("%d %d\n" % ((sum(a), len(a)) if len(a) != 0 else (max(b), 1)))


main()
