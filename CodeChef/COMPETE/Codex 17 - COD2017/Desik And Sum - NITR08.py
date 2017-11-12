def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	map1 = map
	str1 = str

	T = int1(rl())
	for i in xrange(T):
		L, R = map1(int1, rl().split())
		if L % 6 != 0:
			L += (6 - (L % 6))
		R -= R % 6
		L = L / 6
		R = R / 6
		stdout.write(str1((R - L + 1) * (6 * L + (R - L) * 3)) + "\n")


main()
