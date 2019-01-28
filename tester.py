def main():
	from random import randint as r

	n = r(1, 1e2)
	k = r(0, n // 2)
	a = [str(n), str(k)]
	for i in range(2 * n):
		a.append(str(r(0, 1e3)))

	print(" ".join(a))


main()
