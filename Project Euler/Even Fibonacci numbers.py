def main():
	arr = [1, 2]
	append = arr.append
	n = 2

	while arr[n - 1] < 4000000:
		append(arr[n - 1] + arr[n - 2])
		n += 1

	print(sum(x for x in arr if x % 2 == 0))


main()
