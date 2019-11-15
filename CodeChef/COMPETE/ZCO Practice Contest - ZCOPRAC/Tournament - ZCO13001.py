# https://www.codechef.com/ZCOPRAC/problems/ZCO13001
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n = int(rl())
	a = [int(x) for x in rl().split()]

	a.sort(reverse=True)
	stdout.write(str(sum(x * (n - 1 - 2 * i) for i, x in enumerate(a))))


main()
