import math


def is_square(n):
	if n <= 0:
		return False
	sqrt = math.sqrt(n)
	if (sqrt % 1) == 0:
		return True
	return False
