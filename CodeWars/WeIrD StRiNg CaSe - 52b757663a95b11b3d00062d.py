def to_weird_case(string):
	a = ""
	c = True
	for i in string:
		if i == " ":
			c = True
			a += i
			continue
		if c:
			a += i.upper()
		else:
			a += i.lower()
		c = not c
	return a
