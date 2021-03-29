from functools import lru_cache


@lru_cache(maxsize=None)
def num(decay, ahead, behind):
	if decay == 1:
		return 0

	if decay == 2:
		return 1

	if decay == 3:
		return 1 + behind

	if behind == 0:
		return 1

	a = 1
	for i in range(1, behind + 1):
		a += num(decay - 1, behind - i, ahead + i)
		a %= 1000000007
	return a


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write

	for _ in range(int(rl())):
		n, k = map(int, rl().split())
		a = 1
		for i in range(n):
			a += num(k, n - i - 1, i)
			a %= 1000000007
		wl(str(a) + '\n')


main()
