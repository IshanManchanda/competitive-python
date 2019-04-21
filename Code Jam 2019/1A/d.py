def main():
	from sys import stdin, stdout

	rl = stdin.readline
	wl = stdout.write
	int1 = int
	letts = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	t = int1(rl())
	for tn in range(1, t + 1):
		n = int1(rl())
		words = {l: [] for l in letts}

		for _ in range(n):
			a = rl().strip()[::-1]
			words[a[0]].append(a[1:])

		for key in list(words.keys()):
			if len(words[key]) < 2:
				del words[key]

		if len(words) == 3:
			wl("Case #%d: %d\n" % (tn, 6))
			continue

		elif len(words) == 2:
			k = ''
			for key, value in words.items():
				if len(value) == 4:
					k = key
					break
			else:
				wl("Case #%d: %d\n" % (tn, 4))
				continue

			s = 4
			if len(words[k]) == 4:
				if (
					words[k][0][0] == words[k][1][0] or
					words[k][0][0] == words[k][2][0] or
					words[k][0][0] == words[k][3][0] or
					words[k][1][0] == words[k][2][0] or
					words[k][1][0] == words[k][3][0] or
					words[k][2][0] == words[k][3][0]):
					s += 2
			wl("Case #%d: %d\n" % (tn, s))

		elif len(words) == 1:
			k = ''
			for key, value in words.items():
				k = key
				if len(value) < 4:
					wl("Case #%d: %d\n" % (tn, 2))
					continue

			if len(words[k]) == 4:
				if (
					words[k][0][0] == words[k][1][0] or
					words[k][0][0] == words[k][2][0] or
					words[k][0][0] == words[k][3][0] or
					words[k][1][0] == words[k][2][0] or
					words[k][1][0] == words[k][3][0] or
					words[k][2][0] == words[k][3][0]):
					wl("Case #%d: %d\n" % (tn, 4))
				else:
					wl("Case #%d: %d\n" % (tn, 2))
				continue
			elif len(words[k]) == 5:
				if (
					words[k][0][0] == words[k][1][0] or
					words[k][0][0] == words[k][2][0] or
					words[k][0][0] == words[k][3][0] or
					words[k][0][0] == words[k][4][0] or
					words[k][1][0] == words[k][2][0] or
					words[k][1][0] == words[k][3][0] or
					words[k][1][0] == words[k][4][0] or
					words[k][2][0] == words[k][3][0] or
					words[k][2][0] == words[k][4][0] or
					words[k][3][0] == words[k][4][0]):
					wl("Case #%d: %d\n" % (tn, 4))
				else:
					wl("Case #%d: %d\n" % (tn, 2))
				continue

			new_words = {l: [] for l in letts}
			for word in words[k]:
				if len(word) > 0:
					new_words[word[0]].append(word[1:])
			words = new_words

			for key in list(words.keys()):
				if len(words[key]) < 2:
					del words[key]

			if len(words) == 3:
				wl("Case #%d: %d\n" % (tn, 6))
				continue

			elif len(words) == 2:
				k = ''
				for key, value in words.items():
					if len(value) == 4:
						k = key
						break
				else:
					wl("Case #%d: %d\n" % (tn, 4))
					continue

				s = 4
				if len(words[k]) == 4:
					if (
						words[k][0][0] == words[k][1][0] or
						words[k][0][0] == words[k][2][0] or
						words[k][0][0] == words[k][3][0] or
						words[k][1][0] == words[k][2][0] or
						words[k][1][0] == words[k][3][0] or
						words[k][2][0] == words[k][3][0]):
						s += 2
				wl("Case #%d: %d\n" % (tn, s))

			elif len(words) == 1:
				k = ''
				for key, value in words.items():
					k = key
					if len(value) < 4:
						wl("Case #%d: %d\n" % (tn, 2))
						continue

				if len(words[k]) == 4:
					if (
						words[k][0][0] == words[k][1][0] or
						words[k][0][0] == words[k][2][0] or
						words[k][0][0] == words[k][3][0] or
						words[k][1][0] == words[k][2][0] or
						words[k][1][0] == words[k][3][0] or
						words[k][2][0] == words[k][3][0]):
						wl("Case #%d: %d\n" % (tn, 4))
					else:
						wl("Case #%d: %d\n" % (tn, 2))
					continue
				elif len(words[k]) == 5:
					if (
						words[k][0][0] == words[k][1][0] or
						words[k][0][0] == words[k][2][0] or
						words[k][0][0] == words[k][3][0] or
						words[k][0][0] == words[k][4][0] or
						words[k][1][0] == words[k][2][0] or
						words[k][1][0] == words[k][3][0] or
						words[k][1][0] == words[k][4][0] or
						words[k][2][0] == words[k][3][0] or
						words[k][2][0] == words[k][4][0] or
						words[k][3][0] == words[k][4][0]):
						wl("Case #%d: %d\n" % (tn, 4))
					else:
						wl("Case #%d: %d\n" % (tn, 2))
					continue

				new_words = {l: [] for l in letts}
				for word in words[k]:
					if len(word) > 0:
						new_words[word[0]].append(word[1:])
				words = new_words

				for key in list(words.keys()):
					if len(words[key]) < 2:
						del words[key]

				if len(words) == 3:
					wl("Case #%d: %d\n" % (tn, 6))
					continue

				elif len(words) == 2:
					k = ''
					for key, value in words.items():
						if len(value) == 4:
							k = key
							break
					else:
						wl("Case #%d: %d\n" % (tn, 4))
						continue

					s = 4
					if len(words[k]) == 4:
						if (
							words[k][0][0] == words[k][1][0] or
							words[k][0][0] == words[k][2][0] or
							words[k][0][0] == words[k][3][0] or
							words[k][1][0] == words[k][2][0] or
							words[k][1][0] == words[k][3][0] or
							words[k][2][0] == words[k][3][0]):
							s += 2
					wl("Case #%d: %d\n" % (tn, s))

				elif len(words) == 1:
					k = ''
					for key, value in words.items():
						k = key
						if len(value) < 4:
							wl("Case #%d: %d\n" % (tn, 2))
							continue

					if len(words[k]) == 4:
						if (
							words[k][0][0] == words[k][1][0] or
							words[k][0][0] == words[k][2][0] or
							words[k][0][0] == words[k][3][0] or
							words[k][1][0] == words[k][2][0] or
							words[k][1][0] == words[k][3][0] or
							words[k][2][0] == words[k][3][0]):
							wl("Case #%d: %d\n" % (tn, 4))
						else:
							wl("Case #%d: %d\n" % (tn, 2))
						continue
					elif len(words[k]) == 5:
						if (
							words[k][0][0] == words[k][1][0] or
							words[k][0][0] == words[k][2][0] or
							words[k][0][0] == words[k][3][0] or
							words[k][0][0] == words[k][4][0] or
							words[k][1][0] == words[k][2][0] or
							words[k][1][0] == words[k][3][0] or
							words[k][1][0] == words[k][4][0] or
							words[k][2][0] == words[k][3][0] or
							words[k][2][0] == words[k][4][0] or
							words[k][3][0] == words[k][4][0]):
							wl("Case #%d: %d\n" % (tn, 4))
						else:
							wl("Case #%d: %d\n" % (tn, 2))
						continue

					wl("Case #%d: %d\n" % (tn, 6))

		else:
			wl("Case #%d: %d\n" % (tn, -1))


main()
