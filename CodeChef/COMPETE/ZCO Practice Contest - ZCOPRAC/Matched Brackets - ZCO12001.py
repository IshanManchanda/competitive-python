# https://www.codechef.com/ZCOPRAC/problems/ZCO12001
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n = int(rl())
	bs = [int(x) for x in rl().split()]

	o = 0  # Currently open brackets
	md = 0  # Max depth
	mdp = 0  # Max depth position
	cs = 0  # Current symbols
	ms = 0  # Max symbols
	csp = 0  # Current symbols start position
	msp = 0  # Max symbols start position

	for i, b in enumerate(bs):
		if b == 1:
			if o == 0:
				cs = 0
				csp = i + 1
			cs += 1
			o += 1

		else:
			if o > md:
				md = o
				mdp = i

			cs += 1
			o -= 1

			if o == 0:
				if cs > ms:
					ms = cs
					msp = csp

	stdout.write('%d %d %d %d' % (md, mdp, ms, msp))


main()
