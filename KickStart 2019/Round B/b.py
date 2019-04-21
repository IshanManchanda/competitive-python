def main():
	from sys import stdin, stdout
	from collections import defaultdict

	rl = stdin.readline
	wl = stdout.write
	int1 = int
	range1 = range
	sum1 = sum
	max1 = max
	map1 = map
	list1 = list
	d = defaultdict(int)

	t = int1(rl())
	for tn in range1(1, t + 1):
		n, s = map1(int1, rl().split())
		a = list1(map1(int1, rl().split()))
		ans = -1
		arr = [d.copy(), d.copy()]
		arr[1][a[0]] += 1

		for i in range1(1, n):
			arr.append(arr[i].copy())
			arr[i + 1][a[i]] += 1

		for i in range1(1, n + 1):
			for j in range1(i):
				nums = [arr[i][x] - arr[j][x] for x in range1(1001)]
				total = sum1(x if x <= s else 0 for x in nums)
				ans = max1(ans, total)

		wl('Case #%d: %d\n' % (tn, ans))


main()
