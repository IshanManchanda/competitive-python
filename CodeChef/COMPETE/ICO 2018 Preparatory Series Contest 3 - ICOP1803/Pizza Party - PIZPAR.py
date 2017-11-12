def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	C = []
	a = C.append
	i = 0

	M, N = map(int1, rl().split())
	A = sorted([int1(x) for x in rl().split()], reverse=True)

	while N:
		if N >= A[i]:
			N -= A[i]
			a(A[i])
		else:
			a(N)
			N = 0
		i += 1
	C.extend([0] * len(A[i:]))
	S = sum([(x**2 + x + 2) / 2 for x in C])

	stdout.write(str(S))


main()
