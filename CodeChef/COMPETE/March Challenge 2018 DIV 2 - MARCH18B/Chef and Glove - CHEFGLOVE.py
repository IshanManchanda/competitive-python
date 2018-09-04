def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	t = int1(rl())
	for i in range(t):
		n = int1(rl())
		a1 = [int1(x) for x in rl().split()]
		a2 = [int1(x) for x in rl().split()]
		f = b = 1
		o = {
			"11": "both\n",
			"10": "front\n",
			"01": "back\n",
			"00": "none\n",
		}

		for j in range(n):
			if a2[j] < a1[j]:
				f = 0

			if a2[n - j - 1] < a1[j]:
				b = 0
		wl(o[str1(f) + str1(b)])


main()
