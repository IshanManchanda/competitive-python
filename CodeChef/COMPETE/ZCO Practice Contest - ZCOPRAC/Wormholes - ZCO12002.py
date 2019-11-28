# https://www.codechef.com/ZCOPRAC/problems/ZCO12002


def main():
	from sys import stdin, stdout
	from bisect import bisect_left
	rl = stdin.readline

	n, nv, nw = (int(x) for x in rl().split())
	c = [[int(x) for x in rl().split()] for _ in range(n)]
	vs = [int(x) for x in rl().split()]
	ws = [int(x) for x in rl().split()]

	c.sort()
	vs.sort()
	ws.sort()
	s = [x[0] for x in c]
	t = 1e7

	for v in vs:
		i = bisect_left(s, v)
		for j in range(i, n):
			if c[j][0] - v >= t:
				break
			k = bisect_left(ws, c[j][1])
			if k != nw:
				t = min(t, ws[k] - v)

	stdout.write(str(t + 1))


main()
