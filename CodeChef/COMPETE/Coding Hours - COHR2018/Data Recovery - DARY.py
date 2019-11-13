def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	len1, sum1, str1 = len, sum, str

	for _ in range(int(rl())):
		s = rl().strip()
		n = len1(s)
		m = n // 2
		wl(str1(m * (n - m)) + '\n')


main()
