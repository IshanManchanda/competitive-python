dp = [
	[1, [
		[]
	]],
	[1, [
		[1]
	]],
	[2, [
		[1, 1], [2]
	]]
] + [
	[-1, [

	]]
] * 3


def milk(a):
	if a < 0:
		return 0, []
	if dp[a][0] != -1:
		return dp[a]

	# if a >= 160:
	# 	b = milk(a - 1) + milk(a - 2) + milk(a - 4) + milk(a - 16) + milk(a - 32) + milk(a - 160)
	# elif a >= 32:
	# 	b = milk(a - 1) + milk(a - 2) + milk(a - 4) + milk(a - 16) + milk(a - 32)
	# elif a >= 16:
	# 	b = milk(a - 1) + milk(a - 2) + milk(a - 4) + milk(a - 16)
	# elif a >= 4:
	# 	b = milk(a - 1) + milk(a - 2) + milk(a - 4)
	# elif a >= 2:
	# 	b = milk(a - 1) + milk(a - 2)
	# else:
	# 	b = milk(a - 1)

	b, x = milk(a - 1)
	if a >= 2:
		beta, xeta = milk(a - 2)
		for i in xeta:
			if i not in x:
				x += [i]
				b += 1
	dp[a][0] = b
	return b


def main():
	from sys import stdin, stdout, setswitchinterval as ssi
	ssi(999999999)
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	c = {'CN': 160, 'PL': 32, 'G': 16, 'Q': 4, 'PN': 2, 'CP': 1}

	try:
		while True:
			a = int1(rl())
			a *= c[rl().strip()]
			wl(str1(milk(a)) + '\n')
	except ValueError or EOFError or KeyError:
		pass


main()
