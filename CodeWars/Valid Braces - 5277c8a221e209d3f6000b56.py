def validBraces(string):
	match = {"(": ")", "[": "]", "{": "}"}
	opening, closing = "({[", ")}]"
	opened = ""
	for i in string:
		try:
			print(opened)
			if i in opening:
				opened += i
			elif i in closing:
				if i == match[opened[-1]]:
					opened = opened[:-1]
				else:
					return False
		except Exception:
			pass
	return opened == ""
