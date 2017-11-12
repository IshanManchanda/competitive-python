def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int

	N, Q = map(int1, rl().split())
	A = [int1(x) for x in rl().split()]
	V = []
	Vd = []
	D = []
	Dt = []
	for i in xrange(N-1):
		V.append(tuple(x for x in rl().split()))
	for i in xrange(Q-1):
		D.append(int1(rl()))




main()
