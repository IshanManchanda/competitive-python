def rem4(a, b=0):
	sa, sb = str(a), str(b)
	if '4' not in sa and '4' not in sb:
		return a, b

	a, b = max(a, b), min(a, b)
	sa, sb = str(a), str(b)
	if '4' in sa:
		la = len(sa)

		aind = sa.find('4')
		r = a % 10 ** (la - aind - 1)
		x = a - r - 1
		y = b + r + 1
		return rem4(x, y)

	lb = len(sb)
	bind = sb.find('4')
	p = 10 ** (lb - bind - 1)
	r = p - (b % p)
	x = b + r + 1
	y = a - r - 1
	return rem4(x, y)


def main():
	from sys import stdin, stdout, setrecursionlimit
	setrecursionlimit(100000)
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	t = int1(rl())
	for tn in range(1, t + 1):
		n = int1(rl().strip())
		ans = rem4(n)
		wl('Case #%d: %d %d\n' % (tn, ans[0], ans[1]))


main()
