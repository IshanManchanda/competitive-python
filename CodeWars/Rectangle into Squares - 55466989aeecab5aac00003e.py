def sqInRect(length, width):
	if length == width:
		return None
	a = []
	while True:
		if length == width:
			return a + [length]
		if length > width:
			a += [width]
			length = length - width
		else:
			a += [length]
			width = width - length
