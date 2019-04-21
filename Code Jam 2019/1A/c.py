letts = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def make_pairs(w):
	s = 0
	words = {l: [] for l in letts}
	used = []
	for word in w:
		if len(word) > 0:
			words[word[0]].append(word[1:])

	for key in list(words.keys()):
		if len(words[key]) < 2:
			del words[key]
		elif len(words[key]) == 2:
			# A match! Add these.
			s += 2
			used.extend(words[key])
		else:
			ts, tused = make_pairs(words[key])
			s += ts
			for word in set(words[key]) - set(tused):
				pass
	return s, used


def main():
	from sys import stdin, stdout

	rl = stdin.readline
	wl = stdout.write
	int1 = int

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

		s = 0
		for key, value in words.items():
			ts, tused = make_pairs(value)
			s += ts
		print(s)


main()
