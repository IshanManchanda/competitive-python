def main():
	from sys import stdin, stdout
	rl = stdin.readline
	pl = stdout.write
	int1 = int
	str1 = str
	sum1 = sum
	map1 = map

	for _ in xrange(int1(rl())):
		pl(str1(sum1(map1(int1, rl().split())))+'\n')


main()
