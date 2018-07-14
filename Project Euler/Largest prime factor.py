def main():
	k = 600851475143
	m = n = 0
	a = []
	for i in range(2, int(k ** 0.5) + 1):
		if k % i == 0:
			for j in range(2, int(i ** 0.5) + 1):
				if i % j == 0:
					pass
			a += i
			a += k / i

	for i in range(2, int(m ** 0.5) + 1):
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
