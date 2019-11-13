def main():
	from sys import stdin, stdout
	rl = stdin.readline
	int1 = int
	map1 = map
	str1 = str

	tests = int1(rl())
	for i in range(tests):
		left, right = map1(int1, rl().split())
		if left % 6 != 0:
			left += (6 - (left % 6))
		right -= right % 6
		left = left / 6
		right = right / 6
		stdout.write(
			str1((right - left + 1) * (6 * left + (right - left) * 3)) + "\n")


main()
