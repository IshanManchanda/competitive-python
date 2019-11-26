# https://www.codechef.com/JUNE18B/problems/NAICHEF
def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	t = int1(rl())

	for _ in range(t):
		n, a, b = [int1(x) for x in rl().split()]
		c = list(map(int1, rl().split()))
		wl(str1((c.count(a) * c.count(b)) / (n * n)) + '\n')


main()
