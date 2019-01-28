def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	len1 = len
	range1 = range
	str1 = str

	for _ in range1(int1(rl())):
		a = t = n = rl().strip()
		for _ in range1(len1(n) - 1):
			t = t[1:] + t[0]
			a += t
		res = 0
		for i in range1(len1(a)):
			res = (res * 10 + int1(a[i])) % 1000000007
		wl(str1(res) + '\n')


main()
