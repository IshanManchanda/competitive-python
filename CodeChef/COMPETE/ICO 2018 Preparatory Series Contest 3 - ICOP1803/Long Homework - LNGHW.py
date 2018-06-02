def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int

	N, Q, M = map(int1, rl().split())
	A = map(int1, rl().split())
	As = sorted(A)
	i = []
	a = i.append
	R = []
	b = R.append
	for j in range(Q):
		t = rl().split()
		a(int1(t[0]))
		b(int1(t[1]))

	m = [x % M for x in As]

	for k in range(Q):
		try:
			index = [x for x in range(len(m) - 1) if m[x] == R[k]][i[k] - 1]
			stdout.write(str(A.index(As[index]) + 1) + "\n")
		except Exception:
			stdout.write("-1\n")


main()
