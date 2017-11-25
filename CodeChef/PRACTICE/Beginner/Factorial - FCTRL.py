def main():
	from sys import stdin, stdout
	rl = stdin.readline
	pl = stdout.write
	int1 = int
	str1 = str
	xr1 = xrange
	sum1 = sum
	for _ in xr1(int1(rl())):
		n = int1(rl())
		c = sum1(n/5**i for i in xr1(1, 13))
		pl(str1(c)+"\n")


main()
