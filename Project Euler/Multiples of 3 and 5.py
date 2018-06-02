def main():
	n = 0
	for i in range(0, 1000, 3):
		n += i
	for i in range(0, 1000, 5):
		n += i
	for i in range(0, 1000, 15):
		n -= i

	print(n)


main()
