def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	map1 = map
	range1 = range
	min1 = min
	max1 = max

	t = int1(rl())
	for _ in range1(t):
		n, q = map1(int1, rl().split())
		a = {}
		for _ in range1(3 * n):
			person = rl().split()
			if int1(person[0]) in a:
				a[int1(person[0])].append((person[1], person[2]))
			else:
				a[int1(person[0])] = [(person[1], person[2])]
		for _ in range1(q):
			team, seat = map1(int1, rl().split())
			ct = a[team]

			if seat == 1:
				wl((ct[0][0] if ct[0][1] == 'Y' else ct[1][0] if ct[1][
					                                                 1] == 'Y'
				else
				ct[2][0]) + '\n')
			elif seat == 2:
				wl((
					   min1(ct[0][0], ct[1][0]) if ct[2][1] == 'Y' else
					   min1(ct[1][0], ct[2][0]) if ct[0][1] == 'Y' else
					   min1(ct[2][0], ct[0][0])
				   ) + '\n')
			else:
				wl((
					   max1(ct[0][0], ct[1][0]) if ct[2][1] == 'Y' else
					   max1(ct[1][0], ct[2][0]) if ct[0][1] == 'Y' else
					   max1(ct[2][0], ct[0][0])
				   ) + '\n')


main()
