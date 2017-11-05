next_city = [
	(2, 0, 7),
	(5, 4, 10),
	(7, 2, 0),
	(9, 7, 2),
	(4, 10, 5),
	(1, 6, 6),
	(6, 5, 1),
	(0, 3, 8),
	(3, 8, 11),
	(11, 9, 3),
	(10, 1, 4),
	(8, 11, 9)
]

cycle = [0, 1, 2, 2, 2, 0, 1]


def main(journeys, current_city):
	j = len(cycle)

	for i in range(journeys):
		j = j % len(cycle)
		current_city = next_city[current_city][cycle[j]]
		j += 1

	print(current_city)


if __name__ == '__main__':
	main(103, 2)
	main(103, 6)
	main(159, 0)
	main(159, 10)
	main(207, 4)
	main(207, 7)
