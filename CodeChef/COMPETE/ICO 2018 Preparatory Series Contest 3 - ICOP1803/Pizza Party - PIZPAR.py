def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	C = []
	a = C.append
	i = 0

	M, N = map(int1, rl().split())
	array = sorted([int1(x) for x in rl().split()], reverse=True)

	while N:
		if N >= array[i]:
			N -= array[i]
			a(array[i])
		else:
			a(N)
			N = 0
		i += 1
	C.extend([0] * len(array[i:]))

	stdout.write(str(sum([(x ** 2 + x + 2) / 2 for x in C])))


main()
