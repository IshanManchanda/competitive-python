from sys import stdin, stdout


def main():
	N = int(stdin.readline())
	b = []
	for i in range(N):
		b.append(int(stdin.readline()))

	stdout.write(str(b))


if __name__ == "__main__":
	main()
