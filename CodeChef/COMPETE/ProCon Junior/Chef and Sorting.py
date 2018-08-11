def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	len1 = len
	list1 = list
	sorted1 = sorted
	range1 = range
	next1 = next
	enum = enumerate
	rev = reversed
	map1 = map

	for _ in range(int1(rl())):
		n = int1(rl())
		a = list1(map1(int1, rl().split()))
		s = sorted1(a)
		for i in range1(len1(s)):
			if s[i] != a[i]:
				ind = len1(a) - next1(i for i, v in enum(rev(a), 1) if v == s[i])
				a1 = a[i:ind]
				s1 = sorted1(a1)
				for j in s1:
					a = a[:i] + [x for x in a[i:ind] if x != j] + a[ind:] + [j]


main()
