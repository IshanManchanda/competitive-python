def wood(h, r, l, t):
	s = 0
	for i in range(len(h)):
		st = h[i] + r[i] * t
		if st >= l:
			s += st
	return s


def bs(h, r, w, l, left, right):
	if right < left:
		return -1
	if right == left:
		return left if wood(h, r, l, left) >= w else -1
	mid = (left + right) // 2

	if wood(h, r, l, mid) < w:
		return bs(h, r, w, l, mid + 1, right)
	return bs(h, r, w, l, left, mid)


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	h, r = [], []
	ha, ra = h.append, r.append
	n, w, l = map(int1, rl().strip().split())
	for _ in range(n):
		t = rl().strip().split()
		ha(int1(t[0]))
		ra(int1(t[1]))

	if wood(h, r, l, 0) >= w:
		wl("0")
		return

	right = 1
	while wood(h, r, l, right) < w:
		right *= 2

	left = right // 2
	wl(str(bs(h, r, w, l, left, right)))


main()
