def rgb(r, g, b):
	vals = "0123456789ABCDEF"
	a = ""
	cols = [r, g, b]
	for col in cols:
		if col > 254:
			a += "FF"
			continue
		if col < 1:
			a += "00"
			continue
		x = ""
		while True:
			q = col / 16
			print(q)
			r = col % 16
			print(r)
			x += vals[r]
			if q == 0:
				break
			col = q
		if len(x) == 1:
			a += "0"
		a += x[::-1]
	return a
