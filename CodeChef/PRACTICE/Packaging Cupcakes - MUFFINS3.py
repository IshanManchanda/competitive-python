def main():
	from sys import stdin, stdout
	rl = stdin.readline
	pl = stdout.write
	int1 = int
	str1 = str

	for _ in range(int1(rl())):
		pl(str1((int1(rl()) / 2) + 1) + '\n')


main()
