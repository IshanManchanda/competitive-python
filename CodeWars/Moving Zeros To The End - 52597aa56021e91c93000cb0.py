def move_zeros(array):
	a = []
	n = 0
	for i in array:
		if i != 0 or not (i.isinstance(0) or i.isinstance(0)):
			a.append(i)
		else:
			n += 1
	return a + ([0] * n)
