def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int

	number, Q = map(int1, rl().split())
	A = [int1(x) for x in rl().split()]
	V = []
	Vd = []
	D = []
	Dt = []
	for i in range(number-1):
		V.append(tuple(x for x in rl().split()))
	for i in range(Q-1):
		D.append(int1(rl()))




main()
