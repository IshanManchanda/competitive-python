def productFib(prod):
	fibs = [0] * 10000
	fibs[1] = 1
	i = 1
	while True:
		fibs[i + 1] = fibs[i] + fibs[i - 1]
		if fibs[i + 1] * fibs[i] == prod:
			return [fibs[i], fibs[i + 1], True]
		if fibs[i + 1] * fibs[i] > prod:
			return [fibs[i], fibs[i + 1], False]
		i += 1
