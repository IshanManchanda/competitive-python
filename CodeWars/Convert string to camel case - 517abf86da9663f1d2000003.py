def to_camel_case(text):
	cap = False
	a = ""
	for i in text:
		if i not in "-_":
			if cap:
				a += i.upper()
				cap = False
				continue
			a += i
			continue
		cap = True
	return a
