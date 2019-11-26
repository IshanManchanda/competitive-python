# https://www.codechef.com/CMEL2018/problems/CNDLOVE
def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	t = int1(rl())
	for i in range(t):
		rl()
		wl(
			"NO\n" if sum([int1(x) for x in rl().split()]) % 2 == 0
			else "YES\n"
		)


main()
