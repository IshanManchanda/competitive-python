def tickets(people):
	bills_25 = 0
	bills_50 = 0

	for i in people:
		if i == 25:
			bills_25 += 1
			continue
		if i == 50:
			if bills_25 > 0:
				bills_25 -= 1
				bills_50 += 1
				continue
			return "NO"
		if i == 100:
			if bills_50 > 0 and bills_25 > 0:
				bills_50 -= 1
				bills_25 -= 1
				continue
			if bills_25 < 3:
				return "NO"
			bills_25 -= 3
	return "YES"
