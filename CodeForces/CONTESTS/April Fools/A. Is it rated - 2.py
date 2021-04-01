def main():
	from sys import stdin, stdout
	wl = stdout.write
	flush = stdout.flush

	for _ in stdin:
		wl("NO\n")
		flush()


main()
