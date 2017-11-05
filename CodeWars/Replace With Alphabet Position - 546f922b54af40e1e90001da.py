def alphabet_position(text):
	chars = "abcdefghijklmnopqrstuvwxyz"
	ans = ""
	for i in text:
		i = i.lower()
		if i in chars:
			if ans:
				ans += " " + str(chars.find(i) + 1)
			else:
				ans += str(chars.find(i) + 1)

	return ans
