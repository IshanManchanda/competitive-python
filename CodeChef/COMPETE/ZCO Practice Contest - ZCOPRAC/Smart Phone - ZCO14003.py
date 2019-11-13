# https://www.codechef.com/ZCOPRAC/problems/ZCO14003
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	a = []
	n = int(rl())
	for i in range(n):
		a.append(int(rl()))
	a.sort(reverse=True)

	stdout.write(str(max(x * (i + 1) for i, x in enumerate(a))))


main()
