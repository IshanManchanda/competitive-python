def main():
	from sys import stdin, stdout
	rl = stdin.readline
	pl = stdout.write
	int1 = int
	str1 = str
	map1 = map

	for _ in xrange(int1(rl())):
		a, b = map1(int1, rl().split())
		pl(str1(a % b) + '\n')


main()
