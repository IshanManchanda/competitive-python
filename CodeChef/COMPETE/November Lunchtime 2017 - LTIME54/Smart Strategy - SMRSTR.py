def main():
	from sys import stdin, stdout
	rl = stdin.readline
	pl = stdout.write
	int1 = int
	str1 = str
	list1 = list
	map1 = map
	range1 = range

	for _ in range1(int1(rl())):
		_, _ = map1(int1, rl().split())
		D = list1(map1(int1, rl().split()))
		Qs = list1(map1(int1, rl().split()))
		r = []
		a = r.append
		for i in Qs:
			for j in D:
				i /= j
			a(i)
		pl(" ".join(str1(x) for x in r)+"\n")


main()
