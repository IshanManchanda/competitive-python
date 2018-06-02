def find_nb(m):
	s = 0
	i = 1

	while True:
		s += i ** 3
		if s > m:
			return -1
		if s == m:
			return i
		i += 1
