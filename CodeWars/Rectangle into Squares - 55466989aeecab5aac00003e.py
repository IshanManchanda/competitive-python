def sqInRect(lng, wdth):
	if lng == wdth:
		return None
	a = []
	while True:
		if lng == wdth:
			return a + [lng]
		if lng > wdth:
			a += [wdth]
			lng = lng - wdth
		else:
			a += [lng]
			wdth = wdth - lng
