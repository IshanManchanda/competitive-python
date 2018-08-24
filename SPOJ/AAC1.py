from collections import defaultdict


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):
		visited[v] = True

		for i in self.graph[v]:
			if not visited[i]:
				self.DFSUtil(i, visited)

	def DFS(self, v):
		visited = [False] * (len(self.graph))
		self.DFSUtil(v, visited)


def main():
	from sys import stdin, stdout
	rl = stdin.readline
	wl = stdout.write
	int1 = int
	range1 = range
	map1 = map
	str1 = str

	for _ in range1(int1(rl())):
		n, m = map1(int1, rl().split())
		g = Graph()
		for _ in range1(m):
			x, y = map1(int1, rl().split())
			g.addEdge(x - 1, y - 1)
			g.addEdge(y - 1, x - 1)
		# wl(g.DFS(0))
		g.DFS(0)


main()
