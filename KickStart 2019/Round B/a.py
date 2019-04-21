def main():
	from sys import stdin, stdout

	rl = stdin.readline
	wl = stdout.write
	int1 = int
	temp = {x: 0 for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

	t = int1(rl())
	for tn in range(1, t + 1):
		n, q = map(int1, rl().split())
		s = rl().strip()
		ans = 0
		arr = [temp.copy(), temp.copy()]
		arr[1][s[0]] += 1

		for i in range(1, n):
			arr.append(arr[i].copy())
			arr[i + 1][s[i]] += 1

		for i in range(q):
			l, r = map(int1, rl().split())

			letts = [arr[r][x] - arr[l - 1][x] for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
			odd_used = False
			for let in letts:
				if let % 2 == 1:
					if odd_used:
						break
					odd_used = True
			else:
				# No break, so yes!
				ans += 1

		wl('Case #%d: %d\n' % (tn, ans))


main()
