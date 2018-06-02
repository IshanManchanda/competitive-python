def empty():
	return [0, 0, 0, 0, 0, 0, 0, 0, 0]


def main():
	t = int(input())
	d = []
	for i in range(t):
		d.append(input())

	for date in d:
		md = date[0] + date[1] + date[3] + date[4]
		yy = date[-4:]

		mdl, yyl = empty(), empty()
		for c in md:
			mdl[int(c) - 1] += 1

		for c in yy:
			yyl[int(c) - 1] += 1

		if mdl == yyl:
			print("Lucky Watson")
		else:
			print("Unlucky Watson")


if __name__ == '__main__':
	main()
