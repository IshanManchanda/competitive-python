def main():
	import sys
	from numpy.random import permutation as perm
	from tqdm import tqdm

	sys.stdin = open("input.txt")
	rl = sys.stdin.readline
	int1 = int
	range1 = range
	len1 = len
	list1 = list
	set1 = set
	str1 = str

	n = int1(rl())
	himages = []
	vimages = []
	ha, va = himages.append, vimages.append

	for i in range1(n):
		line = rl().strip()
		o, ntags = line.split(' ')[:2]
		tags = line.split()[2:]
		if o == 'H':
			ha((tags, i + 1))
		else:
			va((tags, i + 1))

	ms = 0
	ma = []
	for i in tqdm(range1(1000)):
		hi = himages.copy()
		ha = hi.append
		vi = perm(vimages)

		for j in range1(len1(vi) // 2):
			ha((
				list1(set1(list1(vi[2 * j][0]) + list1(vi[2 * j + 1][0]))),
				'%d %d' % (vi[2 * j][1], vi[2 * j + 1][1])
			))

		s = 0
		hi = perm(hi)
		a = [str1(hi[0][1])]
		for j in range1(len1(hi) - 1):
			com = 0
			for tag in hi[j][0]:
				if tag in hi[j + 1][0]:
					com += 1

			s += min(len(hi[j][0]) - com, len(hi[j + 1][0]) - com, com)
			a.append(str1(hi[j + 1][1]))

		if s > ms:
			ms = s
			ma = a

	with open('%d.txt' % ms, 'w') as f:
		f.write(str1(len(ma)) + '\n')
		f.write('\n'.join(ma))


main()
