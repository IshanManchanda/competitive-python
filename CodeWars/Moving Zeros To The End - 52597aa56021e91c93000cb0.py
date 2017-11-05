def move_zeros(array):
	a = []
	n = 0
	for i in array:
		if i != 0 or (type(i) != type(0) and type(i) != type(0.0)):
			a.append(i)
		else:
			n += 1
	return a + ([0] * n)
