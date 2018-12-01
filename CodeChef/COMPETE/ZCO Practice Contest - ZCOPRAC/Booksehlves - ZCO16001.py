def move(b1, b2, k):
	for _ in range(k):
		# Ideal case: b2 has the N-largest numbers.
		if b2[-1] >= b1[0]:
			return

		# Insert the largest number of b1 into b2
		v = b1.pop(0)
		i = 0
		while i < len(b2) and b2[i] > v:
			i += 1
		b2.insert(i, v)

		# Insert the smallest number of b2 into b1
		v = b2.pop(-1)
		i = len(b1) - 1
		while i > -1 and b1[i] < v:
			i -= 1
		b1.insert(i + 1, v)


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int

	inpt = rl().strip().split()
	n, k = map(int1, inpt[:2])
	b1 = sorted(map(int1, inpt[2:n + 2]), reverse=True)
	b2 = sorted(map(int1, inpt[n + 2:]), reverse=True)
	t1, t2 = b1.copy(), b2.copy()

	# Try moving all max to shelf 1 and then to shelf 2.
	move(b1, b2, k)
	move(t2, t1, k)
	wl(str(min(t1[0] + t2[0], b1[0] + b2[0])))


main()
