def main():
	from sys import stdin, stdout
	x, y = map(float, stdin.readline().split())
	if x % 5 == 0 and y > x + 0.5:
		y -= x + 0.5
	s = str(int(y * 100))
	stdout.write(s[:-2] + "." + s[-2:])


main()
