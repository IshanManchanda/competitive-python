def main():
	n = [1, 2]
	a = n.append
	l = 2
	while n[l - 1] < 4000000:
		a(n[l - 1] + n[l - 2])
		l += 1

	print(sum(x for x in n if x % 2 == 0))


main()
