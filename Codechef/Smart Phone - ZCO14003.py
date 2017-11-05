from sys import stdin, stdout


def main():
	N = int(stdin.readline())
	b = []
	ms = 0
	for i in range(N):
		b.append(int(stdin.readline()))

	for i in range(len(b)):
		s = 0
		for j in range(len(b)):
			if b[j] >= b[i]:
				s += b[i]
		if s > ms:
			ms = s

	stdout.write(str(ms))


if __name__ == "__main__":
	main()
