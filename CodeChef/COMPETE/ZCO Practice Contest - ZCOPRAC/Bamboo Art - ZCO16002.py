# https://www.codechef.com/ZCOPRAC/problems/ZCO16002
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	# We want to find the maximum length of an AP formed by given lengths.

	# Naive solution picks every pair of elements, O(n^2)
	# and checks the array for other potential members. O(n)

	# Instead, we can use DP.
	# Notice that an AP is characterised by its last element and the difference
	# i.e, AP(index, difference)

	# For each element i, we can check all elements smaller than it.
	# If a[i] - a[j] is d,
	# the length of an AP(i, d) is 1 + length of AP(j, d)

	inp = [int(x) for x in rl().split()]
	n, a = inp[0], inp[1:]

	a.sort()
	dp = [[1] * (a[-1] - a[0]) for _ in range(n)]

	for i, x in enumerate(a):
		for j, y in enumerate(a[:i]):
			dp[i][x - y - 1] = 1 + dp[j][x - y - 1]

	stdout.write(str(max(max(x) for x in dp)))


main()
