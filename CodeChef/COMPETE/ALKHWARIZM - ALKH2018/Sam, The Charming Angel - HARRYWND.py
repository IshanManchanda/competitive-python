def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	n, k = [int1(x) for x in rl().split()]
	a = [int1(x) for x in rl().split()]
	b = [[0, 0]] + [[-1, -1] for _ in range(n)]
	for i in range(len(b)):
		for j in a:
			if j <= i:
				l = b[i - j]
				if l[0] != -1:
					if b[i][0] == -1 or l[0] + 1 < b[i][0]:
						b[i][0] = l[0] + 1
					if b[i][1] == -1 or l[1] + 1 > b[i][1]:
						b[i][1] = l[1] + 1
	wl("%s %s\n" % (str1(b[n][0]), str1(b[n][1])))


main()
