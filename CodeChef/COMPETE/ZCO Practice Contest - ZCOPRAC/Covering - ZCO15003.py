# https://www.codechef.com/ZCOPRAC/problems/ZCO15003
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	n = int(rl())
	a = [[int(x) for x in rl().split()] for _ in range(n)]

	a.sort()
	i = s = 0
	while i < n:
		end = a[i][1]
		while i < n and end >= a[i][0]:
			i += 1
			end = min(end, a[i][1]) if i < n else end
		s += 1

	stdout.write(str(s))


main()
