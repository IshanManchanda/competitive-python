# https://www.codechef.com/ZCOPRAC/problems/ZCO16001
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

	inp = rl().strip().split()
	n, k = map(int, inp[:2])
	b1 = sorted(map(int, inp[2:n + 2]), reverse=True)
	b2 = sorted(map(int, inp[n + 2:]), reverse=True)
	t1, t2 = b1.copy(), b2.copy()

	# Try moving all max to shelf 1 and then to shelf 2.
	move(b1, b2, k)
	move(t2, t1, k)
	stdout.write(str(min(t1[0] + t2[0], b1[0] + b2[0])))


main()


# ALT: Iterative
def main2():
	from sys import stdin, stdout
	from bisect import insort
	rl = stdin.readline

	inp = [int(x) for x in rl().split()]
	n, k = inp[:2]
	s1, s2 = inp[2:n + 2], inp[n + 2:]
	s1.sort()
	s2.sort()

	for _ in range(k):
		insort(s1, s2[0])
		del s2[0]
		insort(s2, s1[-1])
		del s1[-1]
		if s2[0] >= s1[-1]:
			break

	s = s1[-1] + s2[-1]

	s2, s1 = inp[2:n + 2], inp[n + 2:]
	s1.sort()
	s2.sort()

	for _ in range(k):
		insort(s1, s2[0])
		del s2[0]
		insort(s2, s1[-1])
		del s1[-1]
		if s2[0] >= s1[-1]:
			break

	s = min(s, s1[-1] + s2[-1])
	stdout.write(str(s))
