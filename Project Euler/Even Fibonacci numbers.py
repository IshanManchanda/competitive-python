def main():
	n = [1, 2]
	a = n.append
	l = len
	while n[l(n) - 1] < 4000000:
		a(n[l(n) - 1] + n[l(n) - 2])

	print(sum(x for x in n if x % 2 == 0))


main()
