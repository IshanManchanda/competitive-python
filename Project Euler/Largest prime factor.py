def main():
	m = n = 0
	for i in range(2, int(600851475143 ** 0.6)):
		if 600851475143 % i == 0:
			m = i

	for i in range(2, int(m ** 0.6)):
		if m % i == 0:
			n = i
	print(n)


# def sieve(limit):
# 	a = [True] * limit
# 	a[0] = a[1] = False
#
# 	for (i, isprime) in enumerate(a):
# 		if isprime:
# 			yield i
# 			for n in range(i * i, limit, i):
# 				a[n] = False


main()
