def remove_url_anchor(url):
	ans = ""
	for c in url:
		if c == "#":
			break
		ans += c
	return ans
