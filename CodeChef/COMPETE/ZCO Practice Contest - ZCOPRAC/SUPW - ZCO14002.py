tab = {}


def find_min(t, i):
	if i in tab:
		return tab[i]
	if len(t[i:]) < 3:
		return 0
	if len(t[i:]) == 3:
		return min(t)
	tab[i] = min(t[i] + find_min(t, i + 1), t[i + 1] + find_min(t, i + 2), t[i + 2] + find_min(t, i + 3))
	return tab[i]


def main():
	from sys import stdin, stdout, setrecursionlimit
	setrecursionlimit(10 ** 6)
	rl = stdin.readline
	wl = stdout.write
	int1, str1, range1, = int, str, range

	rl()
	t = list(map(int1, rl().split()))
	wl(str(find_min(t, 0)))


main()
