def main():
	from sys import stdin, stdout
	rl = stdin.readline
	pl = stdout.write
	int1 = int
	str1 = str
	xr = range
	sum1 = sum
	arr = [5]
	for k in xr(1, 13):
		arr[k] = arr[k - 1] * 5
	for _ in xr(int1(rl())):
		n = int1(rl())
		c = sum1(n / i for i in arr)
		pl(str1(c) + "\n")


main()
