def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	map1 = map

	t = int1(rl().strip())
	for _ in range(t):
		a, b, c, d = map1(int1, rl().strip().split())
		if a == b and c == d:
			wl("YES\n")
		elif a == c and b == d:
			wl("YES\n")
		elif a == d and b == c:
			wl("YES\n")
		else:
			wl("NO\n")


main()
