nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
inp = raw_input()

for c in inp:
	nums[int(c)] += 1

for i in xrange(0, 10):
	print i, nums[i]
