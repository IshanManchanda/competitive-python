def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	str1 = str
	max1 = max
	min1 = min

	N, H = map(int1, rl().split())
	p = b = 0
	h = [int1(x) for x in rl().split()]
	s = [int1(x) for x in rl().split()]

	for i in s:
		if i == 1:
			p = max1(p-1, 0)
		elif i == 2:
			p = min1(p+1, N-1)
		elif i == 3:
			if b or (h[p] == 0):
				continue
			b = 1
			h[p] -= 1
		elif i == 4:
			if (not b) or (h[p] == H):
				continue
			b = 0
			h[p] += 1
		else:
			break

	stdout.write(" ".join(str1(x) for x in h))


main()
