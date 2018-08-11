def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	for _ in range(int1(rl())):
		n = int1(rl())
		wl(str1(int1(n * (n + 1) * (n + 2) / 6)) + "\n")


main()
