def get_middle(s):
	l = len(s)
	if l % 2 == 1:
		return s[(l - 1) / 2]
	return s[(l / 2) - 1: (l / 2) + 1]
