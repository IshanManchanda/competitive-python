# https://www.codechef.com/CMEL2018/problems/SINS
def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	str1 = str

	t = int1(rl())
	for i in range(t):
		x, y = [int1(x) for x in rl().split()]
		while x != y and x != 0 and y != 0:
			if x > y:
				a = x % y
				x = a if a != 0 else y
			else:
				a = y % x
				y = a if a != 0 else x
		wl(str1(x + y) + "\n")


main()
