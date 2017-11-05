def find_nb(m):
	sum = 0
	i = 1

	while True:
		sum += i ** 3
		if sum > m:
			return -1
		if sum == m:
			return i
		i += 1
