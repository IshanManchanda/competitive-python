# https://www.codechef.com/PCJ2018/problems/PCJ18C
def main():
	from sys import stdin, stdout
	from math import gcd as g
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str
	map1 = map

	for _ in range(int1(rl())):
		n, a, k = map1(int1, rl().split())
		if k == 1:
			wl(str1(a) + " 1\n")
			continue
		p1 = ((n * (360 - (2 * a))) - 720) * (k - 1)
		p2 = n * (n - 1)
		gpp = g(p1, p2)
		if gpp == p2:
			kd = int1(p1 / p2)
			wl(str1(kd + a) + " 1\n")
		else:
			p3 = int1(p1 / gpp)
			p4 = int1(p2 / gpp)
			wl(str1(p3 + a * p4) + " " + str1(p4) + "\n")


main()
