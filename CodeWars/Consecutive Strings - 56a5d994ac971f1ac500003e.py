def longest_consec(strarr, k):
	if len(strarr) == 0 or k > len(strarr) or k <= 0:
		return ""
	num = 0
	string = ""
	for i in range(len(strarr) - k + 1):
		leng = len("".join(strarr[j] for j in range(i, i + k)))
		if num < leng:
			num = leng
			string = "".join(strarr[j] for j in range(i, i + k))
	return string
