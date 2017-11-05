from sys import stdin, stdout


def main():
	N, H = stdin.readline().split()
	N = int(N)
	H = int(H)
	p = b = 0
	h = [int(x) for x in stdin.readline().split()]
	s = [int(x) for x in stdin.readline().split()]

	for i in s:
		if i == "1":
			p = max([p-1, 0])
			continue
		if i == "2":
			p = min([p+1, N])
			continue
		if i == "3":
			if b or h[p] == 0:
				continue
			b = 1
			h[p] -= 1
			continue
		if i == "4":
			if (not b) or h[p] == H:
				continue
			b = 0
			h[p] += 1
		if i == "0":
			break

	stdout.write(str(" ".join(str(x) for x in h)))


if __name__ == "__main__":
	main()
