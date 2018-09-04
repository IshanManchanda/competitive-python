def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	for _ in range(int1(rl())):
		n, x = map(int1, rl().split())
		a = map(int1, rl().split())
		t = 0
		for i in a:
			if i >= x:
				t = 1
				break
		wl("YES\n" if t else "NO\n")


main()
