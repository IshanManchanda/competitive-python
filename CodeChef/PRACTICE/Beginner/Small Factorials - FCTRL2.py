def main():
	from sys import stdin, stdout
	rl = stdin.readline
	pl = stdout.write
	int1 = int
	str1 = str
	for i in xrange(int1(rl())):
		n = int1(rl())
		a = 1
		for j in xrange(n):
			a *= n
			n -= 1
		pl(str1(a)+"\n")


main()
