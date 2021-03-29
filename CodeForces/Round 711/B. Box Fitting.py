def main():
	from sys import stdin, stdout
	from collections import Counter
	rl = stdin.readline
	wl = stdout.write

	for _ in range(int(rl())):
		n, w = map(int, rl().split())
		a = Counter(int(x) for x in rl().split())
		a = dict(a.most_common())
		keys = sorted(a.keys(), reverse=True)
		h = -1
		while True:
			cur = 0
			h += 1
			for key in keys:
				while a[key] != 0 and cur + key <= w:
					cur += key
					a[key] -= 1

			if cur == 0:
				break

		wl(str(h) + '\n')


main()
