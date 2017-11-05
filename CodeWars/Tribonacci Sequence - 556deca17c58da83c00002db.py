def tribonacci(signature, n):
	if n < 3:
		if n == 0:
			return []
		if n == 1:
			return [signature[0]]
		if n == 2:
			return signature[:2]
	a = signature
	for i in range(3, n):
		a.append(a[i - 3] + a[i - 2] + a[i - 1])
	return a
