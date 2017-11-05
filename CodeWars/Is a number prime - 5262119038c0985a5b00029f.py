def is_prime(num):
	if num < 2:
		return False
	for i in range(2, int(num ** 0.5) + 1):
		print(i)
		if num % i == 0:
			return False
	return True
