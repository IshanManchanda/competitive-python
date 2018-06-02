nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
inp = input()

for c in inp:
	nums[int(c)] += 1

for i in range(0, 10):
	print(i, nums[i])
