# https://www.codechef.com/ZCOPRAC/problems/ZCO15002
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n, k = (int(x) for x in rl().split())
	a = [int(x) for x in rl().split()]

	a.sort()
	i = j = s = 0
	while j < n and i < n:
		while j < n and a[j] - a[i] < k:
			j += 1
		s += n - j
		i += 1

	stdout.write(str(s))


main()
