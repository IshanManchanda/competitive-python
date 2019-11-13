def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	abs1 = abs
	range1 = range
	len1 = len

	for _ in range1(int1(rl())):
		a = {key: -1 for key in 'abcdefghijklmnopqrstuvwxyz'}
		b = {'abcdefghijklmnopqrstuvwxyz'[i]: 'abcdefghijklmnopqrstuvwxyz'[
			25 - i] for i in range(26)}
		s = rl().strip()
		l = len1(s) - 1
		for i in range1(l + 1):
			c = s[i]
			if a[c] == -1:
				a[c] = i
			if a[b[c]] != -1:
				wl(str1(abs1(a[b[c]] - a[c])) + '\n')
				break
			c = s[l - i]
			if a[c] == -1:
				a[c] = l - i
			if a[b[c]] != -1:
				wl(str1(abs1(a[b[c]] - a[c])) + '\n')
				break


main()
