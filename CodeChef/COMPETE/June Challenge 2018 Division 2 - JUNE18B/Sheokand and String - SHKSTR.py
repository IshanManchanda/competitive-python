def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	n = int1(rl())
	s = []
	for _ in range(n):
		s.append(rl().strip())
	q = int1(rl())
	for _ in range(q):
		a = rl().split()
		m = 0
		ms = ''
		for i in range(int1(a[0])):
			j = 0
			while a[1][j] == s[i][j]:
				j += 1
				if j >= len(a[1]) or j >= len(s[i]):
					break
			if j > m:
				m = j
				ms = s[i]
			elif j == m:
				ms = min([ms, s[i]])
		wl(ms + '\n')
		if q == 1:
			return


main()
