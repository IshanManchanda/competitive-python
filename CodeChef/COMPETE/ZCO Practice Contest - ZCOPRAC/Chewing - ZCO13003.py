# https://www.codechef.com/ZCOPRAC/problems/ZCO13003
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n, k = (int(x) for x in rl().split())
	a = [int(x) for x in rl().split()]

	a.sort()
	for i, x in enumerate(a):
		if x > k:
			del a[i:]
			break

	i = s = 0
	j = n - 1
	while i < j:
		while i < j and a[i] + a[j] >= k:
			j -= 1
		s += j - i
		i += 1

	stdout.write(str(s))


main()
